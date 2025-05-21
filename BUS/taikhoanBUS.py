from datetime import date
from typing import Dict, List
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
    
    def them_tknv(self, datanv: Dict) -> Dict:
        """Thêm tài khoản nhân viên mới thông qua DAO"""
        # Danh sách các trường bắt buộc
        required_fields = ['TenTaiKhoan', 'MatKhau', 'NgayTao', 'AccType']
        
        # Kiểm tra các trường bắt buộc
        missing_fields = [field for field in required_fields if not datanv.get(field)]
        if missing_fields:
            return {"success": False, "error": f"Thiếu thông tin bắt buộc: {', '.join(missing_fields)}"}

        # Gọi DAO để thêm tài khoản 
        result = self.accDao.them_TaiKhoan(datanv)
        
        # Kiểm tra kết quả từ DAO
        if result.get("success") and "insert_id" in result:
            try:
                # Ép kiểu insert_id thành int để đảm bảo idTaiKhoan là số nguyên
                id_tai_khoan = int(result["insert_id"])
                return {
                    "success": True,
                    "idTaiKhoan": id_tai_khoan
                }
            except (ValueError, TypeError):
                return {
                    "success": False,
                    "error": "ID tài khoản không hợp lệ, không phải số nguyên"
                }
        else:
            return {
                "success": False,
                "error": result.get("error", "Lỗi không xác định khi thêm tài khoản nhân viên")
            }
            
    def get_max_id_taikhoan(self) -> int:
        try:
            max_id = self.accDao.get_max_id_taikhoan()
            return int(max_id) if max_id is not None else 0
        except Exception as e:
            raise Exception(f"Lỗi khi lấy ID lớn nhất: {str(e)}")
        
    def getAcc(self, ID:int )-> Dict:
        return self.accDao.getAcc(ID)
    
    def updateAcc(self,Data:Dict)-> Dict:
        return self.accDao.update(Data)
    
    def addND(self, data:Dict) -> Dict:
        return self.accDao.them_TaiKhoan(data)
    
    def status(self,data:Dict) -> Dict:
        return self.accDao.status(data)