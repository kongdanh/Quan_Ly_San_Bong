-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th5 08, 2025 lúc 09:17 PM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `footballrenting`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `chitiethoadon`
--

CREATE TABLE `chitiethoadon` (
  `IdHoaDon` int(11) NOT NULL,
  `IdPhieuGhi` int(11) NOT NULL,
  `ThoiDiemDat` datetime DEFAULT NULL,
  `KhungGio` varchar(50) DEFAULT NULL,
  `Tien` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `chitiethoadon`
--

INSERT INTO `chitiethoadon` (`IdHoaDon`, `IdPhieuGhi`, `ThoiDiemDat`, `KhungGio`, `Tien`) VALUES
(1, 1, '2024-04-15 10:00:00', '8-10', 200000.00),
(2, 2, '2025-05-10 08:00:00', '09:00 - 10:00', 220000.00),
(3, 3, '2025-05-10 10:00:00', '11:00 - 12:00', 250000.00),
(4, 4, '2025-05-11 13:00:00', '14:00 - 15:00', 200000.00),
(5, 5, '2025-05-11 15:00:00', '16:00 - 17:00', 230000.00),
(6, 6, '2025-05-12 09:00:00', '10:00 - 11:00', 240000.00),
(7, 7, '2025-05-12 11:00:00', '12:00 - 13:00', 210000.00),
(8, 8, '2025-05-13 14:00:00', '15:00 - 16:00', 260000.00),
(9, 9, '2025-05-13 16:00:00', '17:00 - 18:00', 220000.00),
(10, 10, '2025-05-14 08:00:00', '09:00 - 10:00', 250000.00),
(11, 11, '2025-05-14 10:00:00', '11:00 - 12:00', 230000.00),
(12, 12, '2025-05-10 08:00:00', '09:00 - 10:00', 220000.00),
(13, 13, '2025-05-10 10:00:00', '11:00 - 12:00', 250000.00),
(14, 14, '2025-05-11 13:00:00', '14:00 - 15:00', 200000.00),
(15, 15, '2025-05-11 15:00:00', '16:00 - 17:00', 230000.00),
(16, 16, '2025-05-12 09:00:00', '10:00 - 11:00', 240000.00),
(17, 17, '2025-05-12 11:00:00', '12:00 - 13:00', 210000.00),
(18, 18, '2025-05-13 14:00:00', '15:00 - 16:00', 260000.00),
(19, 19, '2025-05-13 16:00:00', '17:00 - 18:00', 220000.00),
(20, 20, '2025-05-14 08:00:00', '09:00 - 10:00', 250000.00),
(21, 21, '2025-05-14 10:00:00', '11:00 - 12:00', 230000.00);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `chitietthanhtoan`
--

CREATE TABLE `chitietthanhtoan` (
  `IdPhieuGhi` int(11) NOT NULL,
  `IdThanhToan` int(11) NOT NULL,
  `NgayThue` date DEFAULT NULL,
  `KhungGioThue` varchar(50) DEFAULT NULL,
  `Tien` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `chitietthanhtoan`
--

INSERT INTO `chitietthanhtoan` (`IdPhieuGhi`, `IdThanhToan`, `NgayThue`, `KhungGioThue`, `Tien`) VALUES
(1, 1, '2024-04-16', '08:00 - 09:00', 200000.00),
(12, 2, '2025-05-10', '09:00 - 10:00', 220000.00),
(13, 3, '2025-05-10', '11:00 - 12:00', 250000.00),
(14, 4, '2025-05-11', '14:00 - 15:00', 200000.00),
(15, 5, '2025-05-11', '16:00 - 17:00', 230000.00),
(16, 6, '2025-05-12', '10:00 - 11:00', 240000.00),
(17, 7, '2025-05-12', '12:00 - 13:00', 210000.00),
(18, 8, '2025-05-13', '15:00 - 16:00', 260000.00),
(19, 9, '2025-05-13', '17:00 - 18:00', 220000.00),
(20, 10, '2025-05-14', '09:00 - 10:00', 250000.00),
(21, 11, '2025-05-14', '11:00 - 12:00', 230000.00);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `hoadon`
--

CREATE TABLE `hoadon` (
  `IdHoaDon` int(11) NOT NULL,
  `Ngay` date DEFAULT NULL,
  `TongTien` decimal(10,2) DEFAULT NULL,
  `IdNhanVien` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `hoadon`
--

INSERT INTO `hoadon` (`IdHoaDon`, `Ngay`, `TongTien`, `IdNhanVien`) VALUES
(1, '2024-04-16', 200000.00, 1),
(2, '2025-05-10', 220000.00, 27),
(3, '2025-05-10', 250000.00, 28),
(4, '2025-05-11', 200000.00, 29),
(5, '2025-05-11', 230000.00, 30),
(6, '2025-05-12', 240000.00, 31),
(7, '2025-05-12', 210000.00, 32),
(8, '2025-05-13', 260000.00, 33),
(9, '2025-05-13', 220000.00, 34),
(10, '2025-05-14', 250000.00, 35),
(11, '2025-05-14', 230000.00, 36),
(12, '2025-05-10', 220000.00, 27),
(13, '2025-05-10', 250000.00, 28),
(14, '2025-05-11', 200000.00, 29),
(15, '2025-05-11', 230000.00, 30),
(16, '2025-05-12', 240000.00, 31),
(17, '2025-05-12', 210000.00, 32),
(18, '2025-05-13', 260000.00, 33),
(19, '2025-05-13', 220000.00, 34),
(20, '2025-05-14', 250000.00, 35),
(21, '2025-05-14', 230000.00, 36),
(22, '2025-05-10', 220000.00, 27),
(23, '2025-05-10', 250000.00, 28),
(24, '2025-05-11', 200000.00, 29),
(25, '2025-05-11', 230000.00, 30),
(26, '2025-05-12', 240000.00, 31),
(27, '2025-05-12', 210000.00, 32),
(28, '2025-05-13', 260000.00, 33),
(29, '2025-05-13', 220000.00, 34),
(30, '2025-05-14', 250000.00, 35),
(31, '2025-05-14', 230000.00, 36),
(32, '2025-05-10', 220000.00, 27),
(33, '2025-05-10', 250000.00, 28),
(34, '2025-05-11', 200000.00, 29),
(35, '2025-05-11', 230000.00, 30),
(36, '2025-05-12', 240000.00, 31),
(37, '2025-05-12', 210000.00, 32),
(38, '2025-05-13', 260000.00, 33),
(39, '2025-05-13', 220000.00, 34),
(40, '2025-05-14', 250000.00, 35),
(41, '2025-05-14', 230000.00, 36),
(42, '2025-05-10', 220000.00, 27),
(43, '2025-05-10', 250000.00, 28),
(44, '2025-05-11', 200000.00, 29),
(45, '2025-05-11', 230000.00, 30),
(46, '2025-05-12', 240000.00, 31),
(47, '2025-05-12', 210000.00, 32),
(48, '2025-05-13', 260000.00, 33),
(49, '2025-05-13', 220000.00, 34),
(50, '2025-05-14', 250000.00, 35),
(51, '2025-05-14', 230000.00, 36);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `nguoidung`
--

CREATE TABLE `nguoidung` (
  `IdNguoiDung` int(11) NOT NULL,
  `HoTen` varchar(100) DEFAULT NULL,
  `NgaySinh` date DEFAULT NULL,
  `SDT` varchar(15) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `IdTaiKhoan` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `nguoidung`
--

INSERT INTO `nguoidung` (`IdNguoiDung`, `HoTen`, `NgaySinh`, `SDT`, `Email`, `IdTaiKhoan`) VALUES
(1, 'Nguyen Van A', '2000-05-05', '0987654321', 'nguyenvanA@gmail.com', 1),
(2, 'Tran Van B', '1996-06-15', '0918765432', 'tranvanb@gmail.com', 13),
(3, 'Le Thi C', '1998-07-20', '0929876543', 'lethic@gmail.com', 14),
(4, 'Pham Van D', '1995-03-10', '0931234567', 'phamvand@gmail.com', 15),
(5, 'Nguyen Thi E', '2000-09-25', '0942345678', 'nguyenthie@gmail.com', 16),
(6, 'Hoang Van F', '1997-11-30', '0953456789', 'hoangvanf@gmail.com', 17),
(7, 'Bui Thi G', '1999-04-05', '0964567890', 'buithig@gmail.com', 18),
(8, 'Tran Van H', '1994-12-12', '0975678901', 'tranvanh@gmail.com', 19),
(9, 'Le Van I', '2001-01-15', '0986789012', 'levani@gmail.com', 20),
(10, 'Pham Thi K', '1993-08-20', '0997890123', 'phamthik@gmail.com', 21),
(11, 'Nguyen Van L', '1996-10-10', '0908901234', 'nguyenvanl@gmail.com', 22),
(12, 'Tran Van B', '1996-06-15', '0918765432', 'tranvanb@gmail.com', 13),
(13, 'Le Thi C', '1998-07-20', '0929876543', 'lethic@gmail.com', 14),
(14, 'Pham Van D', '1995-03-10', '0931234567', 'phamvand@gmail.com', 15),
(15, 'Nguyen Thi E', '2000-09-25', '0942345678', 'nguyenthie@gmail.com', 16),
(16, 'Hoang Van F', '1997-11-30', '0953456789', 'hoangvanf@gmail.com', 17),
(17, 'Bui Thi G', '1999-04-05', '0964567890', 'buithig@gmail.com', 18),
(18, 'Tran Van H', '1994-12-12', '0975678901', 'tranvanh@gmail.com', 19),
(19, 'Le Van I', '2001-01-15', '0986789012', 'levani@gmail.com', 20),
(20, 'Pham Thi K', '1993-08-20', '0997890123', 'phamthik@gmail.com', 21),
(21, 'Nguyen Van L', '1996-10-10', '0908901234', 'nguyenvanl@gmail.com', 22),
(22, 'Tran Van B', '1996-06-15', '0918765432', 'tranvanb@gmail.com', 13),
(23, 'Le Thi C', '1998-07-20', '0929876543', 'lethic@gmail.com', 14),
(24, 'Pham Van D', '1995-03-10', '0931234567', 'phamvand@gmail.com', 15),
(25, 'Nguyen Thi E', '2000-09-25', '0942345678', 'nguyenthie@gmail.com', 16),
(26, 'Hoang Van F', '1997-11-30', '0953456789', 'hoangvanf@gmail.com', 17),
(27, 'Bui Thi G', '1999-04-05', '0964567890', 'buithig@gmail.com', 18),
(28, 'Tran Van H', '1994-12-12', '0975678901', 'tranvanh@gmail.com', 19),
(29, 'Le Van I', '2001-01-15', '0986789012', 'levani@gmail.com', 20),
(30, 'Pham Thi K', '1993-08-20', '0997890123', 'phamthik@gmail.com', 21),
(31, 'Nguyen Van L', '1996-10-10', '0908901234', 'nguyenvanl@gmail.com', 22),
(32, 'Tran Van B', '1996-06-15', '0918765432', 'tranvanb@gmail.com', 13),
(33, 'Le Thi C', '1998-07-20', '0929876543', 'lethic@gmail.com', 14),
(34, 'Pham Van D', '1995-03-10', '0931234567', 'phamvand@gmail.com', 15),
(35, 'Nguyen Thi E', '2000-09-25', '0942345678', 'nguyenthie@gmail.com', 16),
(36, 'Hoang Van F', '1997-11-30', '0953456789', 'hoangvanf@gmail.com', 17),
(37, 'Bui Thi G', '1999-04-05', '0964567890', 'buithig@gmail.com', 18),
(38, 'Tran Van H', '1994-12-12', '0975678901', 'tranvanh@gmail.com', 19),
(39, 'Le Van I', '2001-01-15', '0986789012', 'levani@gmail.com', 20),
(40, 'Pham Thi K', '1993-08-20', '0997890123', 'phamthik@gmail.com', 21),
(41, 'Nguyen Van L', '1996-10-10', '0908901234', 'nguyenvanl@gmail.com', 22),
(42, 'Tran Van B', '1996-06-15', '0918765432', 'tranvanb@gmail.com', 13),
(43, 'Le Thi C', '1998-07-20', '0929876543', 'lethic@gmail.com', 14),
(44, 'Pham Van D', '1995-03-10', '0931234567', 'phamvand@gmail.com', 15),
(45, 'Nguyen Thi E', '2000-09-25', '0942345678', 'nguyenthie@gmail.com', 16),
(46, 'Hoang Van F', '1997-11-30', '0953456789', 'hoangvanf@gmail.com', 17),
(47, 'Bui Thi G', '1999-04-05', '0964567890', 'buithig@gmail.com', 18),
(48, 'Tran Van H', '1994-12-12', '0975678901', 'tranvanh@gmail.com', 19),
(49, 'Le Van I', '2001-01-15', '0986789012', 'levani@gmail.com', 20),
(50, 'Pham Thi K', '1993-08-20', '0997890123', 'phamthik@gmail.com', 21),
(51, 'Nguyen Van L', '1996-10-10', '0908901234', 'nguyenvanl@gmail.com', 22),
(52, 'Tran Van B', '1996-06-15', '0918765432', 'tranvanb@gmail.com', 13),
(53, 'Le Thi C', '1998-07-20', '0929876543', 'lethic@gmail.com', 14),
(54, 'Pham Van D', '1995-03-10', '0931234567', 'phamvand@gmail.com', 15),
(55, 'Nguyen Thi E', '2000-09-25', '0942345678', 'nguyenthie@gmail.com', 16),
(56, 'Hoang Van F', '1997-11-30', '0953456789', 'hoangvanf@gmail.com', 17),
(57, 'Bui Thi G', '1999-04-05', '0964567890', 'buithig@gmail.com', 18),
(58, 'Tran Van H', '1994-12-12', '0975678901', 'tranvanh@gmail.com', 19),
(59, 'Le Van I', '2001-01-15', '0986789012', 'levani@gmail.com', 20),
(60, 'Pham Thi K', '1993-08-20', '0997890123', 'phamthik@gmail.com', 21),
(61, 'Nguyen Van L', '1996-10-10', '0908901234', 'nguyenvanl@gmail.com', 22),
(62, 'Tran Van B', '1996-06-15', '0918765432', 'tranvanb@gmail.com', 13),
(63, 'Le Thi C', '1998-07-20', '0929876543', 'lethic@gmail.com', 14),
(64, 'Pham Van D', '1995-03-10', '0931234567', 'phamvand@gmail.com', 15),
(65, 'Nguyen Thi E', '2000-09-25', '0942345678', 'nguyenthie@gmail.com', 16),
(66, 'Hoang Van F', '1997-11-30', '0953456789', 'hoangvanf@gmail.com', 17),
(67, 'Bui Thi G', '1999-04-05', '0964567890', 'buithig@gmail.com', 18),
(68, 'Tran Van H', '1994-12-12', '0975678901', 'tranvanh@gmail.com', 19),
(69, 'Le Van I', '2001-01-15', '0986789012', 'levani@gmail.com', 20),
(70, 'Pham Thi K', '1993-08-20', '0997890123', 'phamthik@gmail.com', 21),
(71, 'Nguyen Van L', '1996-10-10', '0908901234', 'nguyenvanl@gmail.com', 22);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `nhanvien`
--

CREATE TABLE `nhanvien` (
  `IdNhanVien` int(11) NOT NULL,
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
  `hoatdong` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `nhanvien`
--

INSERT INTO `nhanvien` (`IdNhanVien`, `HoTen`, `NgaySinh`, `SDT`, `DiaChi`, `IdTaiKhoan`, `luong`, `chuc_vu`, `vi_tri`, `ngayvaolam`, `mota`, `hopdong`, `phucap`, `cccd`, `gioitinh`, `nganhang`, `hoatdong`) VALUES
(1, 'Tran Thi B', '1995-10-08', '0912345678', 'Da Nang', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(6, 'nv1', '1111-11-11', '1111', '111', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(17, 'Nguyen Van A', '1990-05-15', '0901234567', '123 Đường Láng, Hà Nội', 3, 15000000, 'Quản lý', 'Quản lý sân', '2020-01-10', NULL, 'Dài hạn', 2000000, '123456789', 'Nam', 'Vietcombank-1234567890', 'Hoạt động'),
(18, 'Tran Thi B', '1995-08-22', '0912345678', '45 Nguyễn Huệ, TP.HCM', 2, 10000000, 'Nhân viên', 'Thu ngân', '2021-03-15', NULL, 'Trung hạn', 1000000, '987654321', 'Nữ', 'Techcombank-9876543210', 'Nghỉ phép'),
(19, 'Le Van C', '1992-11-30', '0923456789', '78 Lê Lợi, Đà Nẵng', 3, 12000000, 'Nhân viên', 'Trọng tài', '2022-06-20', NULL, 'Ngắn hạn', 1500000, '456789123', 'Nam', 'BIDV-4567891234', 'Hoạt động'),
(20, 'Pham Thi D', '1988-02-14', '0934567890', '56 Trần Phú, Nha Trang', 4, 13000000, 'Nhân viên', 'Hậu cần', '2019-09-05', NULL, 'Dài hạn', 1800000, '789123456', 'Nữ', 'MB Bank-7891234567', 'Nghỉ việc'),
(21, 'Hoang Van E', '1993-07-25', '0945678901', '89 Nguyễn Trãi, Huế', 5, 11000000, 'Nhân viên', 'Trọng tài', '2021-11-11', NULL, 'Trung hạn', 1200000, '321654987', 'Nam', 'Vietinbank-3216549870', 'Hoạt động'),
(22, 'Bui Thi F', '1996-04-18', '0956789012', '12 Phạm Văn Đồng, Hà Nội', 6, 9000000, 'Nhân viên', 'Thu ngân', '2023-02-25', NULL, 'Ngắn hạn', 800000, '654987321', 'Nữ', 'Agribank-6549873210', 'Nghỉ phép'),
(23, 'Nguyen Van G', '1991-09-09', '0967890123', '34 Hùng Vương, Hải Phòng', 7, 16000000, 'Quản lý', 'Quản lý sân', '2018-07-30', NULL, 'Dài hạn', 2500000, '147258369', 'Nam', 'Sacombank-1472583690', 'Hoạt động'),
(24, 'Tran Van H', '1989-12-12', '0978901234', '67 Lê Đại Hành, Đà Lạt', 8, 14000000, 'Nhân viên', 'Hậu cần', '2020-04-10', NULL, 'Trung hạn', 1700000, '258369147', 'Nam', 'VPBank-2583691470', 'Nghỉ việc'),
(25, 'Le Thi I', '1997-03-03', '0989012345', '90 Nguyễn Văn Cừ, Cần Thơ', 9, 9500000, 'Nhân viên', 'Thu ngân', '2022-08-15', NULL, 'Ngắn hạn', 900000, '369147258', 'Nữ', 'ACB-3691472580', 'Hoạt động'),
(26, 'Pham Van K', '1994-06-06', '0990123456', '23 Điện Biên Phủ, Vinh', 10, 15500000, 'Quản lý', 'Quản lý sân', '2019-12-01', NULL, 'Dài hạn', 2200000, '741852963', 'Nam', 'TPBank-7418529630', 'Nghỉ phép'),
(27, 'Vo Thi M', '1992-05-15', '0987654321', '10 Lê Lợi, Hà Nội', 23, 11000000, 'Nhân viên', 'Thu ngân', '2023-01-10', NULL, 'Ngắn hạn', 1000000, '111222333', 'Nữ', 'Vietcombank-1112223330', 'Hoạt động'),
(28, 'Nguyen Van N', '1989-07-20', '0912345678', '20 Trần Phú, TP.HCM', 24, 12000000, 'Nhân viên', 'Trọng tài', '2022-06-15', NULL, 'Trung hạn', 1500000, '222333444', 'Nam', 'Techcombank-2223334440', 'Hoạt động'),
(29, 'Le Thi O', '1994-03-25', '0923456789', '30 Nguyễn Huệ, Đà Nẵng', 25, 13000000, 'Nhân viên', 'Hậu cần', '2021-09-10', NULL, 'Dài hạn', 1800000, '333444555', 'Nữ', 'BIDV-3334445550', 'Hoạt động'),
(30, 'Pham Van P', '1991-11-30', '0934567890', '40 Lê Lợi, Cần Thơ', 26, 14000000, 'Quản lý', 'Quản lý sân', '2020-03-20', NULL, 'Dài hạn', 2000000, '444555666', 'Nam', 'MB Bank-4445556660', 'Hoạt động'),
(31, 'Hoang Thi Q', '1997-06-05', '0945678901', '50 Trần Hưng Đạo, Huế', 27, 10000000, 'Nhân viên', 'Thu ngân', '2023-04-15', NULL, 'Ngắn hạn', 900000, '555666777', 'Nữ', 'Vietinbank-5556667770', 'Nghỉ phép'),
(32, 'Bui Van R', '1995-09-10', '0956789012', '60 Nguyễn Trãi, Vinh', 28, 11500000, 'Nhân viên', 'Trọng tài', '2022-07-20', NULL, 'Trung hạn', 1200000, '666777888', 'Nam', 'Agribank-6667778880', 'Hoạt động'),
(33, 'Tran Thi S', '1990-12-15', '0967890123', '70 Phạm Văn Đồng, Hải Phòng', 29, 12500000, 'Nhân viên', 'Hậu cần', '2021-10-25', NULL, 'Dài hạn', 1600000, '777888999', 'Nữ', 'Sacombank-7778889990', 'Hoạt động'),
(34, 'Le Van T', '1993-02-20', '0978901234', '80 Lê Đại Hành, Đà Lạt', 30, 13500000, 'Quản lý', 'Quản lý sân', '2020-05-30', NULL, 'Dài hạn', 1900000, '888999000', 'Nam', 'VPBank-8889990000', 'Hoạt động'),
(35, 'Pham Thi U', '1998-04-25', '0989012345', '90 Nguyễn Văn Cừ, Nha Trang', 31, 10500000, 'Nhân viên', 'Thu ngân', '2023-02-10', NULL, 'Ngắn hạn', 1100000, '999000111', 'Nữ', 'ACB-9990001110', 'Hoạt động'),
(36, 'Nguyen Van V', '1996-08-30', '0990123456', '100 Điện Biên Phủ, Hà Nội', 32, 14500000, 'Quản lý', 'Quản lý sân', '2019-11-15', NULL, 'Dài hạn', 2100000, '000111222', 'Nam', 'TPBank-0001112220', 'Hoạt động'),
(37, 'Vo Thi M', '1992-05-15', '0987654321', '10 Lê Lợi, Hà Nội', 23, 11000000, 'Nhân viên', 'Thu ngân', '2023-01-10', NULL, 'Ngắn hạn', 1000000, '111222333', 'Nữ', 'Vietcombank-1112223330', 'Hoạt động'),
(38, 'Nguyen Van N', '1989-07-20', '0912345678', '20 Trần Phú, TP.HCM', 24, 12000000, 'Nhân viên', 'Trọng tài', '2022-06-15', NULL, 'Trung hạn', 1500000, '222333444', 'Nam', 'Techcombank-2223334440', 'Hoạt động'),
(39, 'Le Thi O', '1994-03-25', '0923456789', '30 Nguyễn Huệ, Đà Nẵng', 25, 13000000, 'Nhân viên', 'Hậu cần', '2021-09-10', NULL, 'Dài hạn', 1800000, '333444555', 'Nữ', 'BIDV-3334445550', 'Hoạt động'),
(40, 'Pham Van P', '1991-11-30', '0934567890', '40 Lê Lợi, Cần Thơ', 26, 14000000, 'Quản lý', 'Quản lý sân', '2020-03-20', NULL, 'Dài hạn', 2000000, '444555666', 'Nam', 'MB Bank-4445556660', 'Hoạt động'),
(41, 'Hoang Thi Q', '1997-06-05', '0945678901', '50 Trần Hưng Đạo, Huế', 27, 10000000, 'Nhân viên', 'Thu ngân', '2023-04-15', NULL, 'Ngắn hạn', 900000, '555666777', 'Nữ', 'Vietinbank-5556667770', 'Nghỉ phép'),
(42, 'Bui Van R', '1995-09-10', '0956789012', '60 Nguyễn Trãi, Vinh', 28, 11500000, 'Nhân viên', 'Trọng tài', '2022-07-20', NULL, 'Trung hạn', 1200000, '666777888', 'Nam', 'Agribank-6667778880', 'Hoạt động'),
(43, 'Tran Thi S', '1990-12-15', '0967890123', '70 Phạm Văn Đồng, Hải Phòng', 29, 12500000, 'Nhân viên', 'Hậu cần', '2021-10-25', NULL, 'Dài hạn', 1600000, '777888999', 'Nữ', 'Sacombank-7778889990', 'Hoạt động'),
(44, 'Le Van T', '1993-02-20', '0978901234', '80 Lê Đại Hành, Đà Lạt', 30, 13500000, 'Quản lý', 'Quản lý sân', '2020-05-30', NULL, 'Dài hạn', 1900000, '888999000', 'Nam', 'VPBank-8889990000', 'Hoạt động'),
(45, 'Pham Thi U', '1998-04-25', '0989012345', '90 Nguyễn Văn Cừ, Nha Trang', 31, 10500000, 'Nhân viên', 'Thu ngân', '2023-02-10', NULL, 'Ngắn hạn', 1100000, '999000111', 'Nữ', 'ACB-9990001110', 'Hoạt động'),
(46, 'Nguyen Van V', '1996-08-30', '0990123456', '100 Điện Biên Phủ, Hà Nội', 32, 14500000, 'Quản lý', 'Quản lý sân', '2019-11-15', NULL, 'Dài hạn', 2100000, '000111222', 'Nam', 'TPBank-0001112220', 'Hoạt động'),
(47, 'Vo Thi M', '1992-05-15', '0987654321', '10 Lê Lợi, Hà Nội', 23, 11000000, 'Nhân viên', 'Thu ngân', '2023-01-10', NULL, 'Ngắn hạn', 1000000, '111222333', 'Nữ', 'Vietcombank-1112223330', 'Hoạt động'),
(48, 'Nguyen Van N', '1989-07-20', '0912345678', '20 Trần Phú, TP.HCM', 24, 12000000, 'Nhân viên', 'Trọng tài', '2022-06-15', NULL, 'Trung hạn', 1500000, '222333444', 'Nam', 'Techcombank-2223334440', 'Hoạt động'),
(49, 'Le Thi O', '1994-03-25', '0923456789', '30 Nguyễn Huệ, Đà Nẵng', 25, 13000000, 'Nhân viên', 'Hậu cần', '2021-09-10', NULL, 'Dài hạn', 1800000, '333444555', 'Nữ', 'BIDV-3334445550', 'Hoạt động'),
(50, 'Pham Van P', '1991-11-30', '0934567890', '40 Lê Lợi, Cần Thơ', 26, 14000000, 'Quản lý', 'Quản lý sân', '2020-03-20', NULL, 'Dài hạn', 2000000, '444555666', 'Nam', 'MB Bank-4445556660', 'Hoạt động'),
(51, 'Hoang Thi Q', '1997-06-05', '0945678901', '50 Trần Hưng Đạo, Huế', 27, 10000000, 'Nhân viên', 'Thu ngân', '2023-04-15', NULL, 'Ngắn hạn', 900000, '555666777', 'Nữ', 'Vietinbank-5556667770', 'Nghỉ phép'),
(52, 'Bui Van R', '1995-09-10', '0956789012', '60 Nguyễn Trãi, Vinh', 28, 11500000, 'Nhân viên', 'Trọng tài', '2022-07-20', NULL, 'Trung hạn', 1200000, '666777888', 'Nam', 'Agribank-6667778880', 'Hoạt động'),
(53, 'Tran Thi S', '1990-12-15', '0967890123', '70 Phạm Văn Đồng, Hải Phòng', 29, 12500000, 'Nhân viên', 'Hậu cần', '2021-10-25', NULL, 'Dài hạn', 1600000, '777888999', 'Nữ', 'Sacombank-7778889990', 'Hoạt động'),
(54, 'Le Van T', '1993-02-20', '0978901234', '80 Lê Đại Hành, Đà Lạt', 30, 13500000, 'Quản lý', 'Quản lý sân', '2020-05-30', NULL, 'Dài hạn', 1900000, '888999000', 'Nam', 'VPBank-8889990000', 'Hoạt động'),
(55, 'Pham Thi U', '1998-04-25', '0989012345', '90 Nguyễn Văn Cừ, Nha Trang', 31, 10500000, 'Nhân viên', 'Thu ngân', '2023-02-10', NULL, 'Ngắn hạn', 1100000, '999000111', 'Nữ', 'ACB-9990001110', 'Hoạt động'),
(56, 'Nguyen Van V', '1996-08-30', '0990123456', '100 Điện Biên Phủ, Hà Nội', 32, 14500000, 'Quản lý', 'Quản lý sân', '2019-11-15', NULL, 'Dài hạn', 2100000, '000111222', 'Nam', 'TPBank-0001112220', 'Hoạt động'),
(57, 'Vo Thi M', '1992-05-15', '0987654321', '10 Lê Lợi, Hà Nội', 23, 11000000, 'Nhân viên', 'Thu ngân', '2023-01-10', NULL, 'Ngắn hạn', 1000000, '111222333', 'Nữ', 'Vietcombank-1112223330', 'Hoạt động'),
(58, 'Nguyen Van N', '1989-07-20', '0912345678', '20 Trần Phú, TP.HCM', 24, 12000000, 'Nhân viên', 'Trọng tài', '2022-06-15', NULL, 'Trung hạn', 1500000, '222333444', 'Nam', 'Techcombank-2223334440', 'Hoạt động'),
(59, 'Le Thi O', '1994-03-25', '0923456789', '30 Nguyễn Huệ, Đà Nẵng', 25, 13000000, 'Nhân viên', 'Hậu cần', '2021-09-10', NULL, 'Dài hạn', 1800000, '333444555', 'Nữ', 'BIDV-3334445550', 'Hoạt động'),
(60, 'Pham Van P', '1991-11-30', '0934567890', '40 Lê Lợi, Cần Thơ', 26, 14000000, 'Quản lý', 'Quản lý sân', '2020-03-20', NULL, 'Dài hạn', 2000000, '444555666', 'Nam', 'MB Bank-4445556660', 'Hoạt động'),
(61, 'Hoang Thi Q', '1997-06-05', '0945678901', '50 Trần Hưng Đạo, Huế', 27, 10000000, 'Nhân viên', 'Thu ngân', '2023-04-15', NULL, 'Ngắn hạn', 900000, '555666777', 'Nữ', 'Vietinbank-5556667770', 'Nghỉ phép'),
(62, 'Bui Van R', '1995-09-10', '0956789012', '60 Nguyễn Trãi, Vinh', 28, 11500000, 'Nhân viên', 'Trọng tài', '2022-07-20', NULL, 'Trung hạn', 1200000, '666777888', 'Nam', 'Agribank-6667778880', 'Hoạt động'),
(63, 'Tran Thi S', '1990-12-15', '0967890123', '70 Phạm Văn Đồng, Hải Phòng', 29, 12500000, 'Nhân viên', 'Hậu cần', '2021-10-25', NULL, 'Dài hạn', 1600000, '777888999', 'Nữ', 'Sacombank-7778889990', 'Hoạt động'),
(64, 'Le Van T', '1993-02-20', '0978901234', '80 Lê Đại Hành, Đà Lạt', 30, 13500000, 'Quản lý', 'Quản lý sân', '2020-05-30', NULL, 'Dài hạn', 1900000, '888999000', 'Nam', 'VPBank-8889990000', 'Hoạt động'),
(65, 'Pham Thi U', '1998-04-25', '0989012345', '90 Nguyễn Văn Cừ, Nha Trang', 31, 10500000, 'Nhân viên', 'Thu ngân', '2023-02-10', NULL, 'Ngắn hạn', 1100000, '999000111', 'Nữ', 'ACB-9990001110', 'Hoạt động'),
(66, 'Nguyen Van V', '1996-08-30', '0990123456', '100 Điện Biên Phủ, Hà Nội', 32, 14500000, 'Quản lý', 'Quản lý sân', '2019-11-15', NULL, 'Dài hạn', 2100000, '000111222', 'Nam', 'TPBank-0001112220', 'Hoạt động'),
(67, 'Vo Thi M', '1992-05-15', '0987654321', '10 Lê Lợi, Hà Nội', 23, 11000000, 'Nhân viên', 'Thu ngân', '2023-01-10', NULL, 'Ngắn hạn', 1000000, '111222333', 'Nữ', 'Vietcombank-1112223330', 'Hoạt động'),
(68, 'Nguyen Van N', '1989-07-20', '0912345678', '20 Trần Phú, TP.HCM', 24, 12000000, 'Nhân viên', 'Trọng tài', '2022-06-15', NULL, 'Trung hạn', 1500000, '222333444', 'Nam', 'Techcombank-2223334440', 'Hoạt động'),
(69, 'Le Thi O', '1994-03-25', '0923456789', '30 Nguyễn Huệ, Đà Nẵng', 25, 13000000, 'Nhân viên', 'Hậu cần', '2021-09-10', NULL, 'Dài hạn', 1800000, '333444555', 'Nữ', 'BIDV-3334445550', 'Hoạt động'),
(70, 'Pham Van P', '1991-11-30', '0934567890', '40 Lê Lợi, Cần Thơ', 26, 14000000, 'Quản lý', 'Quản lý sân', '2020-03-20', NULL, 'Dài hạn', 2000000, '444555666', 'Nam', 'MB Bank-4445556660', 'Hoạt động'),
(71, 'Hoang Thi Q', '1997-06-05', '0945678901', '50 Trần Hưng Đạo, Huế', 27, 10000000, 'Nhân viên', 'Thu ngân', '2023-04-15', NULL, 'Ngắn hạn', 900000, '555666777', 'Nữ', 'Vietinbank-5556667770', 'Nghỉ phép'),
(72, 'Bui Van R', '1995-09-10', '0956789012', '60 Nguyễn Trãi, Vinh', 28, 11500000, 'Nhân viên', 'Trọng tài', '2022-07-20', NULL, 'Trung hạn', 1200000, '666777888', 'Nam', 'Agribank-6667778880', 'Hoạt động'),
(73, 'Tran Thi S', '1990-12-15', '0967890123', '70 Phạm Văn Đồng, Hải Phòng', 29, 12500000, 'Nhân viên', 'Hậu cần', '2021-10-25', NULL, 'Dài hạn', 1600000, '777888999', 'Nữ', 'Sacombank-7778889990', 'Hoạt động'),
(74, 'Le Van T', '1993-02-20', '0978901234', '80 Lê Đại Hành, Đà Lạt', 30, 13500000, 'Quản lý', 'Quản lý sân', '2020-05-30', NULL, 'Dài hạn', 1900000, '888999000', 'Nam', 'VPBank-8889990000', 'Hoạt động'),
(75, 'Pham Thi U', '1998-04-25', '0989012345', '90 Nguyễn Văn Cừ, Nha Trang', 31, 10500000, 'Nhân viên', 'Thu ngân', '2023-02-10', NULL, 'Ngắn hạn', 1100000, '999000111', 'Nữ', 'ACB-9990001110', 'Hoạt động'),
(76, 'Nguyen Van V', '1996-08-30', '0990123456', '100 Điện Biên Phủ, Hà Nội', 32, 14500000, 'Quản lý', 'Quản lý sân', '2019-11-15', NULL, 'Dài hạn', 2100000, '000111222', 'Nam', 'TPBank-0001112220', 'Hoạt động'),
(77, 'Vo Thi M', '1992-05-15', '0987654321', '10 Lê Lợi, Hà Nội', 23, 11000000, 'Nhân viên', 'Thu ngân', '2023-01-10', NULL, 'Ngắn hạn', 1000000, '111222333', 'Nữ', 'Vietcombank-1112223330', 'Hoạt động'),
(78, 'Nguyen Van N', '1989-07-20', '0912345678', '20 Trần Phú, TP.HCM', 24, 12000000, 'Nhân viên', 'Trọng tài', '2022-06-15', NULL, 'Trung hạn', 1500000, '222333444', 'Nam', 'Techcombank-2223334440', 'Hoạt động'),
(79, 'Le Thi O', '1994-03-25', '0923456789', '30 Nguyễn Huệ, Đà Nẵng', 25, 13000000, 'Nhân viên', 'Hậu cần', '2021-09-10', NULL, 'Dài hạn', 1800000, '333444555', 'Nữ', 'BIDV-3334445550', 'Hoạt động'),
(80, 'Pham Van P', '1991-11-30', '0934567890', '40 Lê Lợi, Cần Thơ', 26, 14000000, 'Quản lý', 'Quản lý sân', '2020-03-20', NULL, 'Dài hạn', 2000000, '444555666', 'Nam', 'MB Bank-4445556660', 'Hoạt động'),
(81, 'Hoang Thi Q', '1997-06-05', '0945678901', '50 Trần Hưng Đạo, Huế', 27, 10000000, 'Nhân viên', 'Thu ngân', '2023-04-15', NULL, 'Ngắn hạn', 900000, '555666777', 'Nữ', 'Vietinbank-5556667770', 'Nghỉ phép'),
(82, 'Bui Van R', '1995-09-10', '0956789012', '60 Nguyễn Trãi, Vinh', 28, 11500000, 'Nhân viên', 'Trọng tài', '2022-07-20', NULL, 'Trung hạn', 1200000, '666777888', 'Nam', 'Agribank-6667778880', 'Hoạt động'),
(83, 'Tran Thi S', '1990-12-15', '0967890123', '70 Phạm Văn Đồng, Hải Phòng', 29, 12500000, 'Nhân viên', 'Hậu cần', '2021-10-25', NULL, 'Dài hạn', 1600000, '777888999', 'Nữ', 'Sacombank-7778889990', 'Hoạt động'),
(84, 'Le Van T', '1993-02-20', '0978901234', '80 Lê Đại Hành, Đà Lạt', 30, 13500000, 'Quản lý', 'Quản lý sân', '2020-05-30', NULL, 'Dài hạn', 1900000, '888999000', 'Nam', 'VPBank-8889990000', 'Hoạt động'),
(85, 'Pham Thi U', '1998-04-25', '0989012345', '90 Nguyễn Văn Cừ, Nha Trang', 31, 10500000, 'Nhân viên', 'Thu ngân', '2023-02-10', NULL, 'Ngắn hạn', 1100000, '999000111', 'Nữ', 'ACB-9990001110', 'Hoạt động'),
(86, 'Nguyen Van V', '1996-08-30', '0990123456', '100 Điện Biên Phủ, Hà Nội', 32, 14500000, 'Quản lý', 'Quản lý sân', '2019-11-15', NULL, 'Dài hạn', 2100000, '000111222', 'Nam', 'TPBank-0001112220', 'Hoạt động');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `phieughi`
--

CREATE TABLE `phieughi` (
  `IdPhieuGhi` int(11) NOT NULL,
  `Ngay` datetime DEFAULT NULL,
  `KhungGio` varchar(20) DEFAULT NULL,
  `TrangThai` varchar(20) DEFAULT NULL,
  `GiaTien` decimal(10,2) DEFAULT NULL,
  `IdSan` int(11) DEFAULT NULL,
  `IdNguoiDung` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `phieughi`
--

INSERT INTO `phieughi` (`IdPhieuGhi`, `Ngay`, `KhungGio`, `TrangThai`, `GiaTien`, `IdSan`, `IdNguoiDung`) VALUES
(1, '2024-04-16 00:00:00', '8:00 - 9:00', 'Dat', 200000.00, 1, 1),
(2, '2025-05-10 09:00:00', '09:00 - 10:00', 'Dat', 220000.00, 12, 2),
(3, '2025-05-10 11:00:00', '11:00 - 12:00', 'Dat', 250000.00, 13, 3),
(4, '2025-05-11 14:00:00', '14:00 - 15:00', 'Dat', 200000.00, 14, 4),
(5, '2025-05-11 16:00:00', '16:00 - 17:00', 'Dat', 230000.00, 15, 5),
(6, '2025-05-12 10:00:00', '10:00 - 11:00', 'Dat', 240000.00, 16, 6),
(7, '2025-05-12 12:00:00', '12:00 - 13:00', 'Dat', 210000.00, 17, 7),
(8, '2025-05-13 15:00:00', '15:00 - 16:00', 'Dat', 260000.00, 18, 8),
(9, '2025-05-13 17:00:00', '17:00 - 18:00', 'Dat', 220000.00, 19, 9),
(10, '2025-05-14 09:00:00', '09:00 - 10:00', 'Dat', 250000.00, 20, 10),
(11, '2025-05-14 11:00:00', '11:00 - 12:00', 'Dat', 230000.00, 21, 11),
(12, '2025-05-10 09:00:00', '09:00 - 10:00', 'Dat', 220000.00, 12, 2),
(13, '2025-05-10 11:00:00', '11:00 - 12:00', 'Dat', 250000.00, 13, 3),
(14, '2025-05-11 14:00:00', '14:00 - 15:00', 'Dat', 200000.00, 14, 4),
(15, '2025-05-11 16:00:00', '16:00 - 17:00', 'Dat', 230000.00, 15, 5),
(16, '2025-05-12 10:00:00', '10:00 - 11:00', 'Dat', 240000.00, 16, 6),
(17, '2025-05-12 12:00:00', '12:00 - 13:00', 'Dat', 210000.00, 17, 7),
(18, '2025-05-13 15:00:00', '15:00 - 16:00', 'Dat', 260000.00, 18, 8),
(19, '2025-05-13 17:00:00', '17:00 - 18:00', 'Dat', 220000.00, 19, 9),
(20, '2025-05-14 09:00:00', '09:00 - 10:00', 'Dat', 250000.00, 20, 10),
(21, '2025-05-14 11:00:00', '11:00 - 12:00', 'Dat', 230000.00, 21, 11),
(22, '2025-05-10 09:00:00', '09:00 - 10:00', 'Dat', 220000.00, 12, 2),
(23, '2025-05-10 11:00:00', '11:00 - 12:00', 'Dat', 250000.00, 13, 3),
(24, '2025-05-11 14:00:00', '14:00 - 15:00', 'Dat', 200000.00, 14, 4),
(25, '2025-05-11 16:00:00', '16:00 - 17:00', 'Dat', 230000.00, 15, 5),
(26, '2025-05-12 10:00:00', '10:00 - 11:00', 'Dat', 240000.00, 16, 6),
(27, '2025-05-12 12:00:00', '12:00 - 13:00', 'Dat', 210000.00, 17, 7),
(28, '2025-05-13 15:00:00', '15:00 - 16:00', 'Dat', 260000.00, 18, 8),
(29, '2025-05-13 17:00:00', '17:00 - 18:00', 'Dat', 220000.00, 19, 9),
(30, '2025-05-14 09:00:00', '09:00 - 10:00', 'Dat', 250000.00, 20, 10),
(31, '2025-05-14 11:00:00', '11:00 - 12:00', 'Dat', 230000.00, 21, 11),
(32, '2025-05-10 09:00:00', '09:00 - 10:00', 'Dat', 220000.00, 12, 2),
(33, '2025-05-10 11:00:00', '11:00 - 12:00', 'Dat', 250000.00, 13, 3),
(34, '2025-05-11 14:00:00', '14:00 - 15:00', 'Dat', 200000.00, 14, 4),
(35, '2025-05-11 16:00:00', '16:00 - 17:00', 'Dat', 230000.00, 15, 5),
(36, '2025-05-12 10:00:00', '10:00 - 11:00', 'Dat', 240000.00, 16, 6),
(37, '2025-05-12 12:00:00', '12:00 - 13:00', 'Dat', 210000.00, 17, 7),
(38, '2025-05-13 15:00:00', '15:00 - 16:00', 'Dat', 260000.00, 18, 8),
(39, '2025-05-13 17:00:00', '17:00 - 18:00', 'Dat', 220000.00, 19, 9),
(40, '2025-05-14 09:00:00', '09:00 - 10:00', 'Dat', 250000.00, 20, 10),
(41, '2025-05-14 11:00:00', '11:00 - 12:00', 'Dat', 230000.00, 21, 11),
(42, '2025-05-10 09:00:00', '09:00 - 10:00', 'Dat', 220000.00, 12, 2),
(43, '2025-05-10 11:00:00', '11:00 - 12:00', 'Dat', 250000.00, 13, 3),
(44, '2025-05-11 14:00:00', '14:00 - 15:00', 'Dat', 200000.00, 14, 4),
(45, '2025-05-11 16:00:00', '16:00 - 17:00', 'Dat', 230000.00, 15, 5),
(46, '2025-05-12 10:00:00', '10:00 - 11:00', 'Dat', 240000.00, 16, 6),
(47, '2025-05-12 12:00:00', '12:00 - 13:00', 'Dat', 210000.00, 17, 7),
(48, '2025-05-13 15:00:00', '15:00 - 16:00', 'Dat', 260000.00, 18, 8),
(49, '2025-05-13 17:00:00', '17:00 - 18:00', 'Dat', 220000.00, 19, 9),
(50, '2025-05-14 09:00:00', '09:00 - 10:00', 'Dat', 250000.00, 20, 10),
(51, '2025-05-14 11:00:00', '11:00 - 12:00', 'Dat', 230000.00, 21, 11);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `san`
--

CREATE TABLE `san` (
  `IdSan` int(11) NOT NULL,
  `CoSan` varchar(20) DEFAULT NULL,
  `DiaChi` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `san`
--

INSERT INTO `san` (`IdSan`, `CoSan`, `DiaChi`) VALUES
(1, '11', '123 Lê Lợi'),
(2, '7', '456 Trần Phú'),
(9, '5', '347 Tân Bình'),
(12, '11', '234 Nguyễn Văn Linh, TP.HCM'),
(13, '7', '345 Trần Hưng Đạo, Hà Nội'),
(14, '5', '456 Lê Văn Sỹ, Đà Nẵng'),
(15, '11', '567 Nguyễn Đình Chiểu, Cần Thơ'),
(16, '7', '678 Phạm Ngũ Lão, Huế'),
(17, '5', '789 Trần Phú, Nha Trang'),
(18, '11', '890 Hùng Vương, Hải Phòng'),
(19, '7', '901 Lê Đại Hành, Đà Lạt'),
(20, '5', '1012 Nguyễn Trãi, Vinh'),
(21, '11', '1123 Phạm Văn Đồng, Hà Nội'),
(22, '11', '234 Nguyễn Văn Linh, TP.HCM'),
(23, '7', '345 Trần Hưng Đạo, Hà Nội'),
(24, '5', '456 Lê Văn Sỹ, Đà Nẵng'),
(25, '11', '567 Nguyễn Đình Chiểu, Cần Thơ'),
(26, '7', '678 Phạm Ngũ Lão, Huế'),
(27, '5', '789 Trần Phú, Nha Trang'),
(28, '11', '890 Hùng Vương, Hải Phòng'),
(29, '7', '901 Lê Đại Hành, Đà Lạt'),
(30, '5', '1012 Nguyễn Trãi, Vinh'),
(31, '11', '1123 Phạm Văn Đồng, Hà Nội'),
(32, '11', '234 Nguyễn Văn Linh, TP.HCM'),
(33, '7', '345 Trần Hưng Đạo, Hà Nội'),
(34, '5', '456 Lê Văn Sỹ, Đà Nẵng'),
(35, '11', '567 Nguyễn Đình Chiểu, Cần Thơ'),
(36, '7', '678 Phạm Ngũ Lão, Huế'),
(37, '5', '789 Trần Phú, Nha Trang'),
(38, '11', '890 Hùng Vương, Hải Phòng'),
(39, '7', '901 Lê Đại Hành, Đà Lạt'),
(40, '5', '1012 Nguyễn Trãi, Vinh'),
(41, '11', '1123 Phạm Văn Đồng, Hà Nội'),
(42, '11', '234 Nguyễn Văn Linh, TP.HCM'),
(43, '7', '345 Trần Hưng Đạo, Hà Nội'),
(44, '5', '456 Lê Văn Sỹ, Đà Nẵng'),
(45, '11', '567 Nguyễn Đình Chiểu, Cần Thơ'),
(46, '7', '678 Phạm Ngũ Lão, Huế'),
(47, '5', '789 Trần Phú, Nha Trang'),
(48, '11', '890 Hùng Vương, Hải Phòng'),
(49, '7', '901 Lê Đại Hành, Đà Lạt'),
(50, '5', '1012 Nguyễn Trãi, Vinh'),
(51, '11', '1123 Phạm Văn Đồng, Hà Nội'),
(52, '11', '234 Nguyễn Văn Linh, TP.HCM'),
(53, '7', '345 Trần Hưng Đạo, Hà Nội'),
(54, '5', '456 Lê Văn Sỹ, Đà Nẵng'),
(55, '11', '567 Nguyễn Đình Chiểu, Cần Thơ'),
(56, '7', '678 Phạm Ngũ Lão, Huế'),
(57, '5', '789 Trần Phú, Nha Trang'),
(58, '11', '890 Hùng Vương, Hải Phòng'),
(59, '7', '901 Lê Đại Hành, Đà Lạt'),
(60, '5', '1012 Nguyễn Trãi, Vinh'),
(61, '11', '1123 Phạm Văn Đồng, Hà Nội');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `taikhoan`
--

CREATE TABLE `taikhoan` (
  `IdTaiKhoan` int(11) NOT NULL,
  `TenTaiKhoan` varchar(50) DEFAULT NULL,
  `MatKhau` varchar(255) DEFAULT NULL,
  `NgayTao` date DEFAULT NULL,
  `AccType` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `taikhoan`
--

INSERT INTO `taikhoan` (`IdTaiKhoan`, `TenTaiKhoan`, `MatKhau`, `NgayTao`, `AccType`) VALUES
(1, 'user1', 'pass1', '2024-01-01', 'user'),
(2, 'admin1', 'pass2', '2024-01-02', 'admin'),
(3, 'staff1', 'password1', '2025-04-21', 'staff'),
(4, 'staff2', 'password2', '2025-04-21', 'staff'),
(5, 'staff3', 'password3', '2025-04-21', 'staff'),
(6, 'staff4', 'password4', '2025-04-21', 'staff'),
(7, 'staff5', 'password5', '2025-04-21', 'staff'),
(8, 'staff6', 'password6', '2025-04-21', 'staff'),
(9, 'staff7', 'password7', '2025-04-21', 'staff'),
(10, 'staff8', 'password8', '2025-04-21', 'staff'),
(11, 'staff9', 'password9', '2025-04-21', 'staff'),
(12, 'staff10', 'password10', '2025-04-21', 'staff'),
(13, 'user2', 'pass123', '2025-05-01', 'user'),
(14, 'user3', 'pass456', '2025-05-02', 'user'),
(15, 'user4', 'pass789', '2025-05-03', 'user'),
(16, 'user5', 'pass101', '2025-05-04', 'user'),
(17, 'admin2', 'adminpass', '2025-05-01', 'admin'),
(18, 'staff11', 'staffpass11', '2025-05-03', 'staff'),
(19, 'staff12', 'staffpass12', '2025-05-04', 'staff'),
(20, 'staff13', 'staffpass13', '2025-05-05', 'staff'),
(21, 'staff14', 'staffpass14', '2025-05-06', 'staff'),
(22, 'staff15', 'staffpass15', '2025-05-07', 'staff'),
(23, 'user2', 'pass123', '2025-05-01', 'user'),
(24, 'user3', 'pass456', '2025-05-02', 'user'),
(25, 'user4', 'pass789', '2025-05-03', 'user'),
(26, 'user5', 'pass101', '2025-05-04', 'user'),
(27, 'admin2', 'adminpass', '2025-05-01', 'admin'),
(28, 'staff11', 'staffpass11', '2025-05-03', 'staff'),
(29, 'staff12', 'staffpass12', '2025-05-04', 'staff'),
(30, 'staff13', 'staffpass13', '2025-05-05', 'staff'),
(31, 'staff14', 'staffpass14', '2025-05-06', 'staff'),
(32, 'staff15', 'staffpass15', '2025-05-07', 'staff'),
(33, 'user2', 'pass123', '2025-05-01', 'user'),
(34, 'user3', 'pass456', '2025-05-02', 'user'),
(35, 'user4', 'pass789', '2025-05-03', 'user'),
(36, 'user5', 'pass101', '2025-05-04', 'user'),
(37, 'admin2', 'adminpass', '2025-05-01', 'admin'),
(38, 'staff11', 'staffpass11', '2025-05-03', 'staff'),
(39, 'staff12', 'staffpass12', '2025-05-04', 'staff'),
(40, 'staff13', 'staffpass13', '2025-05-05', 'staff'),
(41, 'staff14', 'staffpass14', '2025-05-06', 'staff'),
(42, 'staff15', 'staffpass15', '2025-05-07', 'staff'),
(43, 'user2', 'pass123', '2025-05-01', 'user'),
(44, 'user3', 'pass456', '2025-05-02', 'user'),
(45, 'user4', 'pass789', '2025-05-03', 'user'),
(46, 'user5', 'pass101', '2025-05-04', 'user'),
(47, 'admin2', 'adminpass', '2025-05-01', 'admin'),
(48, 'staff11', 'staffpass11', '2025-05-03', 'staff'),
(49, 'staff12', 'staffpass12', '2025-05-04', 'staff'),
(50, 'staff13', 'staffpass13', '2025-05-05', 'staff'),
(51, 'staff14', 'staffpass14', '2025-05-06', 'staff'),
(52, 'staff15', 'staffpass15', '2025-05-07', 'staff'),
(53, 'user2', 'pass123', '2025-05-01', 'user'),
(54, 'user3', 'pass456', '2025-05-02', 'user'),
(55, 'user4', 'pass789', '2025-05-03', 'user'),
(56, 'user5', 'pass101', '2025-05-04', 'user'),
(57, 'admin2', 'adminpass', '2025-05-01', 'admin'),
(58, 'staff11', 'staffpass11', '2025-05-03', 'staff'),
(59, 'staff12', 'staffpass12', '2025-05-04', 'staff'),
(60, 'staff13', 'staffpass13', '2025-05-05', 'staff'),
(61, 'staff14', 'staffpass14', '2025-05-06', 'staff'),
(62, 'staff15', 'staffpass15', '2025-05-07', 'staff'),
(63, 'user2', 'pass123', '2025-05-01', 'user'),
(64, 'user3', 'pass456', '2025-05-02', 'user'),
(65, 'user4', 'pass789', '2025-05-03', 'user'),
(66, 'user5', 'pass101', '2025-05-04', 'user'),
(67, 'admin2', 'adminpass', '2025-05-01', 'admin'),
(68, 'staff11', 'staffpass11', '2025-05-03', 'staff'),
(69, 'staff12', 'staffpass12', '2025-05-04', 'staff'),
(70, 'staff13', 'staffpass13', '2025-05-05', 'staff'),
(71, 'staff14', 'staffpass14', '2025-05-06', 'staff'),
(72, 'staff15', 'staffpass15', '2025-05-07', 'staff'),
(73, 'user2', 'pass123', '2025-05-01', 'user'),
(74, 'user3', 'pass456', '2025-05-02', 'user'),
(75, 'user4', 'pass789', '2025-05-03', 'user'),
(76, 'user5', 'pass101', '2025-05-04', 'user'),
(77, 'admin2', 'adminpass', '2025-05-01', 'admin'),
(78, 'staff11', 'staffpass11', '2025-05-03', 'staff'),
(79, 'staff12', 'staffpass12', '2025-05-04', 'staff'),
(80, 'staff13', 'staffpass13', '2025-05-05', 'staff'),
(81, 'staff14', 'staffpass14', '2025-05-06', 'staff'),
(82, 'staff15', 'staffpass15', '2025-05-07', 'staff'),
(83, 'user2', 'pass123', '2025-05-01', 'user'),
(84, 'user3', 'pass456', '2025-05-02', 'user'),
(85, 'user4', 'pass789', '2025-05-03', 'user'),
(86, 'user5', 'pass101', '2025-05-04', 'user'),
(87, 'admin2', 'adminpass', '2025-05-01', 'admin'),
(88, 'staff11', 'staffpass11', '2025-05-03', 'staff'),
(89, 'staff12', 'staffpass12', '2025-05-04', 'staff'),
(90, 'staff13', 'staffpass13', '2025-05-05', 'staff'),
(91, 'staff14', 'staffpass14', '2025-05-06', 'staff'),
(92, 'staff15', 'staffpass15', '2025-05-07', 'staff');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `thanhtoan`
--

CREATE TABLE `thanhtoan` (
  `IdThanhToan` int(11) NOT NULL,
  `Ngay` date DEFAULT NULL,
  `TongTien` decimal(10,2) DEFAULT NULL,
  `PhuongThuc` varchar(50) DEFAULT NULL,
  `TrangThai` varchar(20) DEFAULT NULL,
  `IdNguoiDung` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `thanhtoan`
--

INSERT INTO `thanhtoan` (`IdThanhToan`, `Ngay`, `TongTien`, `PhuongThuc`, `TrangThai`, `IdNguoiDung`) VALUES
(1, '2024-04-16', 200000.00, 'Tien mat', 'Da thanh toan', 1),
(2, '2025-05-10', 220000.00, 'Tien mat', 'Da thanh toan', 2),
(3, '2025-05-10', 250000.00, 'Chuyen khoan', 'Da thanh toan', 3),
(4, '2025-05-11', 200000.00, 'Tien mat', 'Da thanh toan', 4),
(5, '2025-05-11', 230000.00, 'Chuyen khoan', 'Da thanh toan', 5),
(6, '2025-05-12', 240000.00, 'Tien mat', 'Da thanh toan', 6),
(7, '2025-05-12', 210000.00, 'Chuyen khoan', 'Da thanh toan', 7),
(8, '2025-05-13', 260000.00, 'Tien mat', 'Da thanh toan', 8),
(9, '2025-05-13', 220000.00, 'Chuyen khoan', 'Da thanh toan', 9),
(10, '2025-05-14', 250000.00, 'Tien mat', 'Da thanh toan', 10),
(11, '2025-05-14', 230000.00, 'Chuyen khoan', 'Da thanh toan', 11);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `chitiethoadon`
--
ALTER TABLE `chitiethoadon`
  ADD PRIMARY KEY (`IdHoaDon`,`IdPhieuGhi`),
  ADD KEY `IdPhieuGhi` (`IdPhieuGhi`);

--
-- Chỉ mục cho bảng `chitietthanhtoan`
--
ALTER TABLE `chitietthanhtoan`
  ADD PRIMARY KEY (`IdPhieuGhi`,`IdThanhToan`),
  ADD KEY `IdThanhToan` (`IdThanhToan`);

--
-- Chỉ mục cho bảng `hoadon`
--
ALTER TABLE `hoadon`
  ADD PRIMARY KEY (`IdHoaDon`),
  ADD KEY `IdNhanVien` (`IdNhanVien`);

--
-- Chỉ mục cho bảng `nguoidung`
--
ALTER TABLE `nguoidung`
  ADD PRIMARY KEY (`IdNguoiDung`),
  ADD KEY `IdTaiKhoan` (`IdTaiKhoan`);

--
-- Chỉ mục cho bảng `nhanvien`
--
ALTER TABLE `nhanvien`
  ADD PRIMARY KEY (`IdNhanVien`),
  ADD KEY `IdTaiKhoan` (`IdTaiKhoan`);

--
-- Chỉ mục cho bảng `phieughi`
--
ALTER TABLE `phieughi`
  ADD PRIMARY KEY (`IdPhieuGhi`),
  ADD KEY `IdSan` (`IdSan`),
  ADD KEY `IdNguoiDung` (`IdNguoiDung`);

--
-- Chỉ mục cho bảng `san`
--
ALTER TABLE `san`
  ADD PRIMARY KEY (`IdSan`);

--
-- Chỉ mục cho bảng `taikhoan`
--
ALTER TABLE `taikhoan`
  ADD PRIMARY KEY (`IdTaiKhoan`);

--
-- Chỉ mục cho bảng `thanhtoan`
--
ALTER TABLE `thanhtoan`
  ADD PRIMARY KEY (`IdThanhToan`),
  ADD KEY `IdNguoiDung` (`IdNguoiDung`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `hoadon`
--
ALTER TABLE `hoadon`
  MODIFY `IdHoaDon` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- AUTO_INCREMENT cho bảng `nguoidung`
--
ALTER TABLE `nguoidung`
  MODIFY `IdNguoiDung` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=72;

--
-- AUTO_INCREMENT cho bảng `nhanvien`
--
ALTER TABLE `nhanvien`
  MODIFY `IdNhanVien` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=87;

--
-- AUTO_INCREMENT cho bảng `phieughi`
--
ALTER TABLE `phieughi`
  MODIFY `IdPhieuGhi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- AUTO_INCREMENT cho bảng `san`
--
ALTER TABLE `san`
  MODIFY `IdSan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- AUTO_INCREMENT cho bảng `taikhoan`
--
ALTER TABLE `taikhoan`
  MODIFY `IdTaiKhoan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=93;

--
-- AUTO_INCREMENT cho bảng `thanhtoan`
--
ALTER TABLE `thanhtoan`
  MODIFY `IdThanhToan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `chitiethoadon`
--
ALTER TABLE `chitiethoadon`
  ADD CONSTRAINT `chitiethoadon_ibfk_1` FOREIGN KEY (`IdHoaDon`) REFERENCES `hoadon` (`IdHoaDon`),
  ADD CONSTRAINT `chitiethoadon_ibfk_2` FOREIGN KEY (`IdPhieuGhi`) REFERENCES `phieughi` (`IdPhieuGhi`);

--
-- Các ràng buộc cho bảng `chitietthanhtoan`
--
ALTER TABLE `chitietthanhtoan`
  ADD CONSTRAINT `chitietthanhtoan_ibfk_1` FOREIGN KEY (`IdPhieuGhi`) REFERENCES `phieughi` (`IdPhieuGhi`),
  ADD CONSTRAINT `chitietthanhtoan_ibfk_2` FOREIGN KEY (`IdThanhToan`) REFERENCES `thanhtoan` (`IdThanhToan`);

--
-- Các ràng buộc cho bảng `hoadon`
--
ALTER TABLE `hoadon`
  ADD CONSTRAINT `hoadon_ibfk_1` FOREIGN KEY (`IdNhanVien`) REFERENCES `nhanvien` (`IdNhanVien`);

--
-- Các ràng buộc cho bảng `nguoidung`
--
ALTER TABLE `nguoidung`
  ADD CONSTRAINT `nguoidung_ibfk_1` FOREIGN KEY (`IdTaiKhoan`) REFERENCES `taikhoan` (`IdTaiKhoan`);

--
-- Các ràng buộc cho bảng `nhanvien`
--
ALTER TABLE `nhanvien`
  ADD CONSTRAINT `nhanvien_ibfk_1` FOREIGN KEY (`IdTaiKhoan`) REFERENCES `taikhoan` (`IdTaiKhoan`);

--
-- Các ràng buộc cho bảng `phieughi`
--
ALTER TABLE `phieughi`
  ADD CONSTRAINT `phieughi_ibfk_1` FOREIGN KEY (`IdSan`) REFERENCES `san` (`IdSan`),
  ADD CONSTRAINT `phieughi_ibfk_2` FOREIGN KEY (`IdNguoiDung`) REFERENCES `nguoidung` (`IdNguoiDung`);

--
-- Các ràng buộc cho bảng `thanhtoan`
--
ALTER TABLE `thanhtoan`
  ADD CONSTRAINT `thanhtoan_ibfk_1` FOREIGN KEY (`IdNguoiDung`) REFERENCES `nguoidung` (`IdNguoiDung`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
