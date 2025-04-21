from typing import Dict
from DAO.hoadon_dao import HoaDonDAO

class HoaDonBUS:
    def __init__(self, dao: HoaDonDAO):
        self.dao = dao
        # mang luu tru ds hd
        self.danh_sach_hoa_don = []
        
    def them_hoa_don(self, hd_data: Dict) -> Dict:
        if not hd_data.get('IdHoaDon') or not hd_data.get('IdNhanVien'):
            return {"success": False, "error": "Thiếu thông tin bắt buộc"}
        return self.dao.them_hoa_don(hd_data)
    
    def sua_hoa_don(self, id_hoa_don: int, hd_data: Dict) -> Dict:
        if not hd_data.get('IdHoaDon') or not hd_data.get('IdNhanVien'):
            return {"success": False, "error": "Thiếu thông tin để cập nhật"}

        try:
            return self.dao.sua_hoa_don(id_hoa_don, hd_data)
        except Exception as e:
            print(f"[BUS ERROR] Lỗi khi gọi DAO sửa hoa don: {e}")
            return {"success": False, "error": str(e)}
    
    def xoa_hoa_don(self, id_hoa_don):
        return self.dao.xoa_hoa_don(id_hoa_don)
    
    def lay_danh_sach_hoa_don(self):
        danh_sach = self.dao.lay_danh_sach_hoa_don()
        print("danh sach hd vua lay: ", danh_sach)
        return danh_sach
    