from datetime import datetime
from flask import Flask, jsonify, render_template, request, redirect, url_for
from BUS.san_bus import SanBus
from DAO.san_dao import SanDAO
from BUS.taikhoanBUS import TaiKhoanBUS
from DAO.db_config import get_connection
from BUS.nhanvien_bus import NhanVienBus
from DAO.nhanvien_dao import NhanVienDAO
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


# trang mở đầu ====================================================================================
@app.route('/')
def index():
    return render_template('index.html')

# sân
# khi nhấn quản lý sân ( chức năng của quản lý or nhân viên) ======================================
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


# nhân viên
# tạo bus dao của nhân viên
nhanvien_dao = NhanVienDAO(conn)
nhanvien_bus = NhanVienBus(nhanvien_dao)

# khi nhấn quản lý nhân viên ( quyền của quản lý hoặc chủ sân ) ========================================
@app.route('/nhanvien')
def quan_ly_nhan_vien():
    # Lấy danh sách nhân viên
    danh_sach_nhan_vien = nhanvien_bus.lay_danh_sach_nhan_vien()
    # Truyền danh sách nhân viên vào template nhanvien.html
    return render_template('nhanvien.html', danh_sach_nhan_vien=danh_sach_nhan_vien)

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

# trang người dùng
@app.route('/user<userID>')
def nguoidung(userID):
    return render_template('user.html',userID=userID)

#thiết lập route cho login page
@app.route('/login')
def dangNhap():
    return render_template('dangnhap_dangki.html')

#đăng nhập
@app.route('/processing', methods=['POST'])
def xuLiDangNhap():
    name = request.form.get('username')
    pwd = request.form.get('password')
    print(request.form.to_dict())
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
        

if __name__ == '__main__':
    app.run(debug=True)
