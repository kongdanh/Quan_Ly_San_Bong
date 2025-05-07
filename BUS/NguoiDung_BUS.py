from DAO.nguoidungDAO import NguoiDungDAO
from BUS.taikhoanBUS import TaiKhoanBUS
from BUS.phieughiBUS import PhieuGhiBUS
from BUS.hoadon_bus import HoaDonBUS
from typing import List, Dict

class NguoiDung_BUS:
    list: List[Dict] = []
    def __init__(self,conn=None):
        self.nguoidungDAO = NguoiDungDAO()
        self.taiKhoanBUS = TaiKhoanBUS()
        self.hoaDonBUS = HoaDonBUS()
        self.phieuGhiBUS = PhieuGhiBUS()
        
        
    def getListNguoiDung(self) -> List[Dict]:
        return self.nguoidungDAO.getListNguoiDung()
    
    def xoaNguoiDung(self, idNguoiDung: int) -> Dict:
        result = self.nguoidungDAO.timKiemNguoiDung(idNguoiDung)
        accID = result['IdTaiKhoan']
        ListHD = self.hoaDonBUS.lay_danh_sach_hoa_don(idNguoiDung)
        for x in ListHD:
            x['IdNguoiDung'] = None
            result = self.hoaDonBUS.updateHD(x)
            if not result['success']:
                return result
        if result['success']:
            result = self.nguoidungDAO.xoa_NguoiDung(idNguoiDung)
        if result['success']:
            return self.taiKhoanBUS.xoaTaiKhoan(accID)
        return result
    
    def getTongTien(self, idNguoiDung:int) -> int:
        list = self.hoaDonBUS.lay_danh_sach_hoa_don(idNguoiDung)
        sum = 0
        for x in list:
            print(x,flush=True)
            if x['TrangThai'] == "Đã thanh toán":
                sum+= x['TongTien'] 
        return sum
    
    def getTrangThai(self, UID:int) -> str:
        result = self.taiKhoanBUS.getAcc(UID)
        if result['success']:
            return result['AccType']
    
    def timKhachHang(self, key:str) -> List[Dict]:
        return self.nguoidungDAO.search(key)