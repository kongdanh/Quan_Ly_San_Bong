from db_config import get_connection
from typing import List, Dict
from mysql.connector import Error

class ChiTietThanhToanDAO:
    def __init__(self,conn=None):
        self.conn = conn if conn is not None else get_connection()
    def getListChiTietThanhToan(self,idThanhToan=None) -> List[Dict]:
        try:
            cursor = self.conn.cursor(dictionary=True)
            if idThanhToan:
                cursor.execute("SELECT * FROM chitietthanhtoan WHERE idThanhToan = %s", (idThanhToan,))
            else:
                cursor.execute("SELECT * FROM chitietthanhtoan")
            return cursor.fetchall()
        except Error as e:
            print(f"[DAO ERROR] Lỗi khi lấy danh sách: {e}")
            return []
        finally:
            cursor.close()
        
    def addChiTietThanhToan(self, data: Dict) -> Dict:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """INSERT INTO chitietthanhtoan (idThanhToan, idPhieuGhi, NgayThue, KhungGioTheu, TongTien) 
                    VALUES (%s, %s, %s, %s)
                """,
                (data['idThanhToan'], data['idPhieuGhi'], data['NgayThue'], data['KhungGioThue'], data['TongTien'])
            )
            self.conn.commit()
            return {"success": True, "idChiTiet": cursor.lastrowid}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi thêm chi tiết thanh toán: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()
            
    def updateChiTietThanhToan(self, data: Dict) -> Dict:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """UPDATE chitietthanhtoan 
                    SET  NgayThue = %s, KhungGioThue = %s, TongTien = %s 
                    WHERE idPhieuGhi = %s AND idThanhToan = %s
                """,
                (data['NgayThue'],
                 data['KhungGioThue'],
                 data['TongTien'],
                 data['idThanhToan'],
                 data['idPhieuGhi'],)
            )
            self.conn.commit()
            return {"success": True}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi cập nhật chi tiết thanh toán: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()
            
    def deleteChiTietThanhToan(self, idPhieuGhi: int, idThanhToan:int) -> Dict:
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM chitietthanhtoan WHERE idPhieuGhi = %s AND idThanhToan", (idPhieuGhi,idThanhToan))
            self.conn.commit()
            return {"success": True}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi xóa chi tiết thanh toán: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()