from datetime import datetime
import mysql.connector
from mysql.connector import Error
from typing import List, Dict
from DAO.db_config import get_connection

class HoaDonDAO:
    def __init__(self, conn=None):
        self.conn = conn if conn is not None else get_connection()
        
    def lay_danh_sach_hoa_don(self, UID: int = None) -> List[Dict]:
        # Lấy danh sách từ database
        conn = get_connection()
        list = []
        try:
            cursor = conn.cursor(dictionary=True)
            if UID:
                cursor.execute("SELECT * FROM hoadon WHERE IdNguoiDung = %s AND status = 1", (UID,))
            else:
                cursor.execute("SELECT * FROM hoadon WHERE status = 1")
            list = cursor.fetchall()
        except Error as e:
            print(f"[DAO ERROR] Lỗi khi lấy danh sách: {e}")
        finally:
            conn.close()
            return list
    
    def them_hoa_don(self, hd_data: Dict) -> Dict:
        try:
            cursor = self.conn.cursor()
            query = """
            INSERT INTO hoadon (Ngay, TongTien, PhuongThuc, TrangThai, IdNhanVien, IdNguoiDung, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                hd_data['Ngay'],
                hd_data['TongTien'],
                hd_data.get('PhuongThuc', 'Tiền mặt'),
                hd_data.get('TrangThai', 0),
                hd_data.get('IdNhanVien'),
                hd_data.get('IdNguoiDung', None),
                hd_data.get('status', 1)
            )
            cursor.execute(query, values)
            self.conn.commit()
            cursor.close()
            return {'success': True}
        except Exception as e:
            self.conn.rollback()
            return {'success': False, 'error': str(e)}

    def editState(self, IdHoaDon: int, State: int) -> Dict:
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
            
    def sua_hoa_don(self, id_hoa_don: int, hd_data: Dict) -> Dict:
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
            cursor.execute("UPDATE hoadon SET status = 0 WHERE IdHoaDon = %s", (id_hoa_don,))
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
                
    def update(self, data: Dict):
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
            
    def timkiemHD(self, key: str, type: str) -> List[Dict]:
        try:
            cursor = self.conn.cursor(dictionary=True)
            if type == "":
                type_condition = ""
            else:
                type_condition = "AND TrangThai = %s"
            
            try:
                key = int(key)
                sql = f"""
                SELECT * FROM hoadon 
                LEFT JOIN NguoiDung ON hoadon.IdNguoiDung = NguoiDung.IdNguoiDung 
                WHERE IdHoaDon = %s {type_condition} AND hoadon.status = 1
                ORDER BY Ngay DESC
                """
                params = [key] if type == "" else [key, int(type)]  # Chuyển type sang int
                cursor.execute(sql, params)
            except ValueError:
                if key == "":
                    sql = f"""
                    SELECT * FROM hoadon 
                    LEFT JOIN NguoiDung ON hoadon.IdNguoiDung = NguoiDung.IdNguoiDung 
                    WHERE hoadon.status = 1 {type_condition}
                    ORDER BY Ngay DESC
                    """
                    params = [] if type == "" else [int(type)]
                    cursor.execute(sql, params)
                else:
                    key = "%" + key + "%"
                    sql = f"""
                    SELECT * FROM hoadon 
                    LEFT JOIN NguoiDung ON hoadon.IdNguoiDung = NguoiDung.IdNguoiDung 
                    WHERE HoTen LIKE %s {type_condition} AND hoadon.status = 1
                    ORDER BY Ngay DESC
                    """
                    params = [key] if type == "" else [key, int(type)]
                    cursor.execute(sql, params)
            return cursor.fetchall()
        except Error as e:
            print(f"[DAO ERROR] Lỗi khi lấy danh sách: {e}")
            return []
        
    def add(self, Data: Dict) -> Dict:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                INSERT INTO hoadon (Ngay, TongTien, PhuongThuc, TrangThai, IdNhanVien, IdNguoiDung)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    Data['Ngay'],
                    Data['TongTien'],
                    Data['PhuongThuc'],
                    Data['TrangThai'],
                    Data['IdNhanVien'],
                    Data['IdNguoiDung']
                )
            )
            self.conn.commit()
            return {"success": True, 'IdHoaDon': cursor.lastrowid}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi thêm hóa đơn: {e}")
            return {"success": False, "error": str(e)}
        finally:
            cursor.close()
    
    def getMonthly(self, month: int) -> float:
        result = {}
        date = datetime.today().date()
        if month != 0:
            date1 = date.replace(day=1, month=month)
            date2 = date.replace(day=1, month=month + 1) if month < 12 else date.replace(day=1, month=1, year=date.year + 1)
        else:
            date1 = date.replace(day=1, month=12, year=date.year - 1)
            date2 = date.replace(day=1, month=1)
            
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(
                """
                SELECT SUM(TongTien) as total FROM hoadon 
                WHERE TrangThai = 2 AND Ngay >= %s AND Ngay < %s AND status = 1
                """,
                (date1, date2)
            )
            result = cursor.fetchone()
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi lấy tổng doanh thu: {e}")
            result = 0
        finally:
            cursor.close()
            return 0 if result['total'] is None else result['total']

    def getHoaDonByUserId(self, user_id: int) -> List[Dict]:
        try:
            cursor = self.conn.cursor(dictionary=True)
            query = """
                SELECT IdHoaDon, Ngay, TongTien, PhuongThuc, IdNguoiDung, TrangThai, IdNhanVien
                FROM hoadon
                WHERE IdNguoiDung = %s AND status = 1
                ORDER BY Ngay DESC
            """
            cursor.execute(query, (user_id,))
            result = cursor.fetchall()
            cursor.close()
            print(f"DEBUG: HoaDonDAO.getHoaDonByUserId returned: {result}")  # Log để debug
            return result if result else []
        except Error as e:
            print(f"[DAO ERROR] Lỗi khi lấy hóa đơn: {e}")
            return []
    def get_by_id(self, id_hoa_don):
        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            query = """
                SELECT hd.IdHoaDon, hd.Ngay, hd.TongTien, hd.PhuongThuc, hd.TrangThai, 
                    hd.IdNhanVien, hd.IdNguoiDung, hd.status, nd.HoTen
                FROM hoadon hd
                LEFT JOIN NguoiDung nd ON hd.IdNguoiDung = nd.IdNguoiDung
                WHERE hd.IdHoaDon = %s AND hd.status = 1
            """
            cursor.execute(query, (id_hoa_don,))
            result = cursor.fetchone()
            return result if result else None
        except Exception as e:
            print(f"[DAO ERROR] Lỗi khi lấy hóa đơn theo ID: {e}", flush=True)
            return {'error': str(e)}
        finally:
            if cursor:
                cursor.close()