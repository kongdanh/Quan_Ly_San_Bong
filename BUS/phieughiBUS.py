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
            # Xử lý trường hợp date là None
            if date is None:
                list_from_dao = self.phieuGhiDAO.getListByDate(None) or []
            else:
                list_from_dao = self.phieuGhiDAO.getListByDate(date)

            # Kiểm tra nếu list_from_dao là None hoặc không phải danh sách
            if not list_from_dao or not isinstance(list_from_dao, list):
                list_from_dao = []

            print("list_from_dao:", list_from_dao)  # Debug dữ liệu từ DAO

            new_list = [dict(item) for item in self.danhSachKhungGio]  # Tạo bản sao để tránh thay đổi trực tiếp
            for y in new_list:
                y['list'] = []
                for x in list_from_dao:
                    if x.get('KhungGio') == y['KhungGio']:  # Sử dụng get để tránh KeyError
                        y['list'].append(x.get('IdSan', None))
            print("new_list:", new_list)  # Debug dữ liệu trả về
            return new_list
        except ValueError as e:
            print(f"[BUS ERROR] Lỗi khi chuyển đổi định dạng ngày: {e}")
            return []
        except Exception as e:
            print(f"[BUS ERROR] Lỗi không xác định: {e}")
            return []
        
    def getReturn(self):
        return self.phieuGhiDAO.getReturn()