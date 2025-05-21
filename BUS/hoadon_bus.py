from datetime import datetime
from typing import Dict, List
from DAO.hoadon_dao import HoaDonDAO

class HoaDonBUS:
    def __init__(self, dao: HoaDonDAO = None):
        self.dao = dao if dao else HoaDonDAO()
        self.danh_sach_hoa_don = []
        
    def them_hoa_don(self, hd_data: Dict) -> Dict:
        try:
            # Gọi DAO để thêm hóa đơn
            result = self.dao.them_hoa_don(hd_data)
            if not result.get('success', False):
                print(f"[BUS ERROR] Thêm hóa đơn thất bại: {result.get('error', 'Không có thông tin lỗi')}", flush=True)
                return result

            # Lấy IdHoaDon vừa tạo
            cursor = self.dao.conn.cursor()
            cursor.execute("SELECT LAST_INSERT_ID()")
            id_hoa_don = cursor.fetchone()[0]
            cursor.close()

            if not id_hoa_don:
                print("[BUS ERROR] Không thể lấy IdHoaDon sau khi chèn", flush=True)
                return {'success': False, 'error': 'Không thể lấy IdHoaDon sau khi chèn'}

            print(f"[BUS INFO] Đã tạo hóa đơn mới với IdHoaDon: {id_hoa_don}", flush=True)
            return {'success': True, 'IdHoaDon': id_hoa_don}

        except Exception as e:
            print(f"[BUS ERROR] Lỗi khi thêm hóa đơn: {e}", flush=True)
            return {'success': False, 'error': str(e)}
    
    def sua_hoa_don(self, id_hoa_don: int, hd_data: Dict) -> Dict:
        if not hd_data.get('IdHoaDon') or not hd_data.get('IdNhanVien'):
            return {"success": False, "error": "Thiếu thông tin để cập nhật"}

        try:
            return self.dao.sua_hoa_don(id_hoa_don, hd_data)
        except Exception as e:
            print(f"[BUS ERROR] Lỗi khi gọi DAO sửa hóa đơn: {e}", flush=True)
            return {"success": False, "error": str(e)}
    
    def xoa_hoa_don(self, id_hoa_don):
        return self.dao.xoa_hoa_don(id_hoa_don)
    
    def lay_danh_sach_hoa_don(self, UID: int = None):
        danh_sach = self.dao.lay_danh_sach_hoa_don(UID)
        return danh_sach
    
    def updateHD(self, data: Dict):
        return self.dao.update(data)
    
    def timkiemHD(self, key: str, type: str) -> List[Dict]:
        return self.dao.timkiemHD(key, type)
    
    def editState(self, IdHoaDon: int, State: str) -> Dict:
        try:
            # Cập nhật trạng thái hóa đơn
            result = self.dao.editState(IdHoaDon, State)
            if not result.get('success', False):
                return result

            # Đồng bộ trạng thái phiếu ghi
            if State == 'Đã thanh toán':
                cursor = self.dao.conn.cursor()
                query = """
                UPDATE phieughi 
                SET TrangThai = 'Đã xác nhận'
                WHERE IdHoaDon = %s
                """
                cursor.execute(query, (IdHoaDon,))
                self.dao.conn.commit()
                cursor.close()
                print(f"[BUS INFO] Đã cập nhật trạng thái phiếu ghi cho IdHoaDon: {IdHoaDon}", flush=True)

            return {'success': True}
        except Exception as e:
            print(f"[BUS ERROR] Lỗi khi cập nhật trạng thái: {e}", flush=True)
            return {'success': False, 'error': str(e)}
    
    def addHD(self, Data: Dict) -> Dict:
        return self.dao.add(Data)
    
    def getMonthlyIncome(self) -> Dict:
        date = datetime.today().date()
        data = {}
        for x in range(1, 13):
            data[x] = self.dao.getMonthly(x)
        return data
    
    def getMonthIncome(self, month: int) -> float:
        return self.dao.getMonthly(month)
    
    def getTabs(self) -> Dict:
        data = {}
        date = datetime.today().date()
        data['curr'] = self.getMonthIncome(date.month) 
        data['prev'] = self.getMonthIncome(date.month - 1)
        data['rate'] = str(((data['curr'] / data['prev']) - 1) * 100) + "%" if data['prev'] != 0 else 'Chưa xác định'
        return data