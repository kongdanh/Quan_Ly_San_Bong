import mysql.connector
from mysql.connector import Error
from typing import List, Dict
from DAO.db_config import get_connection

class NguoiDungDAO:
    def __init__(self, conn=None):
        """Khởi tạo DAO với kết nối database tùy chọn"""
        self.conn = conn if conn is not None else get_connection()

    def getListNguoiDung(self) -> List[Dict]:
        """Lấy toàn bộ danh sách sân (phù hợp với bus)"""
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM nguoidung")
            return cursor.fetchall()
        except Error as e:
            print(f"[DAO ERROR] Lỗi khi lấy danh sách: {e}")
            return []

    def them_nguoiDung(self, signUpData: Dict) -> Dict:
        for x in signUpData.values():
            if not x:
                return {"success": False, "message": "Thiếu thông tin bắt buộc"}
        values = list(signUpData.values())    
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """INSERT INTO nguoidung (HoTen, SDT, NgaySinh, Email, IdTaiKhoan) 
                    VALUES (%s, %s, %s, %s, %s)
                """,    
                (values[0:])
            )
            
            self.conn.commit()
            return {"success": True, "idNguoiDung": cursor.lastrowid}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi thêm người dùng: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()

    def sua_NguoiDung(self, userData: Dict) -> Dict:
        print(userData,flush=True)
        """Sửa thông tin người dùng (phù hợp với bus)"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "UPDATE nguoidung SET HoTen=%s, NgaySinh=%s, SDT=%s, Email=%s WHERE IdNguoiDung = %s",
                (userData['HoTen'],
                 userData['NgaySinh'],
                 userData['SDT'],
                 userData['Email'],
                 userData['IdNguoiDung'])
            )
            self.conn.commit()
            return {"success": True}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi sửa người dùng: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()

    def xoa_NguoiDung(self, userID: int) -> Dict:
        """Xóa người dùng (phù hợp với bus)"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE nguoidung SET status = 0 WHERE IdNguoiDung = %s", (userID,))
            self.conn.commit()
            return {"success": cursor.rowcount > 0}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi xóa người dùng: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()

    def timKiemNguoiDungByPhone(self, phone: int) -> Dict:
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM nguoidung WHERE SDT = %s", (phone,))
            data = cursor.fetchone()
            if( data is None):
                return {"success": False,"message":"Không có người dùng tồn tại"}
            return {"success": True,'idNguoiDung':cursor.lastrowid}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi tìm người dùng: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()
    
    def timKiemNguoiDung(self, userID:int) -> Dict:
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM nguoidung WHERE IdNguoiDung = %s", (userID,))
            data = cursor.fetchone()
            if( data is None):
                return {"success": False,"message":"Không có người dùng tồn tại"}
            data['success'] = True
            return data
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi tìm người dùng: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()
    
    def __del__(self):
        if hasattr(self, 'conn') and self.conn is not None and self.conn.is_connected():
            try:
                self.conn.close()
                print("Kết nối database đã được đóng.")
            except Error as e:
                print(f"Lỗi khi đóng kết nối: {e}")
                
    def search(self, key:str, type:str = None) -> List[Dict]:
        
        result = []
        if type is None or type == "all":
            type = ""
        type =  "%" + type + "%"
        print(key,flush=True)
        print(type,flush=True)    
        try:
            cursor = self.conn.cursor(dictionary=True)
            try:
                self.conn.commit()
                key = int(key)
                cursor.execute("SELECT * FROM nguoidung LEFT JOIN Taikhoan On nguoidung.idTaiKhoan = Taikhoan.idTaiKhoan WHERE ( IdNguoiDung = %s OR SDT = %s ) AND AccType LIKE %s",
                               (key, key, type))
            except ValueError as e:
                key = "%" + key + "%"
                cursor.execute("SELECT * FROM nguoidung LEFT JOIN Taikhoan On nguoidung.idTaiKhoan = Taikhoan.idTaiKhoan WHERE ( HoTen Like %s OR Email Like %s ) AND AccType LIKE %s",
                               (key, key, type))
            result = cursor.fetchall()
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi tìm người dùng: {e}")
        finally:
            cursor.close()
            return result
            
            
    def add(self, data: Dict) -> Dict:  
        result = {}
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """INSERT INTO nguoidung (HoTen, SDT, NgaySinh, Email, IdTaiKhoan) 
                    VALUES (%s, %s, %s, %s, %s)
                """,    
                (data['HoTen'],
                 data['SDT'],
                 data['NgaySinh'],
                 data['Email'],
                 data['IdTaiKhoan'])
            )
            self.conn.commit()
            result = {"success": True, "idNguoiDung": cursor.lastrowid}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi thêm người dùng: {e}")
            result = {"success": False, "message": str(e)}
        finally:
            cursor.close()
            return result
        
        
    def checkValidation(self, data:Dict, ignore:int = None) -> Dict:
        result = []
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("""SELECT * FROM nguoidung LEFT JOIN Taikhoan On nguoidung.idTaiKhoan = Taikhoan.idTaiKhoan WHERE 
                                Email = %s OR 
                                SDT = %s OR
                                TenTaiKhoan = %s""", 
                                (data["Email"],
                                 data["SDT"],
                                 data["TenTaiKhoan"]))
            result = cursor.fetchone()
            if result['IdNguoiDung'] == ignore:
                result = cursor.fetchone()
            cursor.fetchall()
            if result is not None:
                result['amount'] = cursor.rowcount
                result.update({"success": True,"message": "Người dùng đã tồn tại"})
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi tìm người dùng: {e}")
            result = {"success": False, "message": str(e)}
        finally:
            cursor.close()
            return result