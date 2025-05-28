from datetime import date, datetime, timedelta, time
import os
import re
from typing import Dict
from flask import Flask, current_app, jsonify, render_template, request, redirect, url_for
from BUS.san_bus import SanBus
from DAO.san_dao import SanDAO
from BUS.taikhoanBUS import TaiKhoanBUS
from DAO.db_config import get_connection
from BUS.nhanvien_bus import NhanVienBus
from DAO.hoadon_dao import HoaDonDAO
from BUS.hoadon_bus import HoaDonBUS
from BUS.NguoiDung_BUS import NguoiDung_BUS
from BUS.phieughiBUS import PhieuGhiBUS
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Khởi tạo Flask app
app = Flask(__name__, template_folder='GUI')

# Tạo thư mục lưu trữ ảnh nếu chưa tồn tại
if not os.path.exists('GUI/static/asset'):
    os.makedirs('GUI/static/asset')

# Khởi tạo connection, DAO và BUS
conn = get_connection()
dao = SanDAO(conn)
san_bus = SanBus(dao)
taikhoan = TaiKhoanBUS()
khachhang = NguoiDung_BUS()
phieughi = PhieuGhiBUS()
hoa_don_dao = HoaDonDAO(conn)
hoa_don_bus = HoaDonBUS(hoa_don_dao)

# Sân
@app.route('/<role>/san')
def quan_ly_san(role):
    danh_sach_san = san_bus.lay_danh_sach_san()
    # Filter only items where status == 1
    danh_sach_san = [san for san in danh_sach_san if isinstance(san, dict) and san.get('status') == 1]
    for san in danh_sach_san:
        hinh_anh = san.get('HinhAnh')
        if hinh_anh is None or not hinh_anh:
            san['HinhAnh'] = url_for('static', filename='asset/default.jpg')
        else:
            if 'asset/' in hinh_anh:
                san['HinhAnh'] = url_for('static', filename=hinh_anh)
            else:
                san['HinhAnh'] = url_for('static', filename=f'asset/{hinh_anh}')
    return render_template('san.html', danh_sach_san=danh_sach_san, role=role)

@app.route('/<role>/them-san', methods=['POST'])
def them_san(role):
    try:
        co_san = request.form.get('CoSan')
        dia_chi = request.form.get('DiaChi')
        hinh_anh = request.files.get('HinhAnh')
        so_san = request.form.get('SoSan')
        mo_ta = request.form.get('MoTa')
        trang_thai = request.form.get('TrangThai')
        gia_san = request.form.get('GiaSan')

        print(f"Received data - CoSan: {co_san}, DiaChi: {dia_chi}, HinhAnh: {hinh_anh}, SoSan: {so_san}, MoTa: {mo_ta}, TrangThai: {trang_thai}, GiaSan: {gia_san}", flush=True)

        if not co_san or co_san not in ['5', '7', '9', '11']:
            return jsonify({'success': False, 'error': 'Cỡ sân không hợp lệ'}), 400
        if not dia_chi:
            return jsonify({'success': False, 'error': 'Địa chỉ không được để trống'}), 400
        if not so_san or so_san not in ['1', '2', '3', '4']:
            return jsonify({'success': False, 'error': 'Số sân không hợp lệ'}), 400
        if not trang_thai or trang_thai not in ['0', '1']:
            return jsonify({'success': False, 'error': 'Trạng thái không hợp lệ'}), 400
        try:
            gia_san = int(gia_san)
            if gia_san <= 0:
                return jsonify({'success': False, 'error': 'Giá sân phải là số nguyên dương'}), 400
        except (ValueError, TypeError):
            return jsonify({'success': False, 'error': 'Giá sân phải là số nguyên'}), 400

        hinh_anh_path = None
        if hinh_anh and hinh_anh.filename:
            if not hinh_anh.mimetype.startswith('image/'):
                return jsonify({'success': False, 'error': 'Định dạng ảnh không hợp lệ'}), 400
            filename = hinh_anh.filename
            hinh_anh_path = f"asset/{filename}"
            hinh_anh.save(os.path.join('GUI/static', hinh_anh_path))
        else:
            hinh_anh_path = 'default.jpg'

        du_lieu_san = {
            'coSan': co_san,
            'diaChi': dia_chi,
            'hinhAnh': hinh_anh_path,
            'soSan': so_san,
            'moTa': mo_ta if mo_ta else None,
            'trangThai': trang_thai,
            'giaSan': gia_san,
            'status': 1  # Ensure status is set to 1 for new records
        }
        print(f"Sending to SanBus: {du_lieu_san}", flush=True)
        result = san_bus.them_san(du_lieu_san)
        if isinstance(result, dict) and 'idSan' in result:
            return jsonify({'success': True, 'idSan': result['idSan']})
        else:
            return jsonify({'success': False, 'error': str(result)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': f'Lỗi server: {str(e)}'}), 500

@app.route('/<role>/xoa-san/<int:id_san>')
def xoa_san(role, id_san):
    print(san_bus.xoa_san(id_san), flush=True)
    return redirect(url_for('quan_ly_san', role=role))

@app.route('/<role>/sua-san/<int:id>', methods=['POST'])
def sua_san(role, id):
    try:
        co_san = request.form.get('CoSan')
        dia_chi = request.form.get('DiaChi')
        hinh_anh = request.files.get('HinhAnh')
        so_san = request.form.get('SoSan')
        mo_ta = request.form.get('MoTa')
        trang_thai = request.form.get('TrangThai')
        gia_san = request.form.get('GiaSan')

        print(f"Received data - Id: {id}, CoSan: {co_san}, DiaChi: {dia_chi}, HinhAnh: {hinh_anh}, SoSan: {so_san}, MoTa: {mo_ta}, TrangThai: {trang_thai}, GiaSan: {gia_san}", flush=True)

        if not co_san or co_san not in ['5', '7', '9', '11']:
            return jsonify({'success': False, 'error': 'Cỡ sân không hợp lệ'}), 400
        if not dia_chi:
            return jsonify({'success': False, 'error': 'Địa chỉ không được để trống'}), 400
        if not so_san or so_san not in ['1', '2', '3', '4']:
            return jsonify({'success': False, 'error': 'Số sân không hợp lệ'}), 400
        if not trang_thai or trang_thai not in ['0', '1']:
            return jsonify({'success': False, 'error': 'Trạng thái không hợp lệ'}), 400
        try:
            gia_san = int(gia_san)
            if gia_san <= 0:
                return jsonify({'success': False, 'error': 'Giá sân phải là số nguyên dương'}), 400
        except (ValueError, TypeError):
            return jsonify({'success': False, 'error': 'Giá sân phải là số nguyên'}), 400

        hinh_anh_path = None
        if hinh_anh and hinh_anh.filename:
            if not hinh_anh.mimetype.startswith('image/'):
                return jsonify({'success': False, 'error': 'Định dạng ảnh không hợp lệ'}), 400
            filename = hinh_anh.filename
            hinh_anh_path = f"asset/{filename}"
            hinh_anh.save(os.path.join('GUI/static', hinh_anh_path))

        du_lieu_moi = {
            'coSan': co_san,
            'diaChi': dia_chi,
            'hinhAnh': hinh_anh_path,
            'soSan': so_san,
            'moTa': mo_ta if mo_ta else None,
            'trangThai': trang_thai,
            'giaSan': gia_san,
            'status': 1  # Ensure status remains 1 for updated records
        }
        print(f"Sending to SanBus for update: {du_lieu_moi}", flush=True)
        ket_qua = san_bus.sua_san(id, du_lieu_moi)
        if ket_qua.get('success', False):
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': ket_qua.get('error', 'Lỗi không xác định')}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': f'Lỗi server: {str(e)}'}), 500

# Nhân viên
nhanvien_bus = NhanVienBus()

@app.route('/<role>/nhanvien')
def quan_ly_nhan_vien(role):
    danh_sach_nhan_vien = nhanvien_bus.lay_danh_sach_nhan_vien()
    # Filter only items where status == 1
    danh_sach_nhan_vien = [nv for nv in danh_sach_nhan_vien if isinstance(nv, dict) and nv.get('status') == 1]
    tong_nhan_vien = len(danh_sach_nhan_vien)
    so_luong_hd = sum(1 for nv in danh_sach_nhan_vien if isinstance(nv, dict) and nv.get('hoatdong') == 'Hoạt động')
    so_luong_np = sum(1 for nv in danh_sach_nhan_vien if isinstance(nv, dict) and nv.get('hoatdong') == 'Nghỉ phép')
    now = datetime.now()
    thang_hien_tai = now.month
    nam_hien_tai = now.year
    so_nv_moi = sum(
        1 for nv in danh_sach_nhan_vien
        if 'ngayvaolam' in nv and isinstance(nv['ngayvaolam'], str)
        and datetime.strptime(nv['ngayvaolam'], '%Y-%m-%d').month == thang_hien_tai
        and datetime.strptime(nv['ngayvaolam'], '%Y-%m-%d').year == nam_hien_tai
    )
    return render_template('quanlinhanvien.html', danh_sach_nhan_vien=danh_sach_nhan_vien, soluongnv=tong_nhan_vien, slhd=so_luong_hd, nvm=so_nv_moi, nvnp=so_luong_np)

@app.route('/<role>/them-nhan-vien', methods=['POST'])
def them_nhan_vien(role):
    ho_ten = request.form.get('HoTen')
    ngay_sinh = request.form.get('NgaySinh')
    sdt = request.form.get('SDT')
    dia_chi = request.form.get('DiaChi')
    cccd = request.form.get('cccd')
    gioitinh = request.form.get('gioitinh')
    chuc_vu = request.form.get('chuc_vu')
    vi_tri = request.form.get('vi_tri')
    ngay_vao_lam = request.form.get('ngayvaolam')
    hop_dong = request.form.get('hopdong')
    hoat_dong = request.form.get('hoatdong')
    mo_ta = request.form.get('mota')
    luong = request.form.get('luong')
    phu_cap = request.form.get('phucap')
    ngan_hang = request.form.get('nganhang')
    ten_tai_khoan = request.form.get('ten_tai_khoan')
    mat_khau = request.form.get('mat_khau')
    ngay_tao = request.form.get('ngay_tao')
    acc_type = request.form.get('nhom_quyen')
    du_lieu_tai_khoan = {'TenTaiKhoan': ten_tai_khoan, 'MatKhau': mat_khau, 'NgayTao': ngay_tao, 'AccType': acc_type, 'status': 1}
    result_taikhoan = taikhoan.them_tknv(du_lieu_tai_khoan)
    id_tai_khoan = taikhoan.get_max_id_taikhoan()
    du_lieu_nhan_vien = {
        'HoTen': ho_ten, 'NgaySinh': ngay_sinh, 'SDT': sdt, 'DiaChi': dia_chi, 'IdTaiKhoan': id_tai_khoan,
        'cccd': cccd, 'gioitinh': gioitinh, 'chuc_vu': chuc_vu, 'vi_tri': vi_tri, 'ngayvaolam': ngay_vao_lam,
        'hopdong': hop_dong, 'hoatdong': hoat_dong, 'mota': mo_ta, 'luong': luong, 'phucap': phu_cap if phu_cap else 0,
        'nganhang': ngan_hang if ngan_hang else '', 'status': 1
    }
    result_nhanvien = nhanvien_bus.them_nhan_vien(du_lieu_nhan_vien)
    print(f"Kết quả thêm nhân viên từ BUS: {result_nhanvien}")
    if result_nhanvien.get('success'):
        print("Thêm nhân viên thành công!")
        danh_sach_nhan_vien = nhanvien_bus.lay_danh_sach_nhan_vien()
    else:
        print(f"Thêm nhân viên thất bại: {result_nhanvien.get('error', 'Không có thông tin lỗi')}")
        taikhoan.xoaTaiKhoan(id_tai_khoan)
    return redirect(url_for('quan_ly_nhan_vien', role=role))

@app.route('/<role>/xoa-nhan-vien/<int:id_nhan_vien>', methods=['POST'])
def xoa_nhan_vien(role, id_nhan_vien):
    try:
        ket_qua = nhanvien_bus.xoa_nhan_vien(id_nhan_vien)
        if ket_qua.get('success', False):
            return jsonify({'success': True, 'message': 'Xóa nhân viên thành công'}), 200
        else:
            return jsonify({'success': False, 'error': ket_qua.get('error', 'Lỗi khi xóa nhân viên')}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': f'Lỗi server: {str(e)}'}), 500

@app.route('/<role>/sua-nhan-vien/<int:id>', methods=['POST'])
def sua_nhan_vien(role, id):
    try:
        du_lieu_moi = {
            'HoTen': request.form.get('HoTen'),
            'NgaySinh': request.form.get('NgaySinh'),
            'SDT': request.form.get('SDT'),
            'DiaChi': request.form.get('DiaChi'),
            'cccd': request.form.get('cccd'),
            'gioitinh': request.form.get('gioitinh'),
            'chuc_vu': request.form.get('chuc_vu'),
            'vi_tri': request.form.get('vi_tri'),
            'ngayvaolam': request.form.get('ngayvaolam'),
            'hopdong': request.form.get('hopdong'),
            'hoatdong': request.form.get('hoatdong'),
            'mota': request.form.get('mota'),
            'luong': request.form.get('luong'),
            'phucap': request.form.get('phucap', '0'),
            'nganhang': request.form.get('nganhang', ''),
            'IdTaiKhoan': request.form.get('IdTaiKhoan', '0'),
            'ten_tai_khoan': request.form.get('ten_tai_khoan'),
            'mat_khau': request.form.get('mat_khau'),
            'nhom_quyen': request.form.get('nhom_quyen'),
            'ngay_tao': request.form.get('ngay_tao'),
            'status': 1
        }
        ket_qua = nhanvien_bus.sua_nhan_vien(id, du_lieu_moi)
        if ket_qua.get('success', False):
            return jsonify({'success': True, 'message': 'Cập nhật nhân viên thành công'}), 200
        else:
            return jsonify({'success': False, 'error': ket_qua.get('error', 'Lỗi không xác định')}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': f'Lỗi server: {str(e)}'}), 500

# Người dùng
def get_asset_path():
    return os.path.join(current_app.root_path, 'static', 'asset')

@app.route('/user/<userID>')
def nguoidung(userID: int):
    PhieuGhiBUS.danhSachPhieuGhi = phieughi.getListByDate(datetime.now().date())
    danh_sach_san = san_bus.lay_danh_sach_san()
    # Filter only items where status == 1
    danh_sach_san = [san for san in danh_sach_san if isinstance(san, dict) and san.get('status') == 1]
    for san in danh_sach_san:
        hinh_anh = san.get('HinhAnh', 'default.jpg') or 'default.jpg'
        if 'asset/' in hinh_anh:
            san['HinhAnh'] = url_for('static', filename=hinh_anh)
        else:
            san['HinhAnh'] = url_for('static', filename=f'asset/{hinh_anh}')
    hoa_don_list = hoa_don_bus.getHoaDonByUserId(userID)
    return render_template('user.html', userID=userID, san=danh_sach_san, hoa_don_list = hoa_don_list)

@app.route('/user/<int:userID>/render-date/<date>', methods=['POST'])
def renderBooking(userID: int, date):
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()
    PhieuGhiBUS.danhSachPhieuGhi = phieughi.getListByDate(date_obj)
    # Filter only items where status == 1
    PhieuGhiBUS.danhSachPhieuGhi = [pg for pg in PhieuGhiBUS.danhSachPhieuGhi if isinstance(pg, dict) and pg.get('status') == 1]
    print(PhieuGhiBUS.danhSachPhieuGhi, flush=True)
    return jsonify(PhieuGhiBUS.danhSachPhieuGhi)

def serialize_date(obj):
    if isinstance(obj, (datetime, date)):
        return obj.strftime('%Y-%m-%d')
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

@app.route('/user/<int:userID>/dat_san/<int:sanID>/ngay/<date>/khung_gio/<khung_gio>/gia/<gia>/phuongthuc/<phuongThuc>', methods=['POST'])
def datsan(userID: int, sanID: int, date, khung_gio, gia, phuongThuc):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.now().date()
        if date_obj < today:
            return jsonify({'success': False, 'error': 'Không thể đặt sân cho ngày đã qua'}), 400

        if not re.match(r'^\d{2}:\d{2}-\d{2}:\d{2}$', khung_gio):
            return jsonify({'success': False, 'error': 'Định dạng khung giờ không hợp lệ'}), 400

        start_time_str, end_time_str = khung_gio.split('-')
        start_datetime = datetime.strptime(f"{date} {start_time_str}", '%Y-%m-%d %H:%M')
        end_datetime = datetime.strptime(f"{date} {end_time_str}", '%Y-%m-%d %H:%M')

        now = datetime.now()
        time_diff = (start_datetime - now).total_seconds() / 60
        if time_diff < 15:
            return jsonify({'success': False, 'error': 'Không thể đặt sân trong vòng 15 phút tới'}), 400

        if end_datetime <= start_datetime:
            return jsonify({'success': False, 'error': 'Thời gian kết thúc phải sau thời gian bắt đầu'}), 400

        try:
            gia_value = float(gia)
            if gia_value <= 0:
                return jsonify({'success': False, 'error': 'Giá phải lớn hơn 0'}), 400
        except ValueError:
            return jsonify({'success': False, 'error': 'Giá không hợp lệ'}), 400

        nguoi_dung = khachhang.getNguoiDungById(userID)
        if not nguoi_dung or nguoi_dung.get('status') != 1:
            return jsonify({'success': False, 'error': 'Không tìm thấy thông tin người dùng hợp lệ'}), 400

        du_lieu_hoa_don = {
            'Ngay': date_obj,
            'TongTien': gia_value,
            'PhuongThuc': phuongThuc,
            'TrangThai': 0,
            'IdNhanVien': None,
            'IdNguoiDung': userID,
            'status': 1
        }
        result_hoa_don = hoa_don_bus.them_hoa_don(du_lieu_hoa_don)
        print(f"DEBUG: Result from hoa_don_bus.them_hoa_don: {result_hoa_don}", flush=True)
        if not result_hoa_don.get('success', False):
            return jsonify({'success': False, 'error': 'Không thể tạo hóa đơn: ' + result_hoa_don.get('error', 'Lỗi không xác định')}), 400

        id_hoa_don = result_hoa_don.get('IdHoaDon')
        if not id_hoa_don:
            return jsonify({'success': False, 'error': 'Không thể lấy IdHoaDon sau khi tạo hóa đơn'}), 500

        du_lieu_phieu_ghi = {
            'Ngay': date_obj,
            'KhungGio': khung_gio,
            'GiaTien': gia_value,
            'IdSan': sanID,
            'IdHoaDon': id_hoa_don,
            'status': 1
        }

        print(f"DEBUG: Dữ liệu phiếu ghi: {du_lieu_phieu_ghi}", flush=True)

        result = phieughi.themPhieuGhi(du_lieu_phieu_ghi)
        print(f"DEBUG: Result from phieughi.themPhieuGhi: {result}", flush=True)
        if result.get('success', False):
            return jsonify({
                'success': True,
                'message': 'Đặt sân thành công, phiếu ghi đã được tạo với trạng thái Chờ xác nhận',
                'IdPhieuGhi': result.get('IdPhieuGhi'),
                'IdHoaDon': id_hoa_don
            })
        else:
            hoa_don_bus.xoa_hoa_don(id_hoa_don)
            return jsonify({
                'success': False,
                'error': result.get('error', 'Lỗi không xác định')
            }), 400

    except ValueError as ve:
        print(f"Lỗi định dạng dữ liệu: {ve}", flush=True)
        return jsonify({'success': False, 'error': 'Dữ liệu đầu vào không hợp lệ'}), 400
    except Exception as e:
        print(f"Lỗi khi xử lý đặt sân: {e}", flush=True)
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/user/<int:userID>/hoa-don', methods=['GET'])
def get_history(userID: int):
    try:
        hoa_don_list = hoa_don_bus.getHoaDonByUserId(userID)
        print(f"DEBUG: Raw hoa_don_list from BUS: {hoa_don_list}")  # Log dữ liệu thô
        # Chuyển đổi các đối tượng datetime.date thành chuỗi
        serialized_list = []
        for hoa_don in hoa_don_list:
            serialized_hoa_don = dict(hoa_don)
            if 'Ngay' in serialized_hoa_don and isinstance(serialized_hoa_don['Ngay'], (datetime, date)):
                serialized_hoa_don['Ngay'] = serialized_hoa_don['Ngay'].strftime('%Y-%m-%d')
            serialized_list.append(serialized_hoa_don)
        print(f"DEBUG: Serialized hoa_don_list: {serialized_list}")  # Log dữ liệu sau serialize
        return jsonify({'success': True, 'hoa_don_list': serialized_list})
    except Exception as e:
        print(f"Lỗi khi lấy lịch sử: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

# Đăng nhập & Đăng ký
@app.route('/login')
def dangNhap():
    return render_template('dangnhap_dangki.html')

def render_index_template(context=None, AccType=None):
    default_context = {
        'pg': [], 'san': [], 'today_date': datetime.now().strftime("%Y-%m-%d"),
        'today_revenue': 0, 'booked_fields': 0, 'total_fields': 0
    }
    if context:
        default_context.update(context)
    return render_template('quanlitaichinh.html', **default_context, AccType=AccType)

@app.route('/processing', methods=['POST'])
def xuLiDangNhap():
    print(request.form.to_dict(), flush=True)
    result = taikhoan.dangNhapTaiKhoan(request.form.to_dict())
    if result.get('success'):
        if result.get('AccType') == "user":
            return redirect(url_for('nguoidung', userID=result.get('IdTaiKhoan')))
        else:
            return redirect(url_for('quanlitaichinh', role=result.get('AccType')))
    else:
        return redirect('/login')

@app.route('/signUp', methods=['POST'])
def xuliDangKi():
    birth = request.form.to_dict()['date']
    date_obj = datetime.strptime(birth, '%Y-%m-%d').date()
    adjDatas = request.form.to_dict()
    adjDatas['date'] = date_obj
    adjDatas['status'] = 1
    return taikhoan.dangKiTaiKhoan(adjDatas)

# Hóa đơn
@app.route('/hoa-don')
def quan_ly_hoa_don():
    danh_sach_hoa_don = hoa_don_bus.lay_danh_sach_hoa_don()
    # Filter only items where status == 1
    danh_sach_hoa_don = [hd for hd in danh_sach_hoa_don if isinstance(hd, dict) and hd.get('status') == 1]
    return render_template('hoadon.html', danh_sach_hoa_don=danh_sach_hoa_don)

@app.route('/them-hoa-don', methods=['POST'])
def them_hoa_don():
    data = request.get_json()
    ngay = data.get('Ngay')
    tong_tien = data.get('TongTien')
    id_nhan_vien = data.get('IdNhanVien')
    du_lieu_hoa_don = {
        'Ngay': ngay,
        'TongTien': tong_tien,
        'PhuongThuc': data.get('PhuongThuc', 'Tiền mặt'),
        'TrangThai': 0 if data.get('TrangThai') == 'Chờ xác nhận' else data.get('TrangThai', 0),  # Chuyển thành số
        'IdNhanVien': id_nhan_vien,
        'IdNguoiDung': data.get('IdNguoiDung'),
        'status': 1
    }
    result = hoa_don_bus.them_hoa_don(du_lieu_hoa_don)
    if isinstance(result, dict) and 'IdHoaDon' in result:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': str(result)})

@app.route('/xoa-hoa-don/<int:id_hoa_don>', methods=['POST'])
def xoa_hoa_don(id_hoa_don):
    result = hoa_don_bus.xoa_hoa_don(id_hoa_don)
    if result:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'Không thể xóa hóa đơn'})

@app.route('/sua-hoa-don/<int:id>', methods=['POST'])
def sua_hoa_don(id):
    data = request.get_json()
    ngay = data.get('Ngay')
    tong_tien = data.get('TongTien')
    id_nhan_vien = data.get('IdNhanVien')
    du_lieu_moi = {
        'Ngay': ngay,
        'TongTien': tong_tien,
        'IdNhanVien': id_nhan_vien,
        'status': 1
    }
    ket_qua = hoa_don_bus.sua_hoa_don(id, du_lieu_moi)
    if ket_qua:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'Không thể sửa hóa đơn'})

# Quản lý khách hàng
@app.route('/<role>/khachhang')
def quanlikhachhang(role):
    return render_template('quanlikhachhang.html')

@app.route('/<role>/khachhang/xoa_id/<int:IdNguoiDung>', methods=['POST'])
def xoa_khachhang(role, IdNguoiDung: int):
    result = khachhang.xoaNguoiDung(IdNguoiDung)
    return jsonify(result)

@app.route('/<role>/khachhang/timkiem/<key>/<type>', methods=['POST'])
def tim_khachhang(role, key: str, type: str):
    total = khachhang.timKhachHang("")
    # Filter only items where status == 1
    total = [kh for kh in total if isinstance(kh, dict) and kh.get('status') == 1]
    listGuest = khachhang.timKhachHang(key, type)
    listGuest = [kh for kh in listGuest if isinstance(kh, dict) and kh.get('status') == 1]
    today = datetime.today().date()
    data = {
        "list": listGuest,
        'data': {
            'total': len(total),
            'month': len([kh for kh in taikhoan.getListByDate(today - timedelta(days=30), 'user') if isinstance(kh, dict) and kh.get('status') == 1]),
            'week': len([kh for kh in taikhoan.getListByDate(today - timedelta(days=7), 'user') if isinstance(kh, dict) and kh.get('status') == 1]),
            'return': len([pg for pg in phieughi.getReturn() if isinstance(pg, dict) and pg.get('status') == 1]) / len(total) if total else 0
        }
    }
    for x in listGuest:
        x['SoLuong'] = len([hd for hd in hoa_don_bus.lay_danh_sach_hoa_don(x['IdNguoiDung']) if isinstance(hd, dict) and hd.get('status') == 1])
        x['TongTien'] = khachhang.getTongTien(x['IdNguoiDung'])
    return jsonify(data)

@app.route('/<role>/khachhang/load/<type>', methods=['POST'])
def load_khachhang(role, type: str):
    total = khachhang.timKhachHang("")
    # Filter only items where status == 1
    total = [kh for kh in total if isinstance(kh, dict) and kh.get('status') == 1]
    listGuest = khachhang.timKhachHang("", type)
    listGuest = [kh for kh in listGuest if isinstance(kh, dict) and kh.get('status') == 1]
    today = datetime.today().date()
    data = {
        "list": listGuest,
        'data': {
            'total': len(total),
            'month': len([kh for kh in taikhoan.getListByDate(today - timedelta(days=30), 'user') if isinstance(kh, dict) and kh.get('status') == 1]),
            'week': len([kh for kh in taikhoan.getListByDate(today - timedelta(days=7), 'user') if isinstance(kh, dict) and kh.get('status') == 1]),
            'return': len([pg for pg in phieughi.getReturn() if isinstance(pg, dict) and pg.get('status') == 1]) / len(total) if total else 0
        }
    }
    for x in listGuest:
        x['SoLuong'] = len([hd for hd in hoa_don_bus.lay_danh_sach_hoa_don(x['IdNguoiDung']) if isinstance(hd, dict) and hd.get('status') == 1])
        x['TongTien'] = khachhang.getTongTien(x['IdNguoiDung'])
        x['TrangThai'] = khachhang.getTrangThai(x['IdNguoiDung'])
    print(listGuest, flush=True)
    return jsonify(data)

@app.route('/<role>/khachhang/sua', methods=['POST'])
def editKhachHang(role):
    adjDatas = request.form.to_dict()
    adjDatas['NgaySinh'] = None
    adjDatas['status'] = 1
    print(adjDatas, flush=True)
    return jsonify(khachhang.suaNguoiDung(adjDatas))

@app.route('/<role>/khachhang/them', methods=['POST'])
def addKhachHang(role):
    adjDatas = request.form.to_dict()
    adjDatas['NgaySinh'] = None
    adjDatas['NgayTao'] = datetime.today().date()
    adjDatas['status'] = 1
    print(adjDatas, flush=True)
    return jsonify(khachhang.themNguoiDung(adjDatas))

@app.route('/<role>/khachhang/status', methods=['POST'])
def statusUpdate(role):
    adjDatas = request.get_json()
    adjDatas['status'] = 1
    print(adjDatas, flush=True)
    return jsonify(taikhoan.status(adjDatas))

# Báo cáo & Thống kê
@app.route("/<role>/baocao")
def baocao(role):
    from collections import defaultdict
    import datetime
    hd = hoa_don_bus.lay_danh_sach_hoa_don() or []
    # Filter only items where status == 1
    hd = [invoice for invoice in hd if isinstance(invoice, dict) and invoice.get('status') == 1]
    monthly_revenue = defaultdict(float)
    for invoice in hd:
        ngay_value = invoice.get('Ngay')
        if ngay_value is not None:
            if isinstance(ngay_value, datetime.date):
                ngay = ngay_value
            else:
                ngay = datetime.strptime(ngay_value, '%Y-%m-%d').date()
            if ngay.year == 2025:
                month = ngay.month
                monthly_revenue[month] += float(invoice.get('TongTien', 0))
    phieu_ghi = phieughi.getListPhieuGhi(None)
    # Filter only items where status == 1
    phieu_ghi = [pg for pg in phieu_ghi if isinstance(pg, dict) and pg.get('status') == 1]
    print("phieu_ghi in main.py:", phieu_ghi)
    field_counts = defaultdict(int)
    for item in phieu_ghi:
        id_san = item.get('IdSan')
        if id_san is not None:
            field_counts[id_san] += 1
    print("field_counts:", dict(field_counts))
    months = range(1, 13)
    revenue_data = [monthly_revenue.get(month, 0) for month in months]
    total_revenue = sum(revenue_data) if revenue_data else 0
    total_orders = len(hd) if hd else 0
    return render_template("baocao.html",
                           invoices=hd,
                           total_revenue=total_revenue,
                           total_orders=total_orders,
                           monthly_revenue=revenue_data,
                           phieu_ghi=phieu_ghi,
                           field_counts=dict(field_counts),
                           months=[f'Tháng {m}' for m in months])

# Quản lý tài chính
@app.route('/<role>/quanlitaichinh')
def quanlitaichinh(role):
    return render_template('quanlitaichinh.html', role=role)

@app.route('/<role>/quanlitaichinh/timkiem/<key>/<type>', methods=['POST'])
def tim_taichinh(role, key: str, type: str):
    listHD = hoa_don_bus.timkiemHD(key, type)
    # Filter only items where status == 1
    listHD = [hd for hd in listHD if isinstance(hd, dict) and hd.get('status') == 1]
    income: Dict = hoa_don_bus.getMonthlyIncome()
    tabs = hoa_don_bus.getTabs()
    total = 0
    for x in income.values():
        total += x
    tabs['total'] = total
    data = {"list": listHD, "income": income, "fees": tabs}
    return jsonify(data)

@app.route('/<role>/quanlitaichinh/load/<type>', methods=['POST'])
def load_taichinh(role, type: str):
    listHD = hoa_don_bus.timkiemHD("", type)
    # Filter only items where status == 1
    listHD = [hd for hd in listHD if isinstance(hd, dict) and hd.get('status') == 1]
    for x in listHD:
        x['Ngay'] = str(x['Ngay'])
    income: Dict = hoa_don_bus.getMonthlyIncome()
    tabs = hoa_don_bus.getTabs()
    total = 0
    for x in income.values():
        total += x
    tabs['total'] = total
    data = {"list": listHD, "income": income, "fees": tabs}
    return jsonify(data)

@app.route('/<role>/quanlitaichinh/edit/<int:IDHD>/<Status>', methods=['POST'])
def editState(role, IDHD: int, Status):
    result = hoa_don_bus.editState(IDHD, Status)
    return jsonify(result)

@app.route('/them-phieu-ghi', methods=['POST'])
def themphieughi():
    try:
        data = request.get_json()
        ho_ten = data.get('hoTen')
        id_san = int(data.get('idSan'))
        khung_gio = data.get('khungGio')
        gia = float(data.get('gia'))
        trang_thai = data.get('trangThai', 'Chờ xác nhận')

        du_lieu_phieu_ghi = {
            'HoTen': ho_ten,
            'IdSan': id_san,
            'KhungGio': khung_gio,
            'Gia': gia,
            'TrangThai': trang_thai,
            'Ngay': datetime.now().date(),
            'status': 1
        }

        result = phieughi.themPhieuGhi(du_lieu_phieu_ghi)
        if result.get('success', False):
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': result.get('error', 'Lỗi không xác định')}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': f'Lỗi server: {str(e)}'}), 500

# Trang mở đầu
@app.route('/')
def index():
    danh_sach_san = san_bus.lay_danh_sach_san()
    # Filter only items where status == 1
    danh_sach_san = [san for san in danh_sach_san if isinstance(san, dict) and san.get('status') == 1]
    for san in danh_sach_san:
        hinh_anh = san.get('HinhAnh', 'default.jpg') or 'default.jpg'
        if 'asset/' in hinh_anh:
            san['HinhAnh'] = url_for('static', filename=hinh_anh)
        else:
            san['HinhAnh'] = url_for('static', filename=f'asset/{hinh_anh}')
    return render_template('dangnhap_dangki.html', san=danh_sach_san)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)