import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from db_config import get_connection
from mysql.connector import Error  
from typing import List, Dict, Optional
from datetime import datetime, timedelta    

class ThanhToanDAO:
    def __init__(self, conn=None):
        self.conn = conn if conn is not None else get_connection()

    def getListThanhToan(self, idNguoiDung: int = None) -> List[Dict]:
        try:
            cursor = self.conn.cursor(dictionary=True)
            if idNguoiDung:
                cursor.execute("SELECT * FROM thanhtoan WHERE idNguoiDung = %s", (idNguoiDung,))
            else:
                cursor.execute("SELECT * FROM thanhtoan")
            return cursor.fetchall()
        except Error as e:
            print(f"[DAO ERROR] Lỗi khi lấy danh sách: {e}")
            return []
        finally:
            cursor.close()
        
    def addThanhToan(self, data: Dict) -> Dict:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """INSERT INTO thanhtoan (idNguoiDung, NgayLap, TongTien, PhuongThuc, TrangThai) 
                    VALUES (%s, %s, %s, %s, %s)
                """,
                (data['idNguoiDung'], data['NgayLap'], data['TongTien'], data['PhuongThuc'], data['TrangThai'])
            )
            self.conn.commit()
            return {"success": True, "idThanhToan": cursor.lastrowid}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi thêm thanh toán: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()
            
    def updateThanhToan(self, data: Dict) -> Dict:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """UPDATE thanhtoan 
                    SET  Ngay = %s, TongTien = %s, PhuongThuc = %s, TrangThai = %s, IdNguoiDung = %s 
                    WHERE idThanhToan = %s
                """,
                (data['Ngay'],
                 data['TongTien'],
                 data['PhuongThuc'],
                 data['TrangThai'],
                 data['IdNguoiDung'],
                 data['IdThanhToan'],)
            )
            self.conn.commit()
            return {"success": True}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi cập nhật thanh toán: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()
            
    def deleteThanhToan(self, idThanhToan: int) -> Dict:
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM thanhtoan WHERE idThanhToan = %s", (idThanhToan,))
            self.conn.commit()
            return {"success": True}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi xóa thanh toán: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()