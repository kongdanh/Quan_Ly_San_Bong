from DAO.phieughiDAO import PhieuGhiDAO
from typing import List, Dict
from datetime import datetime
from mysql.connector import Error

class PhieuGhiBUS:
    danhSachPhieuGhi: List[Dict] = []
    def __init__(self, conn=None):
        self.phieuGhiDAO = PhieuGhiDAO(conn)

    def getListPhieuGhi(self,idNguoiDung:int = None) -> List[Dict]:
        return self.phieuGhiDAO.getListPhieuGhi(idNguoiDung)

    def xoaPhieuGhi(self, idPhieuGhi: int) -> Dict:
        return self.phieuGhiDAO.xoaPhieuGhi(idPhieuGhi)

    def updatePhieuGhi(self, Datas: Dict) -> Dict:
        return self.phieuGhiDAO.updatePhieuGhi(Datas)

    def themPhieuGhi(self, Datas: Dict) -> Dict:
        return self.phieuGhiDAO.themPhieuGhi(Datas)
    