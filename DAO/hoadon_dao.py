import mysql.connector
from mysql.connector import Error
from typing import List, Dict
from DAO.db_config import get_connection

class HoaDonDAO:
    def __init__(self, conn=None):
        self.conn = conn if conn is not None else get_connection()
        
    def lay_danh_sach_hoa_don(self) -> List[Dict]:
        # lay ds tu dtb
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM hoadon")
            return cursor.fetchall()
        except Error as e:
            print(f"[DAO ERROR] lỗi khi lấy danh sách {e}")
            return []
    
    def them_hoa_don(self, hd_data: Dict) -> Dict:
        if not hd_data.get('IdHoaDon') or not hd_data.get('IdNhanVien'):
            return {"success": False, "error": "Thiếu thông tin bắt buộc"}

        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO hoadon (IdHoaDon, Ngay, TongTien, IdNhanVien) VALUES (%s, %s, %s, %s)",
                (
                    hd_data['IdHoaDon'],
                    hd_data['Ngay'],
                    hd_data['TongTien'],
                    hd_data['IdNhanVien']
                )
            )
            self.conn.commit()
            return {"success": True, "insert_id": cursor.lastrowid}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi thêm hóa đơn: {e}")
            return {"success": False, "error": str(e)}
        finally:
            cursor.close()
            
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