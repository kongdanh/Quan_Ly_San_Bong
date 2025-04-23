from typing import List, Dict
from DAO.ChiTietThanhToanDAO import ChiTietThanhToanDAO

class ChiTietThanhToanBUS:
    danhSachChiTietThanhToan = []
    def __init__(self, conn=None):
        self.dao = ChiTietThanhToanDAO(conn)

    def getListChiTietThanhToan(self, idThanhToan=None) -> List[Dict]:
        return self.dao.getListChiTietThanhToan(idThanhToan)

    def addChiTietThanhToan(self, data: Dict) -> Dict:
        for x in data.values():
            if x is None:
                return {"success": False, "message": "Thiếu dữ liệu"}
        return self.dao.addChiTietThanhToan(data)

    def updateChiTietThanhToan(self, data: Dict) -> Dict:
        for x in data.values():
            if x is None:
                return {"success": False, "message": "Thiếu dữ liệu"}
        return self.dao.updateChiTietThanhToan(data)
    
    def deleteChiTietThanhToan(self, idPhieuGhi, idThanhToan) -> Dict:
        if idPhieuGhi is None or idThanhToan is None:
            return {"success": False, "message": "Thiếu dữ liệu"}
        return self.dao.deleteChiTietThanhToan(idPhieuGhi, idThanhToan)