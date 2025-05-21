import mysql.connector
from mysql.connector import Error
from typing import List, Dict
from DAO.db_config import get_connection

class SanDAO:
    def __init__(self, conn=None):
        """Khởi tạo DAO với kết nối database tùy chọn"""
        self.conn = conn if conn is not None else get_connection()
        self._init_db()

    def _init_db(self):
        """Khởi tạo bảng nếu chưa tồn tại"""
        create_table = """
        CREATE TABLE IF NOT EXISTS san (
            idSan INT AUTO_INCREMENT PRIMARY KEY,
            coSan VARCHAR(10) NOT NULL,
            diaChi VARCHAR(255) NOT NULL,
            hinhAnh VARCHAR(255) DEFAULT 'default.jpg',
            soSan INT NOT NULL,
            moTa TEXT,
            trangThai INT NOT NULL DEFAULT 1,
            giaSan INT NOT NULL DEFAULT 0
        )
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(create_table)
            self.conn.commit()
        except Error as e:
            print(f"[DAO ERROR] Không thể tạo bảng: {e}")
            raise

    def lay_danh_sach_san(self) -> List[Dict]:
        """Lấy toàn bộ danh sách sân (phù hợp với bus)"""
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM san")
            return cursor.fetchall()
        except Error as e:
            print(f"[DAO ERROR] Lỗi khi lấy danh sách: {e}")
            return []

    def them_san(self, san_data: Dict) -> Dict:
        """Thêm sân mới (phù hợp với bus)"""
        if not san_data.get('coSan') or not san_data.get('diaChi'):
            return {"success": False, "error": "Thiếu thông tin bắt buộc"}

        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                INSERT INTO san (coSan, diaChi, hinhAnh, soSan, moTa, trangThai, giaSan)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    san_data['coSan'],
                    san_data['diaChi'],
                    san_data['hinhAnh'],
                    san_data['soSan'],
                    san_data['moTa'],
                    san_data['trangThai'],
                    san_data['giaSan']
                )
            )
            self.conn.commit()
            return {"success": True, "idSan": cursor.lastrowid}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi thêm sân: {e}")
            return {"success": False, "error": str(e)}
        finally:
            cursor.close()

    def sua_san(self, id_san: int, san_data: Dict) -> Dict:
        """Sửa thông tin sân (phù hợp với bus)"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                UPDATE san
                SET coSan = %s, diaChi = %s, hinhAnh = %s, soSan = %s,
                    moTa = %s, trangThai = %s, giaSan = %s
                WHERE idSan = %s
                """,
                (
                    san_data['coSan'],
                    san_data['diaChi'],
                    san_data['hinhAnh'],
                    san_data['soSan'],
                    san_data['moTa'],
                    san_data['trangThai'],
                    san_data['giaSan'],
                    id_san
                )
            )
            self.conn.commit()
            return {"success": cursor.rowcount > 0}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi sửa sân: {e}")
            return {"success": False, "error": str(e)}
        finally:
            cursor.close()

    def xoa_san(self, id_san: int) -> Dict:
        """Xóa sân (phù hợp với bus)"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM san WHERE idSan = %s", (id_san,))
            self.conn.commit()
            return {"success": cursor.rowcount > 0}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi xóa sân: {e}")
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