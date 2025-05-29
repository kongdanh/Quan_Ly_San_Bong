from DAO.phieughiDAO import PhieuGhiDAO
from typing import List, Dict
from datetime import datetime
from mysql.connector import Error
import re

class PhieuGhiBUS:
    danhSachPhieuGhi: List[Dict] = []
    danhSachKhungGio = [
        {'KhungGio': "8:00 - 10:00", 'list': []},
        {'KhungGio': "10:00 - 12:00", 'list': []},
        {'KhungGio': "14:00 -16:00", 'list': []},
        {'KhungGio': "16:00 - 18:00", 'list': []},
        {'KhungGio': "18:00 - 20:00", 'list': []}
    ]

    def __init__(self, conn=None):
        self.phieuGhiDAO = PhieuGhiDAO(conn)

    def getListPhieuGhi(self, idNguoiDung: int = None) -> List[Dict]:
        # Hiện tại không lọc theo idNguoiDung vì bảng phieughi không có cột này
        return self.phieuGhiDAO.getListPhieuGhi(idNguoiDung)

    def xoaPhieuGhi(self, idPhieuGhi: int) -> Dict:
        return self.phieuGhiDAO.xoaPhieuGhi(idPhieuGhi)

    def updatePhieuGhi(self, Datas: Dict) -> Dict:
        return self.phieuGhiDAO.updatePhieuGhi(Datas)

    def getListByDate(self, date: datetime) -> List[Dict]:
        try:
            print(f"DEBUG: Gọi getListByDate với date = {date}")
            result = self.phieuGhiDAO.getListByDate(date)
            print(f"DEBUG: Kết quả từ DAO.get_by_date = {result}")
            if not isinstance(result, list):
                print(f"Cảnh báo: get_by_date trả về {type(result)}, chuyển thành []")
                return []
            for item in result:
                item.setdefault('IdPhieuGhi', 0)
                item.setdefault('IdSan', 0)
                item.setdefault('Ngay', date.strftime("%Y-%m-%d"))
                item.setdefault('KhungGio', '')
                item.setdefault('GiaTien', 0)
                item.setdefault('IdHoaDon', 0)
                item.setdefault('status', 1)
                try:
                    item['GiaTien'] = float(item.get('GiaTien', 0) or 0)
                except (TypeError, ValueError):
                    print(f"Cảnh báo: GiaTien không hợp lệ cho IdPhieuGhi {item.get('IdPhieuGhi')}: {item.get('GiaTien')}")
                    item['GiaTien'] = 0
            return result
        except Exception as e:
            print(f"Lỗi trong getListByDate: {e}")
            return []

    def getReturn(self):
        return self.phieuGhiDAO.getReturn()

    def is_time_overlap(self, start1, end1, start2, end2):
        """Kiểm tra xem hai khung giờ có giao nhau không."""
        return start1 < end2 and start2 < end1

    def themPhieuGhi(self, Datas: Dict) -> Dict:
        try:
            # Lấy thông tin từ dữ liệu
            date = Datas.get('Ngay')
            sanID = Datas.get('IdSan')
            khung_gio = Datas.get('KhungGio')
            if not all([date, sanID, khung_gio]):
                return {'success': False, 'error': 'Dữ liệu đầu vào không đầy đủ'}

            # Kiểm tra định dạng khung giờ
            if not re.match(r'^\d{2}:\d{2}-\d{2}:\d{2}$', khung_gio):
                return {'success': False, 'error': 'Định dạng khung giờ không hợp lệ'}

            # Tách giờ bắt đầu và giờ kết thúc
            start_str, end_str = khung_gio.split('-')
            start_time = datetime.strptime(f"{date} {start_str}", '%Y-%m-%d %H:%M')
            end_time = datetime.strptime(f"{date} {end_str}", '%Y-%m-%d %H:%M')

            if end_time <= start_time:
                return {'success': False, 'error': 'Thời gian kết thúc phải sau thời gian bắt đầu'}

            # Lấy danh sách phiếu ghi hiện có cho ngày và sân
            existing_bookings = self.getListByDate(date)
            print(f"DEBUG: Existing bookings for {date}, IdSan {sanID}: {existing_bookings}")

            for booking in existing_bookings:
                if booking.get('status') != 1 or booking.get('IdSan') != sanID:
                    continue

                # Lấy khung giờ của phiếu ghi hiện có
                booking_khung_gio = booking.get('KhungGio')
                if not booking_khung_gio or not re.match(r'^\d{2}:\d{2}-\d{2}:\d{2}$', booking_khung_gio):
                    continue

                booking_start_str, booking_end_str = booking_khung_gio.split('-')
                booking_start = datetime.strptime(f"{date} {booking_start_str}", '%Y-%m-%d %H:%M')
                booking_end = datetime.strptime(f"{date} {booking_end_str}", '%Y-%m-%d %H:%M')

                # Kiểm tra giao nhau
                if self.is_time_overlap(start_time, end_time, booking_start, booking_end):
                    return {
                        'success': False,
                        'error': f'Khung giờ {khung_gio} giao với khung giờ đã đặt ({booking_khung_gio}). Vui lòng chọn khung giờ khác.'
                    }

            # Nếu không trùng, thêm phiếu ghi
            result = self.phieuGhiDAO.themPhieuGhi(Datas)
            if result.get('success', False):
                # Cập nhật danhSachPhieuGhi nếu cần
                self.danhSachPhieuGhi.append(Datas)
            return result

        except Exception as e:
            print(f"Lỗi trong themPhieuGhi: {e}")
            return {'success': False, 'error': str(e)}
    def get_by_hoa_don(self, id_hoa_don):
        return self.phieuGhiDAO.get_by_hoa_don(id_hoa_don)