import mysql.connector
from mysql.connector import Error
from typing import List, Dict
from DAO.db_config import get_connection

class NhanVienDAO:
    def __init__(self, conn=None):
        """Khởi tạo DAO với kết nối database tùy chọn"""
        self.conn = conn if conn is not None else get_connection()

    def lay_danh_sach_nhan_vien(self) -> List[Dict]:
        # lay danh sach tu dtb
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM nhanvien")
            return cursor.fetchall()
        except Error as e:
            print(f"[DAO ERROR] lỗi khi lấy danh sách {e}")
            return []
    
    def them_nhan_vien(self, nhan_vien_data: Dict) -> Dict:
        if not nhan_vien_data.get('HoTen') or not nhan_vien_data.get('SDT'):
            return {"success": False, "error": "Thiếu thông tin bắt buộc"}

        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO nhanvien (HoTen, NgaySinh, SDT, DiaChi, IdTaiKhoan) VALUES (%s, %s, %s, %s, %s)",
                (
                    nhan_vien_data['HoTen'],
                    nhan_vien_data['NgaySinh'],
                    nhan_vien_data['SDT'],
                    nhan_vien_data['DiaChi'],
                    nhan_vien_data['IdTaiKhoan']
                )
            )
            self.conn.commit()
            return {"success": True, "insert_id": cursor.lastrowid}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi thêm nhân viên: {e}")
            return {"success": False, "error": str(e)}
        finally:
            cursor.close()
    
    def sua_nhan_vien(self, id_nhan_vien: int, nhan_vien_data: Dict) -> Dict:
        """Sửa thông tin nhân viên"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                UPDATE nhanvien
                SET HoTen = %s, NgaySinh = %s, SDT = %s, DiaChi = %s, IdTaiKhoan = %s
                WHERE IdNhanVien = %s
                """,
                (
                    nhan_vien_data['HoTen'],
                    nhan_vien_data['NgaySinh'],
                    nhan_vien_data['SDT'],
                    nhan_vien_data['DiaChi'],
                    nhan_vien_data['IdTaiKhoan'],
                    id_nhan_vien
                )
            )
            self.conn.commit()
            return {"success": cursor.rowcount > 0}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi sửa nhân viên: {e}")
            return {"success": False, "error": str(e)}
        finally:
            cursor.close()

    def xoa_nhan_vien(self, id_nhan_vien: int) -> Dict:
        """Xóa nhân viên theo ID"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM nhanvien WHERE IdNhanVien = %s", (id_nhan_vien,))
            self.conn.commit()
            return {"success": cursor.rowcount > 0}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi xóa nhân viên: {e}")
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
