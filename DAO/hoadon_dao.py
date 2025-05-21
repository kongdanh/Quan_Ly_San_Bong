from datetime import datetime
import mysql.connector
from mysql.connector import Error
from typing import List, Dict
from DAO.db_config import get_connection

class HoaDonDAO:
    def __init__(self, conn=None):
        self.conn = conn if conn is not None else get_connection()
        
    def lay_danh_sach_hoa_don(self,UID:int = None) -> List[Dict]:
        # lay ds tu dtb
        conn = get_connection()
        list = []
        try:
            cursor = conn.cursor(dictionary=True)
            if UID :
                cursor.execute("SELECT * FROM hoadon Where IdNguoiDung = %s",(UID,))
            else:
                cursor.execute("SELECT * FROM hoadon")
            list = cursor.fetchall()
        except Error as e:
            print(f"[DAO ERROR] lỗi khi lấy danh sách {e}")
        finally:
            conn.close()
            return list
    
    def them_hoa_don(self, hd_data: Dict) -> Dict:
        try:
            cursor = self.conn.cursor()
            query = """
            INSERT INTO hoadon (Ngay, TongTien, PhuongThuc, TrangThai, IdNhanVien, IdNguoiDung)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (
                hd_data['Ngay'],
                hd_data['TongTien'],
                hd_data['PhuongThuc'],
                hd_data['TrangThai'],
                hd_data.get('IdNhanVien'),
                hd_data['IdNguoiDung']
            )
            cursor.execute(query, values)
            self.conn.commit()
            cursor.close()
            return {'success': True}
        except Exception as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi thêm hóa đơn: {e}", flush=True)
            return {'success': False, 'error': str(e)}

    def editState(self, IdHoaDon: int, State: str) -> Dict:
        try:
            cursor = self.conn.cursor()
            query = """
            UPDATE hoadon 
            SET TrangThai = %s
            WHERE IdHoaDon = %s
            """
            cursor.execute(query, (State, IdHoaDon))
            self.conn.commit()
            cursor.close()
            return {'success': True}
        except Exception as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi cập nhật trạng thái hóa đơn: {e}", flush=True)
            return {'success': False, 'error': str(e)}
            
    def sua_hoa_don(self, id_hoa_don: int, hd_data:Dict) -> Dict:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                UPDATE hoadon
                SET Ngay = %s, TongTien = %s, IdNhanVien = %s
                WHERE IdHoaDon = %s
                """,
                (
                    hd_data['Ngay'],
                    hd_data['TongTien'],
                    hd_data['IdNhanVien'],
                    id_hoa_don
                )
            )
            self.conn.commit()
            return {"success": cursor.rowcount > 0}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi sửa hóa đơn: {e}")
            return {"success": False, "error": str(e)}
        finally:
            cursor.close()
            
    def xoa_hoa_don(self, id_hoa_don: int) -> Dict:
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM hoadon WHERE IdHoaDon = %s", (id_hoa_don,))
            self.conn.commit()
            return {"success": cursor.rowcount > 0}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi xóa hóa đơn: {e}")
            return {"success": False, "error": str(e)}
        finally:
            cursor.close()
                    
    def __del__(self):
        """Đóng kết nối khi đối tượng bị hủy"""
        if hasattr(self, 'conn') and self.conn is not None and self.conn.is_connected():
            try:
                self.conn.close()
                print("Kết nối database đã được đóng.")
            except Error as e:
                print(f"Lỗi khi đóng kết nối: {e}")
                
    def update(self,data: Dict):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                UPDATE hoadon
                SET Ngay = %s, TongTien = %s, PhuongThuc = %s, TrangThai = %s, IdNhanVien = %s, IdNguoiDung = %s
                WHERE IdHoaDon = %s
                """,
                (
                    data['Ngay'],
                    data['TongTien'],
                    data['PhuongThuc'],
                    data['TrangThai'],
                    data['IdNhanVien'],
                    data['IdNguoiDung'],
                    data['IdHoaDon']
                )
            )
            self.conn.commit()
            return {"success": cursor.rowcount > 0}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi sửa hóa đơn: {e}")
            return {"success": False, "error": str(e)}
        finally:
            cursor.close()
            
    def timkiemHD(self, key:str, type:str) -> List[Dict]:
        if type == "all":
            type = ""
        type = "%" + type + "%"
        try:
            cursor = self.conn.cursor(dictionary=True)
            try:
                key = int(key)
                sql="""SELECT * FROM HOADON LEFT JOIN NguoiDung ON HOADON.IdNguoiDung = NguoiDung.IdNguoiDung WHERE IdHoaDon = %s AND TrangThai LIKE %s ORDER BY Ngay DESC"""
                cursor.execute(sql,(key,type))
            except ValueError:
                if key == "":
                    sql = """SELECT * FROM HOADON LEFT JOIN NguoiDung ON HOADON.IdNguoiDung = NguoiDung.IdNguoiDung WHERE TrangThai LIKE %s ORDER BY Ngay DESC"""
                    cursor.execute(sql,(type,))
                else:
                    key = "%" + key + "%"
                    sql = """SELECT * FROM HOADON LEFT JOIN NguoiDung ON HOADON.IdNguoiDung = NguoiDung.IdNguoiDung WHERE HoTen LIKE %s AND TrangThai LIKE %s ORDER BY Ngay DESC"""
                    cursor.execute(sql,(key,type))
            return cursor.fetchall()
        except Error as e:
            print(f"[DAO ERROR] lỗi khi lấy danh sách {e}")
            return []
        
    def editState(self, IdHoaDon:int, State:str) -> Dict:
        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE hoadon SET TrangThai = %s WHERE IdHoaDon = %s", (State,IdHoaDon))
            self.conn.commit()
            return {"success": True}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi thay đổi hóa đơn: {e}")
            return {"success": False, "error": str(e)}
        finally:
            cursor.close()
            
    def add(self,Data:Dict)->Dict:
        try:
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO hoadon (Ngay, 
                                                TongTien, 
                                                PhuongThuc, 
                                                TrangThai, 
                                                IdNhanVien, 
                                                IdNguoiDung)
                            VALUES( %s, %s, %s, %s, %s, %s)""",
                            (Data['Ngay'],
                             Data['TongTien'],
                             Data['PhuongThuc'],
                             Data['TrangThai'],
                             Data['IdNhanVien'],
                             Data['IdNguoiDung'],))
            self.conn.commit()
            return {"success": True,'IdHoaDon':cursor.lastrowid}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi thay đổi hóa đơn: {e}")
            return {"success": False, "error": str(e)}
        finally:
            cursor.close()
    
    def getMonthly(self, month:int) -> float:
        result = {}
        date = datetime.today().date()
        if month != 0:
            date1 = date.replace(day = 1,month = month)
            date2 = date.replace(day = 1,month = month + 1) if month < 12 else date.replace(day=1,
                                                                                month=1,
                                                                                year=(date.year + 1))
        else:
            date1 = date.replace(day = 1,month = 12, year = date.year - 1)
            date2 = date.replace(day = 1,month = 1) 
            
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("""SELECT sum(TongTien) as total from hoadon 
                           WHERE TrangThai = "Đã thanh toán"
                           AND Ngay >= %s AND Ngay < %s""",
                            (date1,date2))
            result = cursor.fetchone()
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi thay đổi hóa đơn: {e}")
            result = 0
        finally:
            cursor.close()
            return 0 if result['total'] == None else result['total']