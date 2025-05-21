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
            # print(x,flush=True)
            if x['TrangThai'] == "Đã thanh toán":
                sum+= x['TongTien'] 
        return sum
    
    def getTrangThai(self, UID:int) -> str:
        result = self.taiKhoanBUS.getAcc(UID)
        if result['success']:
            return result['AccType']
    
    def timKhachHang(self, key:str, type:str = None) -> List[Dict]:
        return self.nguoidungDAO.search(key, type)
    
    def suaNguoiDung(self, data:Dict) -> Dict:
        oldData = self.timKhachHang(data['IdNguoiDung'])
        oldData = oldData[0]
        print("Check old data",flush=True)
        print(oldData,flush=True)
        flag = 0
        sets = ['SDT','Email','TenTaiKhoan']
        case={
            'SDT':'Số điện thoại đã tồn tại',
            'Email':'Email đã tồn tại',
            'TenTaiKhoan':'Tên tài khoản đã tồn tại'
        }
        
        for x in sets:
            if data[x] != oldData[x]:
                flag += 1
                
        if flag > 0 and flag < 3:
            result = self.nguoidungDAO.checkValidation(data,ignore= data['IdNguoiDung'])
            if result['amount'] > 1:
                for x in sets:
                    if data[x] == result[x]:
                        return {'success':False,'message':case[x]}
        elif flag == 3:
            result = self.nguoidungDAO.checkValidation(data)
            if result is not None:
                for x in sets:
                    if data[x] == result[x]:
                        return {'success':False,'message':case[x]}
                    
        result = self.taiKhoanBUS.updateAcc(data)
        print(result,flush=True)
        if result['success']:
            result = self.nguoidungDAO.sua_NguoiDung(data)
            print(result,flush=True)
        return result
    
    def getNguoiDungById(self, idNguoiDung: int) -> Dict:
        """
        Lấy thông tin người dùng dựa trên IdNguoiDung.
        Trả về dictionary chứa thông tin người dùng hoặc None nếu không tìm thấy.
        """
        result = self.nguoidungDAO.timKiemNguoiDung(idNguoiDung)
        if result and isinstance(result, dict) and 'IdNguoiDung' in result:
            return result
        return None
    
    def themNguoiDung(self, data:Dict) -> Dict:
        data['AccType'] = 'user'
        # print("Check input data",flush=True)
        # print(data,flush=True)
        result = self.nguoidungDAO.checkValidation(data)
        # print("Check validation result",flush=True)
        # print(result,flush=True)
        if result is None:
            result = self.taiKhoanBUS.addND(data)
            print(result,flush=True)
            if result['success']:    
                data['IdTaiKhoan'] = result['idTaiKhoan']
                result = self.nguoidungDAO.add(data)
                print(result,flush=True)
            return result
        else:
            sets = ['SDT','Email','TenTaiKhoan']
            for x in sets:
                if data[x] == result[x]:
                    case={
                        'SDT':'Số điện thoại đã tồn tại',
                        'Email':'Email đã tồn tại',
                        'TenTaiKhoan':'Tên tài khoản đã tồn tại'
                    }
                    return {'success':False,'message':case[x]}