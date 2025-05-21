from datetime import date
import mysql.connector
from mysql.connector import Error
from typing import List, Dict
from DAO.db_config import get_connection

class TaiKhoanDAO:
    def __init__(self,conn = None):
        self.conn = conn if conn is not None else get_connection()

    def getListTaiKhoan(self) -> List[Dict]:
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM taikhoan")
            return cursor.fetchall()
        except Error as e:
            print(f"[DAO ERROR] Lỗi khi lấy danh sách: {e}")
            return []

    def them_TaiKhoan(self, signUpData: Dict) -> Dict:
        result = {}
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """INSERT INTO taikhoan (TenTaiKhoan, MatKhau, NgayTao, AccType) 
                    VALUES (%s, %s, %s, %s)
                """,
                (signUpData['TenTaiKhoan'],signUpData['MatKhau'],signUpData['NgayTao'],signUpData['AccType'])
            )
            self.conn.commit()
            id_tai_khoan = cursor.lastrowid
            result =  {"success": True, "idTaiKhoan": cursor.lastrowid}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi thêm người dùng: {e}")
            result =  {"success": False, "message": str(e), "idTaiKhoan": id_tai_khoan}
        finally:
            cursor.close()
            return result

    def sua_TaiKhoan(self, accID: int, userData: Dict) -> Dict:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "UPDATE taikhoan SET TenTaiKhoan=%s, MatKhau=%s, NgayTao=%s, AccType=%s WHERE idTaiKhoan = %s",
                (userData.values()[0:],accID)
            )
            self.conn.commit()
            id_tai_khoan = cursor.lastrowid
            return {"success": True, "idTaiKhoan": id_tai_khoan}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi sửa người dùng: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()

    def xoa_TaiKhoan(self, accID: int) -> Dict:
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM taikhoan WHERE idTaiKhoan = %s", (accID,))
            self.conn.commit()
            return {"success": cursor.rowcount > 0}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi xóa người dùng: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()

    def dangNhapTaiKhoan(self,signInData:Dict)->Dict:
        try:
            cursor = self.conn.cursor()
            query = """
                SELECT * FROM taikhoan WHERE TenTaiKhoan=%s AND MatKhau=%s
            """
            values=(list(signInData.values())[0:])
            cursor.execute(query,values)
            data = cursor.fetchone()
            result={}
            if data:
                result = {"success": True,'IdTaiKhoan':data[0],'AccType':data[4]}
            else:
                result = {"success": False,"message":"tài khoản không tồn tại"}
            return result
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi đăng nhập tài khoản: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()
    
    def timKiemTaiKhoanByName(self,accName:str)->Dict:
        try:
            cursor = self.conn.cursor(dictionary=True)
            query = """
                SELECT * FROM taikhoan WHERE TenTaiKhoan=%s
            """
            values=(accName,)
            cursor.execute(query,values)
            data = cursor.fetchone()
            if data:
                data.update({'success':True})
                return data
            else:
                data = {"success": False,"message":"tài khoản không tồn tại"}
                return data
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi tìm tài khoản: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()
    
    def timKiemTaiKhoan(self,accID:int)->Dict:
        try:
            cursor = self.conn.cursor(dictionary=True)
            query = """
                SELECT * FROM taikhoan WHERE IdTaiKhoan=%s
            """
            values=(accID,)
            cursor.execute(query,values)
            data = cursor.fetchone()
            if data:
                data.update({'success':True})
                return data
            else:
                data = {"success": False,"message":"tài khoản không tồn tại"}
                return data
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi tìm tài khoản: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()
    
    def __del__(self):
        """Đóng kết nối khi hủy (nếu tồn tại)"""
        if hasattr(self, 'conn') and self.conn is not None and self.conn.is_connected():
            try:
                self.conn.close()
                print("Kết nối database đã được đóng.")
            except Error as e:
                print(f"Lỗi khi đóng kết nối: {e}")
                
    def getListByDate(self, date: date, type:str = None) -> List[Dict]:
        try:
            self.conn.commit()
            cursor = self.conn.cursor(dictionary=True)
            if type is not None:
                cursor.execute("SELECT * FROM taikhoan WHERE NgayTao >= %s AND AccType = %s", (date, type))
            else:
                cursor.execute("SELECT * FROM taikhoan WHERE NgayTao >= %s", (date,))
            return cursor.fetchall()
        except Error as e:
            print(f"[DAO ERROR] Lỗi khi lấy danh sách theo ngày: {e}")
            return []
        
    def get_max_id_taikhoan(self) -> int:
        """Lấy giá trị idTaiKhoan lớn nhất từ bảng taikhoan"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT MAX(IdTaiKhoan) FROM taikhoan")
            max_id = cursor.fetchone()[0]
            return int(max_id) if max_id is not None else 0
        except Exception as e:
            raise Exception(f"Lỗi khi lấy ID lớn nhất: {str(e)}")
        
    def getAcc(self, ID:int) -> Dict:
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM TaiKhoan Where IdTaiKhoan = %s",(ID,))
            data = cursor.fetchone()
            if data:
                data.update({'success':True})
                return data
            else:
                data = {"success": False,"message":"tài khoản không tồn tại"}
                return data
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi tìm tài khoản: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()
            
    def update(self, userData: Dict) -> Dict:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "UPDATE taikhoan SET TenTaiKhoan=%s, MatKhau=%s WHERE IdTaiKhoan = %s",
                (userData['TenTaiKhoan'], userData['MatKhau'], userData['IdTaiKhoan'])
            )
            self.conn.commit()
            id_tai_khoan = cursor.lastrowid
            return {"success": True, "idTaiKhoan": id_tai_khoan}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi sửa người dùng: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()
            
    def status(self, userData: Dict) -> Dict:
        result = {}
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "UPDATE taikhoan SET AccType = %s WHERE IdTaiKhoan = %s",
                (userData['AccType'], 
                 userData['IdTaiKhoan'])
            )
            self.conn.commit()
            result = {"success": cursor.rowcount}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi sửa tài khoản: {e}")
            result = {"success": False, "message": str(e)}
        finally:
            cursor.close()
            return result