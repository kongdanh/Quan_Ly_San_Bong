from typing import Dict
from DAO.nhanvien_dao import NhanVienDAO  # Import lớp DAO tương ứng

class NhanVienBus:
    def __init__(self, dao: NhanVienDAO):
        self.dao = dao
        self.danh_sach_nhan_vien = []  # Tùy chọn, nếu muốn giữ bản sao nội bộ

    def them_nhan_vien(self, nhan_vien_data: Dict) -> Dict:
        """Thêm nhân viên mới thông qua DAO"""
        if not nhan_vien_data.get('HoTen') or not nhan_vien_data.get('SDT'):
            return {"success": False, "error": "Thiếu thông tin bắt buộc"}
        return self.dao.them_nhan_vien(nhan_vien_data)

    def lay_danh_sach_nhan_vien(self):
        danh_sach = self.dao.lay_danh_sach_nhan_vien()
        print("Danh sách nhân viên từ DAO:", danh_sach)  # Debug
        return danh_sach

    def them_nhan_vien_to_list(self, nhan_vien_data):
        if not hasattr(self, 'danh_sach_nhan_vien'):
            self.danh_sach_nhan_vien = []
        new_id = max((nv.get('IdNhanVien', 0) for nv in self.danh_sach_nhan_vien), default=0) + 1
        self.danh_sach_nhan_vien.append({
            "IdNhanVien": new_id,
            "HoTen": nhan_vien_data["HoTen"],
            "NgaySinh": nhan_vien_data["NgaySinh"],
            "SDT": nhan_vien_data["SDT"],
            "DiaChi": nhan_vien_data["DiaChi"],
            "IdTaiKhoan": nhan_vien_data["IdTaiKhoan"]
        })
        return True

    def xoa_nhan_vien(self, id_nhan_vien):
        """Xóa nhân viên thông qua DAO"""
        return self.dao.xoa_nhan_vien(id_nhan_vien)

    def sua_nhan_vien(self, id_nhan_vien: int, nhan_vien_data: Dict) -> Dict:
        """Sửa thông tin nhân viên qua DAO"""
        if not nhan_vien_data.get('HoTen') or not nhan_vien_data.get('SDT'):
            return {"success": False, "error": "Thiếu thông tin để cập nhật"}

        try:
            return self.dao.sua_nhan_vien(id_nhan_vien, nhan_vien_data)
        except Exception as e:
            print(f"[BUS ERROR] Lỗi khi gọi DAO sửa nhân viên: {e}")
            return {"success": False, "error": str(e)}
