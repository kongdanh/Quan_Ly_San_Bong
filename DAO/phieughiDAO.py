from DAO.db_config import get_connection
from typing import List, Dict
from mysql.connector import Error
from datetime import datetime, timedelta, time

class PhieuGhiDAO:
    def __init__(self, conn=None):
        if conn is None:
            self.conn = get_connection()
        else:
            self.conn = conn

    def getListPhieuGhi(self, idNguoiDung: int = None) -> List[Dict]:
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
            cursor.execute("UPDATE phieughi SET status = 0 WHERE IdPhieuGhi = %s", (idPhieuGhi,))
            self.conn.commit()
            return {"success": True}
        except Error as e:
            print(f"Error: {e}")
            return {"success": False, "message": str(e)}    
        
    def updatePhieuGhi(self, Datas: Dict) -> Dict:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "UPDATE phieughi SET IdSan=%s, IdHoaDon=%s, Ngay=%s, KhungGio=%s WHERE IdPhieuGhi = %s",
                (Datas['IdSan'], Datas['IdHoaDon'], Datas['Ngay'], Datas['KhungGio'], Datas['IdPhieuGhi'])
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
        print(Datas, flush=True)
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO phieughi (IdSan, IdHoaDon, Ngay, KhungGio, GiaTien) VALUES (%s, %s, %s, %s, %s)",
                (Datas['IdSan'], Datas['IdHoaDon'], Datas['Ngay'], Datas['KhungGio'], Datas['GiaTien'])
            )
            self.conn.commit()
            return {"success": cursor.rowcount > 0}
        except Error as e:
            self.conn.rollback()
            print(f"Error: {e}")
            return {"success": False, "message": str(e)}
        finally:
            cursor.close()
            
    def getListByDate(self, date: datetime) -> List[Dict]:
        try:
            cursor = self.conn.cursor(dictionary=True)
            start_of_day = datetime.combine(date, time.min)
            end_of_day = datetime.combine(date, time.max)
            query = """
                SELECT p.IdPhieuGhi, p.IdSan, p.IdNguoiDung, p.Ngay, p.KhungGio, COALESCE(p.GiaTien, 0) AS Gia, p.TrangThai
                FROM phieughi p
                WHERE p.Ngay >= %s AND p.Ngay <= %s
            """
            cursor.execute(query, (start_of_day, end_of_day))
            result = cursor.fetchall()
            print(f"DEBUG: Kết quả truy vấn get_by_date = {result}")
            return result
        except Error as e:
            print(f"[DAO ERROR] Lỗi khi lấy phiếu ghi theo ngày: {e}")
            return []
        finally:
            cursor.close()
            
    def getReturn(self) -> List[Dict]:
        result = []
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("""SELECT 
                                IdNguoiDung,
                                COUNT(*) AS Tong,
                                SUM(TongTien) AS TongTien
                            FROM 
                                hoadon
                            WHERE 
                                Ngay >= %s
                            GROUP BY 
                                IdNguoiDung;""",(datetime.today().date()-timedelta(days=30),))
            result = cursor.fetchall()
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            return result