from DAO.nguoidungDAO import NguoiDungDAO
from BUS.taikhoanBUS import TaiKhoanBUS
from BUS.ThanhToanBUS import ThanhToanBUS
from BUS.phieughiBUS import PhieuGhiBUS
from typing import List, Dict

class NguoiDung_BUS:
    list: List[Dict] = []
    def __init__(self,conn=None):
        self.nguoidungDAO = NguoiDungDAO()
        self.taiKhoanBUS = TaiKhoanBUS()
        self.thanhToanBUS = ThanhToanBUS()
        self.phieuGhiBUS = PhieuGhiBUS()
        
        
    def getListNguoiDung(self) -> List[Dict]:
        return self.nguoidungDAO.getListNguoiDung()
    
    def xoaNguoiDung(self, idNguoiDung: int) -> Dict:
        result = self.nguoidungDAO.timKiemNguoiDung(idNguoiDung)
        accID = result['IdTaiKhoan']
        ListPhieuGhi = self.phieuGhiBUS.getListPhieuGhi(idNguoiDung)
        ListThanhToan = self.thanhToanBUS.getListThanhToan(idNguoiDung)
        for x in ListPhieuGhi:
            x['IdNguoiDung'] = None
            result = self.phieuGhiBUS.updatePhieuGhi(x)
            if not result['success']:
                return result
        for x in ListThanhToan:
            x['IdNguoiDung'] = None
            result = self.thanhToanBUS.updateThanhToan(x)
            if not result['success']:
                return result
        if result['success']:
            result = self.nguoidungDAO.xoa_NguoiDung(idNguoiDung)
        if result['success']:
            return self.taiKhoanBUS.xoaTaiKhoan(accID)
        return result
    
    def getTongTien(self, idNguoiDung:int) -> int:
        list = self.thanhToanBUS.getListThanhToan(idNguoiDung)
        sum = 0
        for x in list:
            if x['TrangThai'] == "Da thanh toan":
                sum+= x['TongTien'] 
        return sum
    
