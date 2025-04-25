from typing import Dict
from DAO.nhanvien_dao import NhanVienDAO  # Import lớp DAO tương ứng

class NhanVienBus:
    def __init__(self):
        self.dao = NhanVienDAO()
        self.danh_sach_nhan_vien = []  # Tùy chọn, nếu muốn giữ bản sao nội bộ

    def them_nhan_vien(self, nhan_vien_data: Dict) -> Dict:
        """Thêm nhân viên mới thông qua DAO"""
        required_fields = [
            'HoTen', 'NgaySinh', 'SDT', 'DiaChi', 'IdTaiKhoan', 'luong', 'chuc_vu', 'vi_tri',
            'ngayvaolam', 'mota', 'hopdong', 'phucap', 'cccd', 'gioitinh', 'nganhang', 'hoatdong'
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

    def lay_danh_sach_nhan_vien(self):
        danh_sach = self.dao.lay_danh_sach_nhan_vien()
        return danh_sach

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
