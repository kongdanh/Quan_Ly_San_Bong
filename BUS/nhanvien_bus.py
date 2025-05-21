from typing import Dict, List
from DAO.nhanvien_dao import NhanVienDAO
from BUS.taikhoanBUS import TaiKhoanBUS  # Giả sử bạn đã có TaiKhoanBUS

class NhanVienBus:
    def __init__(self):
        self.dao = NhanVienDAO()
        self.taikhoanBUS = TaiKhoanBUS()  # Khởi tạo TaiKhoanBUS
        self.danh_sach_nhan_vien = []

    def them_nhan_vien(self, nhan_vien_data: Dict) -> Dict:
        required_fields = [
            'HoTen', 'NgaySinh', 'SDT', 'DiaChi', 'IdTaiKhoan', 'luong', 'chuc_vu', 'vi_tri',
            'ngayvaolam', 'hopdong', 'cccd', 'gioitinh', 'hoatdong'
        ]
        missing_fields = [field for field in required_fields if not nhan_vien_data.get(field)]
        if missing_fields:
            print(f"Thiếu trường bắt buộc trong nhân viên: {missing_fields}")
            return {"success": False, "error": f"Thiếu thông tin bắt buộc: {', '.join(missing_fields)}"}
        print("bus", nhan_vien_data)
        result = self.dao.them_nhan_vien(nhan_vien_data)
        print(f"Kết quả từ DAO (nhanvien): {result}")
        
        if result.get("success") and "insert_id" in result:
            return {"success": True, "idNhanVien": result["insert_id"]}
        else:
            return {"success": False, "error": result.get("error", "Lỗi không xác định khi thêm nhân viên")}

    def lay_danh_sach_nhan_vien(self) -> List[Dict]:
        danh_sach = self.dao.lay_danh_sach_nhan_vien()
        # Lấy thông tin tài khoản cho từng nhân viên
        for nv in danh_sach:
            tai_khoan = self.taikhoanBUS.getAcc(nv.get('IdTaiKhoan', 0))
            if tai_khoan and tai_khoan.get('success', False):
                nv['ten_tai_khoan'] = tai_khoan.get('TenTaiKhoan', '')
                nv['mat_khau'] = tai_khoan.get('MatKhau', '')
                nv['ngay_tao'] = tai_khoan.get('NgayTao', '')
                nv['nhom_quyen'] = tai_khoan.get('AccType', '')
            else:
                nv['ten_tai_khoan'] = ''
                nv['mat_khau'] = ''
                nv['ngay_tao'] = ''
                nv['nhom_quyen'] = ''
        return danh_sach

    def xoa_nhan_vien(self, id_nhan_vien: int) -> Dict:
        # Xóa tài khoản liên quan nếu cần
        nhan_vien = self.dao.lay_nhan_vien_theo_id(id_nhan_vien)
        if nhan_vien and nhan_vien.get('IdTaiKhoan'):
            self.taikhoanBUS.xoaTaiKhoan(nhan_vien['IdTaiKhoan'])
        return self.dao.xoa_nhan_vien(id_nhan_vien)

    def sua_nhan_vien(self, id_nhan_vien: int, nhan_vien_data: Dict) -> Dict:
        required_fields = [
            'HoTen', 'NgaySinh', 'SDT', 'DiaChi', 'IdTaiKhoan', 'luong', 'chuc_vu', 'vi_tri',
            'ngayvaolam', 'hopdong', 'cccd', 'gioitinh', 'hoatdong'
        ]
        missing_fields = [field for field in required_fields if not nhan_vien_data.get(field)]
        if missing_fields:
            print(f"Thiếu trường bắt buộc khi sửa nhân viên: {missing_fields}")
            return {"success": False, "error": f"Thiếu thông tin bắt buộc: {', '.join(missing_fields)}"}

        try:
            # Cập nhật thông tin tài khoản nếu có
            if nhan_vien_data.get('ten_tai_khoan') and nhan_vien_data.get('mat_khau'):
                tai_khoan_data = [{
                    'IdTaiKhoan': nhan_vien_data['IdTaiKhoan'],
                    'TenTaiKhoan': nhan_vien_data['ten_tai_khoan'],
                    'MatKhau': nhan_vien_data['mat_khau'],
                    'AccType': nhan_vien_data.get('nhom_quyen', 'Nhân viên'),
                    'NgayTao': nhan_vien_data.get('ngay_tao', '')
                }]
                self.taikhoanBUS.updateAcc2(tai_khoan_data)

            return self.dao.sua_nhan_vien(id_nhan_vien, nhan_vien_data)
        except Exception as e:
            print(f"[BUS ERROR] Lỗi khi gọi DAO sửa nhân viên: {e}")
            return {"success": False, "error": str(e)}
