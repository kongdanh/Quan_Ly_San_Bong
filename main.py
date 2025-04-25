from datetime import datetime, timedelta
from flask import Flask, jsonify, render_template, request, redirect, url_for
from BUS.san_bus import SanBus
from DAO.san_dao import SanDAO
from BUS.taikhoanBUS import TaiKhoanBUS
from DAO.db_config import get_connection
from BUS.nhanvien_bus import NhanVienBus
from DAO.nhanvien_dao import NhanVienDAO
from DAO.hoadon_dao import HoaDonDAO
from BUS.hoadon_bus import HoaDonBUS
from BUS.NguoiDungBUS import NguoiDungBUS
from BUS.ThanhToanBUS import ThanhToanBUS
from datetime import datetime
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Khởi tạo Flask app
app = Flask(__name__, template_folder='GUI')

# Khởi tạo connection, DAO và BUS trước khi định nghĩa route
conn = get_connection()
dao = SanDAO(conn)  # Truyền conn từ get_connection()
san_bus = SanBus(dao)
taikhoan = TaiKhoanBUS()
khachhang = NguoiDungBUS()
thanhtoan = ThanhToanBUS()
# trang mở đầu ====================================================================================
@app.route('/')
def index():
    return render_template('index.html')

# sân
# khi nhấn quản lý sân ( chức năng của quản lý or nhân viên) ======================================
# region sân
@app.route('/san')
def quan_ly_san():
    # Lấy danh sách sân
    danh_sach_san = san_bus.lay_danh_sach_san()
    # Truyền danh sách sân vào template san.html
    return render_template('san.html', danh_sach_san=danh_sach_san)

# route thêm sân
@app.route('/them-san', methods=['POST'])
def them_san():
    # lấy thông tin sân từ from thêm sân
    co_san = request.form.get('coSan')
    dia_chi = request.form.get('diaChi')
    # gọi bus
    result = san_bus.them_san({'coSan': co_san, 'diaChi': dia_chi})
    if isinstance(result, dict) and 'idSan' in result:
        danh_sach_san = san_bus.lay_danh_sach_san()
        print(f"Danh sách sân sau khi thêm: {danh_sach_san}")
    else :
        print(f"Thêm sân thất bại, result: {result}")
    return redirect(url_for('quan_ly_san'))

# route xóa sân ( sử dụng id san ) ==================================================================
@app.route('/xoa-san/<int:id_san>')
def xoa_san(id_san):
    # gọi bus
    san_bus.xoa_san(id_san)
    return redirect(url_for('quan_ly_san'))

# sửa sân ( thông qua id lấy tại bảng sân )
@app.route('/sua-san/<int:id>', methods=['POST'])
def sua_san(id):
    # lấy dữ liệu mới từ from
    co_san = request.form.get('coSan')
    dia_chi = request.form.get('diaChi')
    du_lieu_moi = {
        'coSan': co_san,
        'diaChi': dia_chi
    }
    # gọi bus
    ket_qua = san_bus.sua_san(id, du_lieu_moi)
    return jsonify(ket_qua)

# endregion
###################################################################################
# region nhân viên
# nhân viên
# tạo bus dao của nhân viên
nhanvien_dao = NhanVienDAO(conn)
nhanvien_bus = NhanVienBus(nhanvien_dao)

# khi nhấn quản lý nhân viên ( quyền của quản lý hoặc chủ sân ) ========================================

@app.route('/nhanvien')
def quan_ly_nhan_vien():
    # Lấy danh sách nhân viên
    danh_sach_nhan_vien = nhanvien_bus.lay_danh_sach_nhan_vien()
    tong_nhan_vien = len(danh_sach_nhan_vien)
    so_luong_hd = sum(1 for nv in danh_sach_nhan_vien if isinstance(nv, dict) and nv.get('hoatdong') == 'Hoạt động')
    so_luong_np = sum(1 for nv in danh_sach_nhan_vien if isinstance(nv, dict) and nv.get('hoatdong') == 'Nghỉ phép')

    now = datetime.now()
    thang_hien_tai = now.month
    nam_hien_tai = now.year
    so_nv_moi = sum(
    1 for nv in danh_sach_nhan_vien
    if 'ngayvaolam' in nv
    and isinstance(nv['ngayvaolam'], str)
    and datetime.strptime(nv['ngayvaolam'], '%Y-%m-%d').month == thang_hien_tai
    and datetime.strptime(nv['ngayvaolam'], '%Y-%m-%d').year == nam_hien_tai
)
    # Truyền danh sách nhân viên vào template nhanvien.html
    return render_template('quanlinhanvien.html', danh_sach_nhan_vien=danh_sach_nhan_vien, soluongnv = tong_nhan_vien, slhd = so_luong_hd, nvm = so_nv_moi, nvnp = so_luong_np)

# route thêm nhân viên
@app.route('/them-nhan-vien', methods=['POST'])
def them_nhan_vien():
    # lấy thông tin từ from
    ho_ten = request.form.get('hoTen')
    ngay_sinh = request.form.get('ngaySinh')
    sdt = request.form.get('sdt')
    dia_chi = request.form.get('diaChi')
    id_tai_khoan = request.form.get('idTaiKhoan')
    
    # tạo Dict từ thông tin
    du_lieu_nhan_vien = {
        'hoTen': ho_ten,
        'ngaySinh': ngay_sinh,
        'sdt': sdt,
        'diaChi': dia_chi,
        'idTaiKhoan': id_tai_khoan
    }
    
    # gọi bus
    result = nhanvien_bus.them_nhan_vien(du_lieu_nhan_vien)
    if isinstance(result, dict) and 'idNhanVien' in result:  # Kiểm tra thêm thành công
        danh_sach_nhan_vien = nhanvien_bus.lay_danh_sach_nhan_vien()
        print(f"Danh sách nhân viên sau khi thêm: {danh_sach_nhan_vien}")
    else:
        print(f"Thêm nhân viên thất bại, result: {result}")
    
    return redirect(url_for('nhanvien.quan_ly_nhan_vien'))

# Route xóa nhân viên ( thông qua id nhân viên )
@app.route('/xoa-nhan-vien/<int:id_nhan_vien>')
def xoa_nhan_vien(id_nhan_vien):
    # gọi bus
    nhanvien_bus.xoa_nhan_vien(id_nhan_vien)
    return redirect(url_for('nhanvien.quan_ly_nhan_vien'))

# Route sửa thông tin nhân viên ( lấy id nhân viên tại bảng )
@app.route('/sua-nhan-vien/<int:id>', methods=['POST'])
def sua_nhan_vien(id):
    ho_ten = request.form.get('hoTen')
    ngay_sinh = request.form.get('ngaySinh')
    sdt = request.form.get('sdt')
    dia_chi = request.form.get('diaChi')
    id_tai_khoan = request.form.get('idTaiKhoan')
    
    # tạo Dict từ dữ liệu trên
    du_lieu_moi = {
        'hoTen': ho_ten,
        'ngaySinh': ngay_sinh,
        'sdt': sdt,
        'diaChi': dia_chi,
        'idTaiKhoan': id_tai_khoan
    }
    
    # gọi bus
    ket_qua = NhanVienBus.sua_nhan_vien(id, du_lieu_moi)
    return jsonify(ket_qua)
# endregion
###################################################################################
# region người dùng
# trang người dùng
@app.route('/user<userID>')
def nguoidung(userID):
    return render_template('user.html',userID=userID)

# endregion
############################################################################################
# region đăng nhập & đăng ký
#thiết lập route cho login page
@app.route('/login')
def dangNhap():
    return render_template('dangnhap_dangki.html')

#đăng nhập
@app.route('/processing', methods=['POST'])
def xuLiDangNhap():
    print(request.form.to_dict(),flush=True)
    result = taikhoan.dangNhapTaiKhoan(request.form.to_dict())
    if result.get('success'):
        # dẫn vào trang người dùng
        if result.get('AccType') == "user":
            return redirect(url_for('nguoidung',userID = result.get('IdTaiKhoan')))    
        # dẫn tới quản lí sân
        else:
            return redirect(url_for('index'))   
    else:
        return redirect('login')
        
@app.route('/signUp', methods=['POST'])
def xuliDangKi():
    birth = request.form.to_dict()['date']
    date_obj = datetime.strptime(birth, '%Y-%m-%d').date()
    adjDatas = request.form.to_dict()
    adjDatas['date'] = date_obj
    return taikhoan.dangKiTaiKhoan(adjDatas)
# endregion 
########################################################################################       
# region Hóa Đơn
# Khởi tạo DAO và BUS cho hóa đơn
hoa_don_dao = HoaDonDAO(conn)  # conn là kết nối database đã được thiết lập
hoa_don_bus = HoaDonBUS(hoa_don_dao)

# Route hiển thị danh sách hóa đơn
@app.route('/hoa-don')
def quan_ly_hoa_don():
    # Lấy danh sách hóa đơn
    danh_sach_hoa_don = hoa_don_bus.lay_danh_sach_hoa_don()
    # Truyền danh sách hóa đơn vào template hoa_don.html
    return render_template('hoadon.html', danh_sach_hoa_don=danh_sach_hoa_don)

# Route thêm hóa đơn
@app.route('/them-hoa-don', methods=['POST'])
def them_hoa_don():
    # Lấy thông tin hóa đơn từ request
    data = request.get_json()
    ngay = data.get('Ngay')
    tong_tien = data.get('TongTien')
    id_nhan_vien = data.get('IdNhanVien')

    # Tạo dict từ thông tin
    du_lieu_hoa_don = {
        'Ngay': ngay,
        'TongTien': tong_tien,
        'IdNhanVien': id_nhan_vien
    }

    # Gọi bus để thêm hóa đơn
    result = hoa_don_bus.them_hoa_don(du_lieu_hoa_don)
    if isinstance(result, dict) and 'IdHoaDon' in result:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': str(result)})

# Route xóa hóa đơn
@app.route('/xoa-hoa-don/<int:id_hoa_don>', methods=['POST'])
def xoa_hoa_don(id_hoa_don):
    # Gọi bus để xóa hóa đơn
    result = hoa_don_bus.xoa_hoa_don(id_hoa_don)
    if result:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'Không thể xóa hóa đơn'})

# Route sửa hóa đơn
@app.route('/sua-hoa-don/<int:id>', methods=['POST'])
def sua_hoa_don(id):
    # Lấy dữ liệu mới từ request
    data = request.get_json()
    ngay = data.get('Ngay')
    tong_tien = data.get('TongTien')
    id_nhan_vien = data.get('IdNhanVien')

    # Tạo dict từ dữ liệu mới
    du_lieu_moi = {
        'Ngay': ngay,
        'TongTien': tong_tien,
        'IdNhanVien': id_nhan_vien
    }

    # Gọi bus để sửa hóa đơn
    ket_qua = hoa_don_bus.sua_hoa_don(id, du_lieu_moi)
    if ket_qua:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'Không thể sửa hóa đơn'})
# endregion
########################################################################################
# region quản lí khách hàng
@app.route('/khachhang')
def quanlikhachhang():
    NguoiDungBUS.list = khachhang.getListNguoiDung()
    date = datetime.now().date()
    datas = {'Tong':len(NguoiDungBUS.list),
             'newByWeek': len(taikhoan.getListByDate(date - timedelta(days=7),'user')),
             'newByMonth': len(taikhoan.getListByDate(date - timedelta(days=30),'user')),
             'comeBack':30}
    for x in NguoiDungBUS.list:
        x['SoLuong'] = len(thanhtoan.getListThanhToan(x['IdNguoiDung']))
        x['TongTien'] = khachhang.getTongTien(x['IdNguoiDung'])
    return render_template('quanlikhachhang.html',danhsachkhachhang = NguoiDungBUS.list, data=datas)

@app.route('/khachhang/xoa_id/<int:IdNguoiDung>', methods=['POST'])
def xoa_khachhang(IdNguoiDung: int):
    print("HELLO", flush=True)
    result = khachhang.xoaNguoiDung(IdNguoiDung)
    print(result, flush=True)
    return jsonify(result)
# endregion
########################################################################################
# region báo cáo & thống kê
@app.route("/baocao")
def baocao():
    return render_template("baocao.html")
# endregion
########################################################################################
# region quản lý tài chính
@app.route('/quanlitaichinh')
def quanlitaichinh():
    return render_template('quanlitaichinh.html')
# endregion 
########################################################################################

if __name__ == '__main__':
    app.run(debug=True)

