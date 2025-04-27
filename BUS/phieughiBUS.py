from DAO.phieughiDAO import PhieuGhiDAO
from typing import List, Dict
from datetime import datetime
from mysql.connector import Error

class PhieuGhiBUS:
    danhSachPhieuGhi: List[Dict] = []
    danhSachKhungGio = [{'KhungGio':"8:00 - 10:00",'list':[]},
                        {'KhungGio':"10:00 - 12:00",'list':[]},
                        {'KhungGio':"14:00 -16:00",'list':[]},
                        {'KhungGio':"16:00 - 18:00",'list':[]},
                        {'KhungGio':"18:00 - 20:00",'list':[]}]
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
    
    def getListByDate(self, date: datetime) -> List[Dict]:
        try:
            list = self.phieuGhiDAO.getListByDate(date)
            print(list)
            new_list = PhieuGhiBUS.danhSachKhungGio
            i = 0
            for y in new_list:
                for x in range(i,len(list)):
                    if list[x]['KhungGio'] == y['KhungGio']:
                        y['list'].append(list[x]['KhungGio'])
                    else:
                        i=x
                        break
            print(new_list)
            return new_list
        except ValueError as e:
            print(f"[BUS ERROR] Lỗi khi chuyển đổi định dạng ngày: {e}")
            return []