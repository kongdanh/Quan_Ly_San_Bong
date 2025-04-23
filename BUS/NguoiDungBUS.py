from DAO.nguoidungDAO import NguoiDungDAO
from BUS.taikhoanBUS import TaiKhoanBUS
from BUS.ThanhToanBUS import ThanhToanBUS
from typing import List, Dict

class NguoiDungBUS:
    list: List[Dict] = []
    def __init__(self,conn=None):
        self.nguoidungDAO = NguoiDungDAO()
        self.taiKhoanBUS = TaiKhoanBUS()
        self.thanhToanBUS = ThanhToanBUS()
        
    def getListNguoiDung(self) -> List[Dict]:
        return self.nguoidungDAO.getListNguoiDung()
    
    def xoaNguoiDung(self, idNguoiDung: int) -> Dict:
        result = self.nguoidungDAO.timKiemNguoiDung(idNguoiDung)
        if result['success']:
            result = self.taiKhoanBUS.xoaTaiKhoan(result['IdTaiKhoan'])
        if result['success']:
            return self.nguoidungDAO.xoa_NguoiDung(idNguoiDung)
        return result
    
    def getTongTien(self, idNguoiDung:int) -> int:
        list = self.thanhToanBUS.getListThanhToan(idNguoiDung)
        sum = 0
        for x in list:
            if x['TrangThai'] == "Da thanh toan":
                sum+= x['TongTien'] 
        return sum
    
    