from db_config import get_connection
from typing import List, Dict
from mysql.connector import Error
class PhieuGhiDAO:
    def __init__(self, conn=None):
        if conn is None:
            self.conn = get_connection()
        else:
            self.conn = conn

    def getListPhieuGhi(self, idNguoiDung:int = None) -> List[Dict]:
        try:
            cursor = self.conn.cursor(dictionary=True)
            if idNguoiDung:
                cursor.execute("SELECT * FROM phieughi WHERE IdNguoiDung = %s", (idNguoiDung,))
            else:
                cursor.execute("SELECT * FROM phieughi")
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error: {e}")
            return []

    def xoaPhieuGhi(self, idPhieuGhi: int) -> Dict:
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("DELETE FROM phieughi WHERE IdPhieuGhi = %s", (idPhieuGhi,))
            self.conn.commit()
            return {"success": True}
        except Error as e:
            print(f"Error: {e}")
            return {"success": False, "message": str(e)}    
        
    def updatePhieuGhi(self, Datas: Dict) -> Dict:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "UPDATE phieughi SET IdSan=%s, IdNguoiDung=%s, Ngay=%s, KhungGio=%s WHERE IdPhieuGhi = %s",
                (Datas['IdSan'], Datas['IdNguoiDung'], Datas['Ngay'], Datas['KhungGio'], Datas['IdPhieuGhi'])
            )
            self.conn.commit()
            return {"success": cursor.rowcount > 0}
        except Error as e:
            self.conn.rollback()
            print(f"Error: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()
            
    def themPhieuGhi(self, Datas: Dict) -> Dict:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO phieughi (IdSan, IdNguoiDung, Ngay, KhungGio) VALUES (%s, %s, %s, %s)",
                (Datas['IdSan'], Datas['IdNguoiDung'], Datas['Ngay'], Datas['KhungGio'])
            )
            self.conn.commit()
            return {"success": cursor.rowcount > 0}
        except Error as e:
            self.conn.rollback()
            print(f"Error: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()