from datetime import datetime
from typing import Dict, List
from DAO.hoadon_dao import HoaDonDAO

class HoaDonBUS:
    def __init__(self, dao: HoaDonDAO = None):
        self.dao = dao if dao else HoaDonDAO()
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
    
    def lay_danh_sach_hoa_don(self, UID:int = None):
        danh_sach = self.dao.lay_danh_sach_hoa_don(UID)
        # print("danh sach hd vua lay: ", danh_sach,flush=True)
        return danh_sach
    
    def updateHD(self, data:Dict):
        return self.dao.update(data)
    
    def timkiemHD(self, key:str) -> List[Dict]:
        return self.dao.timkiemHD(key)
    
    def editState(self, IdHoaDon:int, State:str)->Dict:
        return self.dao.editState(IdHoaDon, State)
    
    def addHD(self, Data:Dict)->Dict:
        return self.dao.add(Data)
    
    def getMonthlyIncome(self)->List[Dict]:
        date = datetime.today().date()
        data = {}
        for x in range(1,13):
            data[x] = self.dao.getMonthly(x)
        return data
    
    def getMonthIncome(self, month:int)-> float:
        return self.dao.getMonthly(month)
    
    def getTabs(self)->List[Dict]:
        data = {}
        date = datetime.today().date()
        data['curr'] = self.getMonthIncome(date.month) 
        data['prev'] = self.getMonthIncome(date.month - 1)
        data['rate'] = str(((data['curr'] / data['prev']) - 1 )* 100) + "%" if data['prev'] != 0 else 'Chưa xác định'
        return data