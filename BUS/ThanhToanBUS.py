from DAO.ThanhToanDAO import ThanhToanDAO
from BUS.ChiTietThanhToanBUS import ChiTietThanhToanBUS
from typing import List, Dict
from datetime import datetime, timedelta

class ThanhToanBUS:
    danhSachThanhToan = []
    def __init__(self, conn=None):
        self.dao = ThanhToanDAO(conn)
        self.ChiTiet = ChiTietThanhToanBUS(conn)

    def getListThanhToan(self, idNguoiDung: int = None) -> List[Dict]:
        return self.dao.getListThanhToan(idNguoiDung)

    def addThanhToan(self, data: Dict) -> Dict:
        for x in data.values():
            if x is None:
                return {"success": False, "message": "Thiếu dữ liệu"}
        return self.dao.addThanhToan(data)

    def updateThanhToan(self, data: Dict) -> Dict:
        return self.dao.updateThanhToan(data)
    
    def deleteThanhToan(self, idThanhToan: int) -> Dict:
        if idThanhToan is None:
            return {"success": False, "message": "Thiếu dữ liệu"}
        listchitiet = self.ChiTiet.getListChiTietThanhToan(idThanhToan)
        for x in listchitiet:
            if not self.ChiTiet.deleteChiTietThanhToan(x['idPhieuGhi'], idThanhToan):
                return {"success": False, "message": "Lỗi khi xóa chi tiết thanh toán"}
        return self.dao.deleteThanhToan(idThanhToan)