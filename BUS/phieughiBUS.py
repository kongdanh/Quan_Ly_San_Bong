from DAO.phieughiDAO import PhieuGhiDAO
from typing import List, Dict
from datetime import datetime
from mysql.connector import Error

class PhieuGhiBUS:
    danhSachPhieuGhi: List[Dict] = []
    danhSachKhungGio = [{'KhungGio': "8:00 - 10:00", 'list': []},
                        {'KhungGio': "10:00 - 12:00", 'list': []},
                        {'KhungGio': "14:00 -16:00", 'list': []},
                        {'KhungGio': "16:00 - 18:00", 'list': []},
                        {'KhungGio': "18:00 - 20:00", 'list': []}]

    def __init__(self, conn=None):
        self.phieuGhiDAO = PhieuGhiDAO(conn)

    def getListPhieuGhi(self, idNguoiDung: int = None) -> List[Dict]:
        return self.phieuGhiDAO.getListPhieuGhi(idNguoiDung)

    def xoaPhieuGhi(self, idPhieuGhi: int) -> Dict:
        return self.phieuGhiDAO.xoaPhieuGhi(idPhieuGhi)

    def updatePhieuGhi(self, Datas: Dict) -> Dict:
        return self.phieuGhiDAO.updatePhieuGhi(Datas)

    def themPhieuGhi(self, Datas: Dict) -> Dict:
        return self.phieuGhiDAO.themPhieuGhi(Datas)
    
    def getListByDate(self, date: datetime) -> List[Dict]:
        try:
            print(f"DEBUG: Gọi getListByDate với date = {date}")
            result = self.phieuGhiDAO.getListByDate(date)  # Sửa: Gọi phương thức từ DAO
            print(f"DEBUG: Kết quả từ DAO.get_by_date = {result}")
            if not isinstance(result, list):
                print(f"Cảnh báo: get_by_date trả về {type(result)}, chuyển thành []")
                return []
            for item in result:
                item.setdefault('IdPhieuGhi', 0)
                item.setdefault('IdSan', 0)
                item.setdefault('IdNguoiDung', 0)
                item.setdefault('Ngay', date.strftime("%Y-%m-%d"))
                item.setdefault('KhungGio', '')
                item.setdefault('Gia', 0)
                item.setdefault('TrangThai', 'Chưa xác định')
                try:
                    item['Gia'] = float(item.get('Gia', 0) or 0)
                except (TypeError, ValueError):
                    print(f"Cảnh báo: Gia không hợp lệ cho IdPhieuGhi {item.get('IdPhieuGhi')}: {item.get('Gia')}")
                    item['Gia'] = 0
            return result
        except Exception as e:
            print(f"Lỗi trong getListByDate: {e}")
            return []
        
    def getReturn(self):
        return self.phieuGhiDAO.getReturn()