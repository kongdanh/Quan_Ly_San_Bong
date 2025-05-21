from typing import Dict, List
from DAO.san_dao import SanDAO  # Import DAO layer

class SanBus:
    def __init__(self, dao=None):
        """Khởi tạo Bus với DAO tùy chọn"""
        self.dao = dao if dao is not None else SanDAO()  # Truyền instance của SanDAO vào Bus
        self.danh_sach_san = []  # Khởi tạo danh sách nội bộ (tùy chọn)

    def them_san(self, san_data: Dict) -> Dict:
        """Thêm sân mới qua DAO"""
        required_fields = ['coSan', 'diaChi']
        for field in required_fields:
            if not san_data.get(field):
                return {"success": False, "error": f"Thiếu thông tin bắt buộc: {field}"}

        # Đảm bảo các thuộc tính khác có giá trị mặc định nếu không được cung cấp
        san_data_full = {
            'coSan': san_data.get('coSan', '5'),  # Sửa 'CoSan' thành 'coSan' để khớp với main.py
            'diaChi': san_data.get('diaChi', 'Chưa có thông tin'),
            'hinhAnh': san_data.get('hinhAnh', 'default.jpg'),
            'giaSan': san_data.get('giaSan', 0),
            'soSan': san_data.get('soSan', 1),  # Sửa 'sanSo' thành 'soSan' để khớp với main.py
            'moTa': san_data.get('moTa', 'Chưa có mô tả'),
            'trangThai': san_data.get('trangThai', 1)
        }

        print(f"[SanBus] Sending to DAO: {san_data_full}")  # Debug
        # Gọi hàm trong DAO để thêm vào database
        result = self.dao.them_san(san_data_full)
        return result

    def lay_danh_sach_san(self) -> List[Dict]:
        """Lấy danh sách sân từ DAO"""
        danh_sach = self.dao.lay_danh_sach_san()
        # Cập nhật danh sách nội bộ (tùy chọn)
        self.danh_sach_san = danh_sach
        print(f"[SanBus] Retrieved from DAO: {danh_sach}")  # Debug
        return danh_sach

    def them_san_to_list(self, san_data: Dict) -> bool:
        """Thêm sân vào danh sách nội bộ (tùy chọn)"""
        if not hasattr(self, 'danh_sach_san'):
            self.danh_sach_san = []
        
        required_fields = ['coSan', 'diaChi']
        for field in required_fields:
            if not san_data.get(field):
                print(f"[BUS ERROR] Thiếu thông tin bắt buộc trong danh sách nội bộ: {field}")
                return False

        new_id = max((san.get('IdSan', 0) for san in self.danh_sach_san), default=0) + 1
        self.danh_sach_san.append({
            "IdSan": new_id,
            "CoSan": san_data.get('coSan', '5'),
            "DiaChi": san_data.get('diaChi', 'Chưa có thông tin'),
            "HinhAnh": san_data.get('hinhAnh', 'default.jpg'),
            "GiaSan": san_data.get('giaSan', 0),
            "SoSan": san_data.get('soSan', 1),  # Sửa 'sanSo' thành 'soSan'
            "MoTa": san_data.get('moTa', 'Chưa có mô tả'),
            "TrangThai": san_data.get('trangThai', 1)
        })
        return True

    def xoa_san(self, id_san: int) -> Dict:
        """Xóa sân qua DAO"""
        result = self.dao.xoa_san(id_san)
        # Cập nhật danh sách nội bộ (tùy chọn)
        if result.get('success'):
            self.danh_sach_san = [san for san in self.danh_sach_san if san.get('IdSan') != id_san]
        return result
    
    def sua_san(self, id_san: int, san_data: Dict) -> Dict:
        """Gọi DAO để sửa thông tin sân"""
        required_fields = ['coSan', 'diaChi']
        for field in required_fields:
            if not san_data.get(field):
                return {"success": False, "error": f"Thiếu thông tin để cập nhật: {field}"}

        # Đảm bảo các thuộc tính khác có giá trị mặc định nếu không được cung cấp
        san_data_full = {
            'coSan': san_data.get('coSan', '5'),
            'diaChi': san_data.get('diaChi', 'Chưa có thông tin'),
            'hinhAnh': san_data.get('hinhAnh', 'default.jpg'),
            'giaSan': san_data.get('giaSan', 0),
            'soSan': san_data.get('soSan', 1),
            'moTa': san_data.get('moTa', 'Chưa có mô tả'),
            'trangThai': san_data.get('trangThai', 1)
        }

        try:
            print(f"[SanBus] Sending to DAO for update: {san_data_full}")  # Debug
            result = self.dao.sua_san(id_san, san_data_full)
            # Cập nhật danh sách nội bộ (tùy chọn)
            if result.get('success'):
                for san in self.danh_sach_san:
                    if san.get('IdSan') == id_san:
                        san.update(san_data_full)
                        # Đổi key để khớp với HTML/JavaScript
                        san['IdSan'] = id_san
                        san['CoSan'] = san_data_full['coSan']
                        san['DiaChi'] = san_data_full['diaChi']
                        san['HinhAnh'] = san_data_full['hinhAnh']
                        san['GiaSan'] = san_data_full['giaSan']
                        san['SoSan'] = san_data_full['soSan']
                        san['MoTa'] = san_data_full['moTa']
                        san['TrangThai'] = san_data_full['trangThai']
                        break
            return result
        except Exception as e:
            print(f"[BUS ERROR] Lỗi khi gọi DAO sửa sân: {e}")
            return {"success": False, "error": str(e)}