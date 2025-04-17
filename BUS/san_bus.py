from typing import Dict
from DAO.san_dao import SanDAO  # Import DAO layer

class SanBus:
    def __init__(self, dao):
        self.dao = dao  # Truyền instance của SanDAO vào Bus
        # Nếu muốn giữ danh sách nội bộ, khởi tạo nó
        self.danh_sach_san = []  # Khởi tạo danh sách (tùy chọn)

    def them_san(self, san_data: Dict) -> Dict:
        """Thêm sân mới qua DAO"""
        if not san_data.get('coSan') or not san_data.get('diaChi'):
            return {"success": False, "error": "Thiếu thông tin bắt buộc"}

        # Gọi hàm trong DAO để thêm vào database
        result = self.dao.them_san(san_data)
        return result

    def lay_danh_sach_san(self):
        return self.dao.lay_danh_sach_san()

    # Nếu muốn giữ logic danh sách nội bộ, thêm như một phương thức khác
    def them_san_to_list(self, san_data):
        if not hasattr(self, 'danh_sach_san'):
            self.danh_sach_san = []
        new_id = max((san.get('idSan', 0) for san in self.danh_sach_san), default=0) + 1
        self.danh_sach_san.append({
            "idSan": new_id,
            "coSan": san_data["coSan"],
            "diaChi": san_data["diaChi"]
        })
        return True

    def xoa_san(self, id_san):
        """Xóa sân qua DAO"""
        return self.dao.xoa_san(id_san)
    
    def sua_san(self, id_san: int, san_data: Dict) -> Dict:
        """Gọi DAO để sửa thông tin sân"""
        if not san_data.get('coSan') or not san_data.get('diaChi'):
            return {"success": False, "error": "Thiếu thông tin để cập nhật"}

        try:
            result = self.dao.sua_san(id_san, san_data)
            return result
        except Exception as e:
            print(f"[BUS ERROR] Lỗi khi gọi DAO sửa sân: {e}")
            return {"success": False, "error": str(e)}


# Không khởi tạo trực tiếp san_bus ở đây, để main.py xử lý