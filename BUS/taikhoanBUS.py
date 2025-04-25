from datetime import date
from typing import Dict
from DAO.nguoidungDAO import NguoiDungDAO
from DAO.taikhoanDAO import TaiKhoanDAO

class TaiKhoanBUS:
    def __init__(self):
        self.userDao = NguoiDungDAO()
        self.accDao = TaiKhoanDAO()
        
    def taoTaiKhoanND(self,signUpData:Dict) -> Dict:
        # dictionary sẽ có 4 dữ liệu đầu là data tài khoản các dữ liệu sau nó là thông tin người dùng
        for x in signUpData.values():
            if not x:
                return {"success": False, "message": "Thiếu thông tin bắt buộc"}
        accDatas = dict(list(signUpData.items())[4:7])
        result = self.accDao.them_TaiKhoan(accDatas)
        if not result.get("success"):
            return result
        accid = result['idTaiKhoan']
        userDatas = dict(list(signUpData.items())[0:4])
        userDatas['idTaiKhoan'] = accid
        result = self.userDao.them_nguoiDung(userDatas)
        if not result.get("success"):
            result = self.accDao.xoa_TaiKhoan(accid)
        return result
    
    def danhSachTaiKhoan(self):
        return self.accDao.getListTaiKhoan()
    
    def dangNhapTaiKhoan(self,signInData:Dict)->Dict:
        #dictionary đưa vào chỉ có 2 values là tên và mật khẩu
        # ví dụ: {'username': 'user1', 'password': 'pass1'}
        result = self.accDao.timKiemTaiKhoanByName(signInData['username'])
        print(result,flush=True)
        if result.get("success"):
            return self.accDao.dangNhapTaiKhoan(signInData)
        return result
    
    def dangKiTaiKhoan(self,signUpData:Dict)->Dict:
        #dictionary đưa vào chỉ có 2 values là tên và mật khẩu
        # ví dụ: {'username': 'user1', 'password': 'pass1'}
        result = self.accDao.timKiemTaiKhoanByName(signUpData['username'])
        if result.get("success"):
            return {'success':False,'message':'Tên người dùng đã tồn tại'}
        result = self.userDao.timKiemNguoiDung(signUpData['phone'])
        if result.get("success"):
            return {'success':False,'message':'Số điện thoại này đã được sử dụng'}
        result = self.taoTaiKhoanND(signUpData)
        return result

    def xoaTaiKhoan(self, idTaiKhoan: int) -> Dict:
        return  self.accDao.xoa_TaiKhoan(idTaiKhoan)
    
    def getListByDate(self, date: date, type:str = None) -> Dict:
        return self.accDao.getListByDate(date,type)
    
    def timKiemTaiKhoan(self, idTaiKhoan: int) -> Dict:
        return self.accDao.timKiemTaiKhoan(idTaiKhoan)