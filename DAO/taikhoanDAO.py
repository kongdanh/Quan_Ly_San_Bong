import mysql.connector
from mysql.connector import Error
from typing import List, Dict
from DAO.db_config import get_connection

class TaiKhoanDAO:
    def __init__(self, conn=None):
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
        for x in signUpData.values():
            if not x:
                return {"success": False, "error": "Thiếu thông tin bắt buộc"}

        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """INSERT INTO taikhoan (TenTaiKhoan, MatKhau, NgayTao, AccType) 
                    VALUES (%s, %s, %s, %s)
                """,
                (signUpData.values()[0:])
            )
            
            self.conn.commit()
            return {"success": True, "idTaiKhoan": cursor.lastrowid}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi thêm người dùng: {e}")
            return {"success": False, "error": str(e)}
        finally:
            cursor.close()

    def sua_TaiKhoan(self, accID: int, userData: Dict) -> Dict:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "UPDATE taikhoan SET TenTaiKhoan=%s, MatKhau=%s, NgayTao=%s, AccType=%s WHERE idTaiKhoan = %s",
                (userData.values()[0:],accID)
            )
            self.conn.commit()
            return {"success": cursor.rowcount > 0}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi sửa người dùng: {e}")
            return {"success": False, "error": str(e)}
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
            return {"success": False, "error": str(e)}
        finally:
            cursor.close()

    def dangNhapTaiKhoan(self,signInData:Dict)->Dict:
        try:
            cursor = self.conn.cursor()
            query = """
                SELECT * FROM taikhoan WHERE TenTaiKhoan=%s AND MatKhau=%s
            """
            values=(signInData.values()[0:])
            cursor.execute(query,values)
            self.conn.commit()
            data = cursor.fetchone()
            return {"success": True if data else False}.update(data if data else {"error":"tài khoản không đúng mật khẩu"})
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi tìm người dùng: {e}")
            return {"success": False, "error": str(e)}
        finally:
            cursor.close()
    
    def timKiemTaiKhoan(self,accName:str)->Dict:
        try:
            cursor = self.conn.cursor()
            query = """
                SELECT * FROM taikhoan WHERE TenTaiKhoan=%s
            """
            values=(accName,)
            cursor.execute(query,values)
            self.conn.commit()
            data = cursor.fetchone()
            return {"success": True if data else False}.update(data if data else {"error":"tài khoản không tồn tại"})
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi tìm người dùng: {e}")
            return {"success": False, "error": str(e)}
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