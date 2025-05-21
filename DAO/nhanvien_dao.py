import mysql.connector
from mysql.connector import Error
from typing import List, Dict
from DAO.db_config import get_connection

class NhanVienDAO:
    def __init__(self, conn=None):
        self.conn = conn if conn is not None else get_connection()

    def lay_danh_sach_nhan_vien(self) -> List[Dict]:
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM nhanvien")
            return cursor.fetchall()
        except Error as e:
            print(f"[DAO ERROR] Lỗi khi lấy danh sách: {e}")
            return []
        finally:
            cursor.close()

    def lay_nhan_vien_theo_id(self, id_nhan_vien: int) -> Dict:
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM nhanvien WHERE IdNhanVien = %s", (id_nhan_vien,))
            return cursor.fetchone() or {}
        except Error as e:
            print(f"[DAO ERROR] Lỗi khi lấy nhân viên theo ID: {e}")
            return {}
        finally:
            cursor.close()

    def them_nhan_vien(self, nhan_vien_data: Dict) -> Dict:
        required_fields = [
            'HoTen', 'NgaySinh', 'SDT', 'DiaChi', 'IdTaiKhoan', 'luong', 'chuc_vu', 'vi_tri',
            'ngayvaolam', 'hopdong', 'cccd', 'gioitinh', 'hoatdong'
        ]
        missing_fields = [field for field in required_fields if not nhan_vien_data.get(field)]
        if missing_fields:
            print(f"Thiếu trường bắt buộc trong nhanvien (DAO): {missing_fields}")
            return {"success": False, "error": f"Thiếu thông tin bắt buộc: {', '.join(missing_fields)}"}

        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                INSERT INTO nhanvien (
                    HoTen, NgaySinh, SDT, DiaChi, IdTaiKhoan, luong, chuc_vu, vi_tri, ngayvaolam, mota,
                    hopdong, phucap, cccd, gioitinh, nganhang, hoatdong
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    nhan_vien_data['HoTen'],
                    nhan_vien_data['NgaySinh'],
                    nhan_vien_data['SDT'],
                    nhan_vien_data['DiaChi'],
                    nhan_vien_data['IdTaiKhoan'],
                    nhan_vien_data['luong'],
                    nhan_vien_data['chuc_vu'],
                    nhan_vien_data['vi_tri'],
                    nhan_vien_data['ngayvaolam'],
                    nhan_vien_data.get('mota', ''),
                    nhan_vien_data['hopdong'],
                    nhan_vien_data.get('phucap', 0),
                    nhan_vien_data['cccd'],
                    nhan_vien_data['gioitinh'],
                    nhan_vien_data.get('nganhang', ''),
                    nhan_vien_data['hoatdong']
                )
            )
            self.conn.commit()
            print(f"Đã commit nhân viên, số hàng bị ảnh hưởng: {cursor.rowcount}")
            return {"success": True, "insert_id": cursor.lastrowid}
        except Error as e:
            self.conn.rollback()
            print(f"[DAO ERROR] Lỗi khi thêm nhân viên: {e}")
            return {"success": False, "error": str(e)}
        finally:
            cursor.close()

    def sua_nhan_vien(self, id_nhan_vien: int, nhan_vien_data: Dict) -> Dict:
        required_fields = [
            'HoTen', 'NgaySinh', 'SDT', 'DiaChi', 'IdTaiKhoan', 'luong', 'chuc_vu', 'vi_tri',
            'ngayvaolam', 'hopdong', 'cccd', 'gioitinh', 'hoatdong'
        ]
        missing_fields = [field for field in required_fields if not nhan_vien_data.get(field)]
        if missing_fields:
            print(f"Thiếu trường bắt buộc khi sửa nhân viên (DAO): {missing_fields}")
            return {"success": False, "error": f"Thiếu thông tin bắt buộc: {', '.join(missing_fields)}"}

        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                UPDATE nhanvien
                SET HoTen = %s, NgaySinh = %s, SDT = %s, DiaChi = %s, IdTaiKhoan = %s,
                    luong = %s, chuc_vu = %s, vi_tri = %s, ngayvaolam = %s, mota = %s,
                    hopdong = %s, phucap = %s, cccd = %s, gioitinh = %s, nganhang = %s,
                    hoatdong = %s
                WHERE IdNhanVien = %s
                """,
                (
                    nhan_vien_data['HoTen'],
                    nhan_vien_data['NgaySinh'],
                    nhan_vien_data['SDT'],
                    nhan_vien_data['DiaChi'],
                    nhan_vien_data['IdTaiKhoan'],
                    nhan_vien_data['luong'],
                    nhan_vien_data['chuc_vu'],
                    nhan_vien_data['vi_tri'],
                    nhan_vien_data['ngayvaolam'],
                    nhan_vien_data.get('mota', ''),
                    nhan_vien_data['hopdong'],
                    nhan_vien_data.get('phucap', 0),
                    nhan_vien_data['cccd'],
                    nhan_vien_data['gioitinh'],
                    nhan_vien_data.get('nganhang', ''),
                    nhan_vien_data['hoatdong'],
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
        if hasattr(self, 'conn') and self.conn is not None and self.conn.is_connected():
            try:
                self.conn.close()
                print("Kết nối database đã được đóng.")
            except Error as e:
                print(f"Lỗi khi đóng kết nối: {e}")