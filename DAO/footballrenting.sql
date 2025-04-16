-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th4 16, 2025 lúc 07:03 PM
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
(1, 1, '2024-04-15 10:00:00', '08:00 - 09:00', 200000.00);

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
(1, 1, '2024-04-16', '08:00 - 09:00', 200000.00);

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
(1, '2024-04-16', 200000.00, 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `nguoidung`
--

CREATE TABLE `nguoidung` (
  `IdNguoiDung` int(11) NOT NULL,
  `HoTen` varchar(100) DEFAULT NULL,
  `NgaySinh` date DEFAULT NULL,
  `SDT` varchar(15) DEFAULT NULL,
  `DiaChi` varchar(255) DEFAULT NULL,
  `IdTaiKhoan` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `nguoidung`
--

INSERT INTO `nguoidung` (`IdNguoiDung`, `HoTen`, `NgaySinh`, `SDT`, `DiaChi`, `IdTaiKhoan`) VALUES
(1, 'Nguyen Van A', '2000-05-05', '0901234567', 'Ha Noi', 1);

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
  `IdTaiKhoan` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `nhanvien`
--

INSERT INTO `nhanvien` (`IdNhanVien`, `HoTen`, `NgaySinh`, `SDT`, `DiaChi`, `IdTaiKhoan`) VALUES
(1, 'Tran Thi B', '1995-08-08', '0912345678', 'Da Nang', 2);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `phieughi`
--

CREATE TABLE `phieughi` (
  `IdPhieuGhi` int(11) NOT NULL,
  `BatDau` datetime DEFAULT NULL,
  `KetThuc` datetime DEFAULT NULL,
  `TrangThai` varchar(20) DEFAULT NULL,
  `GiaTien` decimal(10,2) DEFAULT NULL,
  `IdSan` int(11) DEFAULT NULL,
  `IdNguoiDung` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `phieughi`
--

INSERT INTO `phieughi` (`IdPhieuGhi`, `BatDau`, `KetThuc`, `TrangThai`, `GiaTien`, `IdSan`, `IdNguoiDung`) VALUES
(1, '2024-04-16 08:00:00', '2024-04-16 09:00:00', 'Dat', 200000.00, 1, 1);

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
(1, '5 vs 5', '123 Le Loi'),
(2, '7 vs 7', '456 Tran Phu');

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
(2, 'admin1', 'pass2', '2024-01-02', 'admin');

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
(1, '2024-04-16', 200000.00, 'Tien mat', 'Da thanh toan', 1);

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
  MODIFY `IdHoaDon` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `nguoidung`
--
ALTER TABLE `nguoidung`
  MODIFY `IdNguoiDung` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `nhanvien`
--
ALTER TABLE `nhanvien`
  MODIFY `IdNhanVien` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `phieughi`
--
ALTER TABLE `phieughi`
  MODIFY `IdPhieuGhi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `san`
--
ALTER TABLE `san`
  MODIFY `IdSan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT cho bảng `taikhoan`
--
ALTER TABLE `taikhoan`
  MODIFY `IdTaiKhoan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT cho bảng `thanhtoan`
--
ALTER TABLE `thanhtoan`
  MODIFY `IdThanhToan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

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
