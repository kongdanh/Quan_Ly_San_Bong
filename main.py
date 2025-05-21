from datetime import datetime, timedelta
import os
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
@app.route('/san')
def quan_ly_san():
    danh_sach_san = san_bus.lay_danh_sach_san()
    for san in danh_sach_san:
        if isinstance(san, dict):
            hinh_anh = san.get('HinhAnh')
            if hinh_anh is None or not hinh_anh:
                san['HinhAnh'] = url_for('static', filename='asset/default.jpg')
            else:
                # Chỉ thêm 'asset/' nếu chưa có trong hinh_anh
                if 'asset/' in hinh_anh:
                    san['HinhAnh'] = url_for('static', filename=hinh_anh)
                else:
                    san['HinhAnh'] = url_for('static', filename=f'asset/{hinh_anh}')
    return render_template('san.html', danh_sach_san=danh_sach_san)

@app.route('/them-san', methods=['POST'])
def them_san():
    try:
        co_san = request.form.get('CoSan')
        dia_chi = request.form.get('DiaChi')
        hinh_anh = request.files.get('HinhAnh')
        so_san = request.form.get('SoSan')
        mo_ta = request.form.get('MoTa')
        trang_thai = request.form.get('TrangThai')
        gia_san = request.form.get('GiaSan')

        # Debug dữ liệu nhận được
        print(f"Received data - CoSan: {co_san}, DiaChi: {dia_chi}, HinhAnh: {hinh_anh}, SoSan: {so_san}, MoTa: {mo_ta}, TrangThai: {trang_thai}, GiaSan: {gia_san}", flush=True)

        # Kiểm tra dữ liệu đầu vào
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

        # Xử lý file upload
        hinh_anh_path = None
        if hinh_anh and hinh_anh.filename:
            if not hinh_anh.mimetype.startswith('image/'):
                return jsonify({'success': False, 'error': 'Định dạng ảnh không hợp lệ'}), 400
            filename = hinh_anh.filename
            hinh_anh_path = f"asset/{filename}"
            hinh_anh.save(os.path.join('GUI/static', hinh_anh_path))
        else:
            hinh_anh_path = 'default.jpg'

        # Gửi dữ liệu đến BUS
        du_lieu_san = {
            'coSan': co_san,
            'diaChi': dia_chi,
            'hinhAnh': hinh_anh_path,
            'soSan': so_san,
            'moTa': mo_ta if mo_ta else None,
            'trangThai': trang_thai,
            'giaSan': gia_san
        }
        print(f"Sending to SanBus: {du_lieu_san}", flush=True)
        result = san_bus.them_san(du_lieu_san)
        if isinstance(result, dict) and 'idSan' in result:
            return jsonify({'success': True, 'idSan': result['idSan']})
        else:
            return jsonify({'success': False, 'error': str(result)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': f'Lỗi server: {str(e)}'}), 500

@app.route('/xoa-san/<int:id_san>')
def xoa_san(id_san):
    san_bus.xoa_san(id_san)
    return redirect(url_for('quan_ly_san'))

@app.route('/sua-san/<int:id>', methods=['POST'])
def sua_san(id):
    try:
        co_san = request.form.get('CoSan')
        dia_chi = request.form.get('DiaChi')
        hinh_anh = request.files.get('HinhAnh')
        so_san = request.form.get('SoSan')
        mo_ta = request.form.get('MoTa')
        trang_thai = request.form.get('TrangThai')
        gia_san = request.form.get('GiaSan')

        # Debug dữ liệu nhận được
        print(f"Received data - Id: {id}, CoSan: {co_san}, DiaChi: {dia_chi}, HinhAnh: {hinh_anh}, SoSan: {so_san}, MoTa: {mo_ta}, TrangThai: {trang_thai}, GiaSan: {gia_san}", flush=True)

        # Kiểm tra dữ liệu đầu vào
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

        # Xử lý file upload
        hinh_anh_path = None
        if hinh_anh and hinh_anh.filename:
            if not hinh_anh.mimetype.startswith('image/'):
                return jsonify({'success': False, 'error': 'Định dạng ảnh không hợp lệ'}), 400
            filename = hinh_anh.filename
            hinh_anh_path = f"asset/{filename}"
            hinh_anh.save(os.path.join('GUI/static', hinh_anh_path))
        # Nếu không upload ảnh mới, giữ nguyên giá trị cũ (cần lấy từ CSDL hoặc không thay đổi)

        # Gửi dữ liệu đến BUS
        du_lieu_moi = {
            'coSan': co_san,
            'diaChi': dia_chi,
            'hinhAnh': hinh_anh_path,
            'soSan': so_san,
            'moTa': mo_ta if mo_ta else None,
            'trangThai': trang_thai,
            'giaSan': gia_san
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

@app.route('/nhanvien')
def quan_ly_nhan_vien():
    danh_sach_nhan_vien = nhanvien_bus.lay_danh_sach_nhan_vien()
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

@app.route('/them-nhan-vien', methods=['POST'])
def them_nhan_vien():
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
    du_lieu_tai_khoan = {'TenTaiKhoan': ten_tai_khoan, 'MatKhau': mat_khau, 'NgayTao': ngay_tao, 'AccType': acc_type}
    result_taikhoan = taikhoan.them_tknv(du_lieu_tai_khoan)
    id_tai_khoan = taikhoan.get_max_id_taikhoan()
    du_lieu_nhan_vien = {
        'HoTen': ho_ten, 'NgaySinh': ngay_sinh, 'SDT': sdt, 'DiaChi': dia_chi, 'IdTaiKhoan': id_tai_khoan,
        'cccd': cccd, 'gioitinh': gioitinh, 'chuc_vu': chuc_vu, 'vi_tri': vi_tri, 'ngayvaolam': ngay_vao_lam,
        'hopdong': hop_dong, 'hoatdong': hoat_dong, 'mota': mo_ta, 'luong': luong, 'phucap': phu_cap if phu_cap else 0,
        'nganhang': ngan_hang if ngan_hang else ''
    }
    result_nhanvien = nhanvien_bus.them_nhan_vien(du_lieu_nhan_vien)
    print(f"Kết quả thêm nhân viên từ BUS: {result_nhanvien}")
    if result_nhanvien.get('success'):
        print("Thêm nhân viên thành công!")
        danh_sach_nhan_vien = nhanvien_bus.lay_danh_sach_nhan_vien()
    else:
        print(f"Thêm nhân viên thất bại: {result_nhanvien.get('error', 'Không có thông tin lỗi')}")
        taikhoan.xoaTaiKhoan(id_tai_khoan)
    return redirect(url_for('quan_ly_nhan_vien'))

@app.route('/xoa-nhan-vien/<int:id_nhan_vien>')
def xoa_nhan_vien(id_nhan_vien):
    nhanvien_bus.xoa_nhan_vien(id_nhan_vien)
    return redirect(url_for('quan_ly_nhan_vien'))

@app.route('/sua-nhan-vien/<int:id>', methods=['POST'])
def sua_nhan_vien(id):
    ho_ten = request.form.get('hoTen')
    ngay_sinh = request.form.get('ngaySinh')
    sdt = request.form.get('sdt')
    dia_chi = request.form.get('diaChi')
    id_tai_khoan = request.form.get('idTaiKhoan')
    du_lieu_moi = {'hoTen': ho_ten, 'ngaySinh': ngay_sinh, 'sdt': sdt, 'diaChi': dia_chi, 'idTaiKhoan': id_tai_khoan}
    ket_qua = nhanvien_bus.sua_nhan_vien(id, du_lieu_moi)
    return jsonify(ket_qua)

# Người dùng
def get_asset_path():
    return os.path.join(current_app.root_path, 'static', 'asset')

@app.route('/user/<userID>')
def nguoidung(userID: int):
    PhieuGhiBUS.danhSachPhieuGhi = phieughi.getListByDate(datetime.now().date())
    danh_sach_san = san_bus.lay_danh_sach_san()
    for san in danh_sach_san:
        if isinstance(san, dict):
            hinh_anh = san.get('HinhAnh', 'default.jpg')
            if 'asset/' in hinh_anh:
                san['HinhAnh'] = url_for('static', filename=hinh_anh)
            else:
                san['HinhAnh'] = url_for('static', filename=f'asset/{hinh_anh}')
    return render_template('user.html', userID=userID, san=danh_sach_san)

@app.route('/user/<int:userID>/render-date/<date>', methods=['POST'])
def renderBooking(userID: int, date):
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()
    PhieuGhiBUS.danhSachPhieuGhi = phieughi.getListByDate(date_obj)
    print(PhieuGhiBUS.danhSachPhieuGhi, flush=True)
    return jsonify(PhieuGhiBUS.danhSachPhieuGhi)

@app.route('/user/<int:userID>/dat_san/<int:sanID>/ngay/<date>/khung_gio/<khung_gio>/gia/<gia>', methods=['POST'])
def datsan(userID: int, sanID: int, date, khung_gio, gia):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        data = request.get_json()
        order = {
            'Ngay': date_obj,
            'TongTien': float(gia),
            'PhuongThuc': data.get('PhuongThuc'),
            'TrangThai': data.get('TrangThai', 'Chờ xác nhận'),
            'IdNhanVien': data.get('IdNhanVien'),
            'IdNguoiDung': userID
        }
        result = hoa_don_bus.them_hoa_don(order)
        if result.get('success'):
            return jsonify({'success': True, 'message': 'Đặt sân thành công', 'IdHoaDon': result.get('IdHoaDon')})
        else:
            return jsonify({'success': False, 'message': result.get('error', 'Lỗi không xác định')})
    except Exception as e:
        print(f"Lỗi khi xử lý đặt sân: {e}", flush=True)
        return jsonify({'success': False, 'message': str(e)})

# Đăng nhập & Đăng ký
@app.route('/login')
def dangNhap():
    return render_template('dangnhap_dangki.html')

def render_index_template(context=None):
    default_context = {
        'pg': [], 'san': [], 'today_date': datetime.now().strftime("%Y-%m-%d"),
        'today_revenue': 0, 'booked_fields': 0, 'total_fields': 0
    }
    if context:
        default_context.update(context)
    return render_template('index.html', **default_context)

@app.route('/processing', methods=['POST'])
def xuLiDangNhap():
    print(request.form.to_dict(), flush=True)
    result = taikhoan.dangNhapTaiKhoan(request.form.to_dict())
    if result.get('success'):
        if result.get('AccType') == "user":
            return redirect(url_for('nguoidung', userID=result.get('IdTaiKhoan')))
        else:
            return render_index_template()
    else:
        return redirect('/login')

@app.route('/signUp', methods=['POST'])
def xuliDangKi():
    birth = request.form.to_dict()['date']
    date_obj = datetime.strptime(birth, '%Y-%m-%d').date()
    adjDatas = request.form.to_dict()
    adjDatas['date'] = date_obj
    return taikhoan.dangKiTaiKhoan(adjDatas)

# Hóa đơn
@app.route('/hoa-don')
def quan_ly_hoa_don():
    danh_sach_hoa_don = hoa_don_bus.lay_danh_sach_hoa_don()
    return render_template('hoadon.html', danh_sach_hoa_don=danh_sach_hoa_don)

@app.route('/them-hoa-don', methods=['POST'])
def them_hoa_don():
    data = request.get_json()
    ngay = data.get('Ngay')
    tong_tien = data.get('TongTien')
    id_nhan_vien = data.get('IdNhanVien')
    du_lieu_hoa_don = {'Ngay': ngay, 'TongTien': tong_tien, 'IdNhanVien': id_nhan_vien}
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
    du_lieu_moi = {'Ngay': ngay, 'TongTien': tong_tien, 'IdNhanVien': id_nhan_vien}
    ket_qua = hoa_don_bus.sua_hoa_don(id, du_lieu_moi)
    if ket_qua:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'Không thể sửa hóa đơn'})

# Quản lý khách hàng
@app.route('/khachhang')
def quanlikhachhang():
    return render_template('quanlikhachhang.html')

@app.route('/khachhang/xoa_id/<int:IdNguoiDung>', methods=['POST'])
def xoa_khachhang(IdNguoiDung: int):
    result = khachhang.xoaNguoiDung(IdNguoiDung)
    return jsonify(result)

@app.route('/khachhang/timkiem/<key>', methods=['POST'])
def tim_khachhang(key: str):
    listGuest = khachhang.timKhachHang(key)
    today = datetime.today().date()
    data = {"list": listGuest, 'data':{'total':len(listGuest),
                                       'month':len(taikhoan.getListByDate(today - timedelta(days=30),'user')),
                                       'week':len(taikhoan.getListByDate(today - timedelta(days=7),'user')),
                                       'return':len(phieughi.getReturn())/len(listGuest)}}
    for x in listGuest:
        x['SoLuong'] = len(hoa_don_bus.lay_danh_sach_hoa_don(x['IdNguoiDung']))
        x['TongTien'] = khachhang.getTongTien(x['IdNguoiDung'])
    return jsonify(listGuest)

@app.route('/khachhang/load', methods=['POST'])
def load_khachhang():
    listGuest = khachhang.timKhachHang("")
    today = datetime.today().date()
    data = {"list": listGuest, 'data':{'total':len(listGuest),
                                       'month':len(taikhoan.getListByDate(today - timedelta(days=30),'user')),
                                       'week':len(taikhoan.getListByDate(today - timedelta(days=7),'user')),
                                       'return':len(phieughi.getReturn())/len(listGuest)}}
    for x in listGuest:
        x['SoLuong'] = len(hoa_don_bus.lay_danh_sach_hoa_don(x['IdNguoiDung']))
        x['TongTien'] = khachhang.getTongTien(x['IdNguoiDung'])
        x['TrangThai'] = khachhang.getTrangThai(x['IdNguoiDung'])
    print("HI")
    print(listGuest,flush=True)
    return jsonify(listGuest)

# Báo cáo & Thống kê
@app.route("/baocao")
def baocao():
    from collections import defaultdict
    import datetime
    hd = hoa_don_bus.lay_danh_sach_hoa_don() or []
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
@app.route('/quanlitaichinh')
def quanlitaichinh():
    return render_template('quanlitaichinh.html')

@app.route('/quanlitaichinh/timkiem/<key>', methods=['POST'])
def tim_taichinh(key:str):
    print(key + ".",flush=True)
    listHD = hoa_don_bus.timkiemHD(key)
    print(listHD,flush=True)
    return jsonify(listHD)

@app.route('/quanlitaichinh/load/', methods=['POST'])
def load_taichinh():
    listHD = hoa_don_bus.timkiemHD("")
    income:Dict = hoa_don_bus.getMonthlyIncome()
    tabs = hoa_don_bus.getTabs()
    total = 0
    for x in income.values():
        total += x
    tabs['total'] = total
    data = {"list": listHD,"income":income,"fees":tabs}
    return jsonify(data)

@app.route('/quanlitaichinh/edit/<int:IDHD>/<Status>', methods=['POST'])
def editState(IDHD: int, Status):
    result = hoa_don_bus.editState(IDHD, Status)
    return jsonify(result)

# Phiếu ghi
@app.route('/them-phieu-ghi')
def themphieughi():
    result = PhieuGhiBUS.themPhieuGhi()
    return jsonify({'success': True, 'result': result})

# Trang mở đầu
@app.route('/')
def index():
    danh_sach_san = san_bus.lay_danh_sach_san()
    for san in danh_sach_san:
        if isinstance(san, dict):
            hinh_anh = san.get('HinhAnh', 'default.jpg')
            if 'asset/' in hinh_anh:
                san['HinhAnh'] = url_for('static', filename=hinh_anh)
            else:
                san['HinhAnh'] = url_for('static', filename=f'asset/{hinh_anh}')
    return render_template('user.html', san=danh_sach_san)

@app.route('/index')
def pagemain():
    try:
        danh_sach_san = san_bus.lay_danh_sach_san() or []
        print("Danh sách sân trong /index:", danh_sach_san)
        for san in danh_sach_san:
            print("Sân:", san)
            hinh_anh = san.get('HinhAnh', 'default.jpg')
            if 'asset/' in hinh_anh:
                san['HinhAnh'] = url_for('static', filename=hinh_anh)
            else:
                san['HinhAnh'] = url_for('static', filename=f'asset/{hinh_anh}')
        ds_pg = phieughi.getListByDate(datetime.now().date()) or []
        print("Danh sách phiếu ghi:", ds_pg)
        booked_fields = len([pg for pg in ds_pg if pg.get('TrangThai', '').lower() == 'dat'])
        return render_template('index.html',
                               san=danh_sach_san,
                               pg=ds_pg,
                               today_date=datetime.now().strftime("%Y-%m-%d"),
                               today_revenue=0,
                               booked_fields=booked_fields,
                               total_fields=len(danh_sach_san) if danh_sach_san else 0)
    except Exception as e:
        print("Lỗi trong route /index:", str(e))
        return "Có lỗi xảy ra: " + str(e), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)