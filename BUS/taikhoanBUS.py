from typing import Dict
from DAO import taikhoanDAO,nguoidungDAO

class taikhoanBUS:
    def __init__(self):
        self.userDao = nguoidungDAO()
        self.accDao = taikhoanDAO()
        
    def taoTaiKhoanND(self,signUpData:Dict) -> Dict:
        # dictionary sẽ có 4 dữ liệu đầu là data tài khoản các dữ liệu sau nó là thông tin người dùng
        for x in signUpData.values():
            if not x:
                return {"success": False, "error": "Thiếu thông tin bắt buộc"}
        result = [] 
        result.append(self.accDao.them_TaiKhoan(dict(list(signUpData.items())[:4])))
        if not result[0].get("success"):
            return result
        result.append(self.userDao.them_NguoiDung(dict(list(signUpData.items())[4:])))
        if not result[1].get("success"):
            result.append(self.accDao.xoa_TaiKhoan(result.get("idTaiKhoan")))
        return result[len(result)-1]
    
    def taoTaiKhoanNV(self,signUpData:Dict) -> Dict:
        # dictionary sẽ có 4 dữ liệu đầu là data tài khoản các dữ liệu sau nó là thông tin người dùng
        for x in signUpData.values():
            if not x:
                return {"success": False, "error": "Thiếu thông tin bắt buộc"}
        result = [] 
        result.append(self.accDao.timTaiKhoan(signUpData.values()[0]))
        if not result[0].get("success"):
            return result
        result.append(self.accDao.them_TaiKhoan(dict(list(signUpData.items())[:4])))
        if not result[0].get("success"):
            return result
        result.append(self.userDao.them_NguoiDung(dict(list(signUpData.items())[4:])))
        if not result[1].get("success"):
            result.append(self.accDao.xoa_TaiKhoan(result.get("idTaiKhoan")))
        return result[len(result)-1]
    
    def danhSachTaiKhoan(self):
        return self.accDao.getListTaiKhoan()
    
    def dangNhapTaiKhoan(self,signInData:Dict)->Dict:
        #dictionary đưa vào chỉ có 2 values là tên và mật khẩu
        result = self.accDao.timTaiKhoan(signInData.values()[0])
        if result.get("success"):
            return self.accDao.dangNhapTaiKhoan(signInData)
        return result
