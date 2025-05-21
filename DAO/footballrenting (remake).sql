-- SQL DUMP: Football Database with Users and Staff
-- Version: Updated - Full Sample Data

CREATE DATABASE IF NOT EXISTS football;
USE football;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

-- ----------------------------
-- Table structure
-- ----------------------------

CREATE TABLE `taikhoan` (
  `IdTaiKhoan` int(11) NOT NULL AUTO_INCREMENT,
  `TenTaiKhoan` varchar(50) DEFAULT NULL,
  `MatKhau` varchar(255) DEFAULT NULL,
  `NgayTao` date DEFAULT NULL,
  `AccType` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`IdTaiKhoan`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `nguoidung` (
  `IdNguoiDung` int(11) NOT NULL AUTO_INCREMENT,
  `HoTen` varchar(100) DEFAULT NULL,
  `NgaySinh` date DEFAULT NULL,
  `SDT` varchar(15) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `IdTaiKhoan` int(11) DEFAULT NULL,
  PRIMARY KEY (`IdNguoiDung`),
  KEY `IdTaiKhoan` (`IdTaiKhoan`),
  CONSTRAINT `nguoidung_ibfk_1` FOREIGN KEY (`IdTaiKhoan`) REFERENCES `taikhoan` (`IdTaiKhoan`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `nhanvien` (
  `IdNhanVien` int(11) NOT NULL AUTO_INCREMENT,
  `HoTen` varchar(100) DEFAULT NULL,
  `NgaySinh` date DEFAULT NULL,
  `SDT` varchar(15) DEFAULT NULL,
  `DiaChi` varchar(255) DEFAULT NULL,
  `IdTaiKhoan` int(11) DEFAULT NULL,
  `luong` bigint(20) DEFAULT NULL,
  `chuc_vu` varchar(100) DEFAULT NULL,
  `vi_tri` varchar(100) DEFAULT NULL,
  `ngayvaolam` date DEFAULT NULL,
  `mota` varchar(1000) DEFAULT NULL,
  `hopdong` varchar(100) DEFAULT NULL,
  `phucap` bigint(20) DEFAULT NULL,
  `cccd` varchar(12) DEFAULT NULL,
  `gioitinh` varchar(10) DEFAULT NULL,
  `nganhang` varchar(100) DEFAULT NULL,
  `hoatdong` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`IdNhanVien`),
  KEY `IdTaiKhoan` (`IdTaiKhoan`),
  CONSTRAINT `nhanvien_ibfk_1` FOREIGN KEY (`IdTaiKhoan`) REFERENCES `taikhoan` (`IdTaiKhoan`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `san` (
  `IdSan` int(11) NOT NULL AUTO_INCREMENT,
  `CoSan` varchar(20) DEFAULT NULL,
  `DiaChi` varchar(255) DEFAULT NULL,
  `HinhAnh` varchar(255) DEFAULT NULL,
  `SoSan` int(11) DEFAULT NULL,
  `MoTa` text DEFAULT 'Chưa có mô tả',
  `TrangThai` tinyint(4) DEFAULT 1,
  `GiaSan` int(11) DEFAULT NULL,
  PRIMARY KEY (`IdSan`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `hoadon` (
  `IdHoaDon` int(11) NOT NULL AUTO_INCREMENT,
  `Ngay` date DEFAULT NULL,
  `TongTien` decimal(10,2) DEFAULT NULL,
  `PhuongThuc` varchar(50) DEFAULT NULL,
  `TrangThai` varchar(20) DEFAULT NULL,
  `IdNhanVien` int(11) DEFAULT NULL,
  `IdNguoiDung` int(11) DEFAULT NULL,
  PRIMARY KEY (`IdHoaDon`),
  KEY `IdNhanVien` (`IdNhanVien`),
  KEY `IdNguoiDung` (`IdNguoiDung`),
  CONSTRAINT `hoadon_ibfk_1` FOREIGN KEY (`IdNhanVien`) REFERENCES `nhanvien` (`IdNhanVien`),
  CONSTRAINT `hoadon_ibfk_2` FOREIGN KEY (`IdNguoiDung`) REFERENCES `nguoidung` (`IdNguoiDung`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `phieughi` (
  `IdPhieuGhi` int(11) NOT NULL AUTO_INCREMENT,
  `Ngay` datetime DEFAULT NULL,
  `KhungGio` varchar(20) DEFAULT NULL,
  `GiaTien` decimal(10,2) DEFAULT NULL,
  `IdSan` int(11) DEFAULT NULL,
  `IdHoaDon` int(11) DEFAULT NULL,
  PRIMARY KEY (`IdPhieuGhi`),
  KEY `IdSan` (`IdSan`),
  KEY `IdHoaDon` (`IdHoaDon`),
  CONSTRAINT `phieughi_ibfk_1` FOREIGN KEY (`IdSan`) REFERENCES `san` (`IdSan`),
  CONSTRAINT `phieughi_ibfk_2` FOREIGN KEY (`IdHoaDon`) REFERENCES `hoadon` (`IdHoaDon`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Sample Data
-- ----------------------------

-- TAIKHOAN
INSERT INTO `taikhoan` (`TenTaiKhoan`, `MatKhau`, `NgayTao`, `AccType`) VALUES
('tranvanb', 'matkhau123', '2025-04-01', 'user'),
('lethic', 'matkhau456', '2025-04-01', 'user'),
('nguyenvand', 'matkhau789', '2025-04-01', 'user'),
('phamthie', 'matkhau321', '2025-04-01', 'user'),
('admin1', 'pass2', '2024-01-02', 'admin'),
('staff1', 'password1', '2025-04-21', 'staff'),
('staff2', 'password2', '2025-04-21', 'staff'),
('staff3', 'password3', '2025-04-21', 'staff'),
('staff4', 'password4', '2025-04-21', 'staff'),
('staff5', 'password5', '2025-04-21', 'staff'),
('staff6', 'password6', '2025-04-21', 'staff'),
('staff7', 'password7', '2025-04-21', 'staff'),
('staff8', 'password8', '2025-04-21', 'staff'),
('staff9', 'password9', '2025-04-21', 'staff'),
('staff10', 'password10', '2025-04-21', 'staff');

-- NGUOIDUNG
INSERT INTO `nguoidung` (`HoTen`, `NgaySinh`, `SDT`, `Email`, `IdTaiKhoan`) VALUES
('Tran Van B', '1998-06-12', '0911002200', 'tranvanb@example.com', 1),
('Le Thi C', '2001-03-22', '0933344556', 'lethic@example.com', 2),
('Nguyen Van D', '1997-09-10', '0909988776', 'nguyenvand@example.com', 3),
('Pham Thi E', '1995-12-01', '0922123444', 'phamthie@example.com', 4);

-- NHANVIEN
INSERT INTO `nhanvien` (
  `HoTen`, `NgaySinh`, `SDT`, `DiaChi`, `IdTaiKhoan`,
  `luong`, `chuc_vu`, `vi_tri`, `ngayvaolam`, `mota`,
  `hopdong`, `phucap`, `cccd`, `gioitinh`, `nganhang`, `hoatdong`
) VALUES
('Nguyen Van A', '1990-05-12', '0909123456', '789 Nguyễn Huệ', 5, 10000000, 'Quản lý', 'Tiếp tân', '2023-01-01', 'Chuyên hỗ trợ đặt sân', 'Dài hạn', 1000000, '123456789012', 'Nam', 'Vietcombank-123456', 'Hoạt động'),
('Tran Thi B', '1992-08-20', '0912123456', '456 Lý Tự Trọng', 6, 9000000, 'Nhân viên', 'Hậu cần', '2023-03-15', 'Phụ trách vệ sinh sân bãi', 'Thời vụ', 500000, '987654321098', 'Nữ', 'ACB-987654', 'Hoạt động'),
('Le Van C', '1992-11-30', '0923456789', '78 Lê Lợi, Đà Nẵng', 7, 12000000, 'Nhân viên', 'Trọng tài', '2022-06-20', NULL, 'Ngắn hạn', 1500000, '456789123', 'Nam', 'BIDV-4567891234', 'Hoạt động'),
('Pham Thi D', '1988-02-14', '0934567890', '56 Trần Phú, Nha Trang', 7, 13000000, 'Nhân viên', 'Hậu cần', '2019-09-05', NULL, 'Dài hạn', 1800000, '789123456', 'Nữ', 'MB Bank-7891234567', 'Nghỉ việc'),
('Hoang Van E', '1993-07-25', '0945678901', '89 Nguyễn Trãi, Huế', 8, 11000000, 'Nhân viên', 'Trọng tài', '2021-11-11', NULL, 'Trung hạn', 1200000, '321654987', 'Nam', 'Vietinbank-3216549870', 'Hoạt động'),
('Bui Thi F', '1996-04-18', '0956789012', '12 Phạm Văn Đồng, Hà Nội', 11, 9000000, 'Nhân viên', 'Thu ngân', '2023-02-25', NULL, 'Ngắn hạn', 800000, '654987321', 'Nữ', 'Agribank-6549873210', 'Nghỉ phép'),
('Nguyen Van G', '1991-09-09', '0967890123', '34 Hùng Vương, Hải Phòng', 5, 16000000, 'Quản lý', 'Quản lý sân', '2018-07-30', NULL, 'Dài hạn', 2500000, '147258369', 'Nam', 'Sacombank-1472583690', 'Hoạt động'),
('Tran Van H', '1989-12-12', '0978901234', '67 Lê Đại Hành, Đà Lạt', 8, 14000000, 'Nhân viên', 'Hậu cần', '2020-04-10', NULL, 'Trung hạn', 1700000, '258369147', 'Nam', 'VPBank-2583691470', 'Nghỉ việc'),
('Le Thi I', '1997-03-03', '0989012345', '90 Nguyễn Văn Cừ, Cần Thơ', 9, 9500000, 'Nhân viên', 'Thu ngân', '2022-08-15', NULL, 'Ngắn hạn', 900000, '369147258', 'Nữ', 'ACB-3691472580', 'Hoạt động'),
('Pham Van K', '1994-06-06', '0990123456', '23 Điện Biên Phủ, Vinh', 5, 15500000, 'Quản lý', 'Quản lý sân', '2019-12-01', NULL, 'Dài hạn', 2200000, '741852963', 'Nam', 'TPBank-7418529630', 'Nghỉ phép');

-- SAN
INSERT INTO `san` (`CoSan`, `DiaChi`, `HinhAnh`, `SoSan`, `MoTa`, `TrangThai`, `GiaSan`) VALUES
('11', '123 Lê Lợi', NULL, NULL, 'Chưa có mô tả', 1, NULL),
('7', '456 Trần Phú', NULL, NULL, 'Chưa có mô tả', 1, NULL),
('5', '789 Nguyễn Huệ', NULL, NULL, 'Chưa có mô tả', 1, NULL);

-- HOADON
INSERT INTO `hoadon` (`Ngay`, `TongTien`, `PhuongThuc`, `TrangThai`, `IdNhanVien`, `IdNguoiDung`) VALUES
('2025-04-15', 200000.00, 'Chuyển khoản', 'Chờ xác nhận', NULL, 1),
('2025-04-14', 250000.00, 'Tiền mặt', 'Đã xác nhận', 2, 2),
('2025-04-13', 300000.00, 'Tiền mặt', 'Đã thanh toán', 2, 3),
('2025-04-12', 150000.00, 'Chuyển khoản', 'Đã thanh toán', NULL, 4);

-- PHIEUGHI
INSERT INTO `phieughi` (`Ngay`, `KhungGio`, `GiaTien`, `IdSan`, `IdHoaDon`) VALUES
('2025-04-15 08:00:00', '8:00 - 10:00', 200000.00, 1, 1),
('2025-04-14 10:00:00', '10:00 - 12:00', 250000.00, 2, 2),
('2025-04-13 14:00:00', '14:00 - 16:00', 300000.00, 3, 3),
('2025-04-12 16:00:00', '16:00 - 18:00', 150000.00, 1, 4);

COMMIT;