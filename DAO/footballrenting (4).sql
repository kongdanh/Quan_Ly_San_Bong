-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th5 22, 2025 lúc 02:36 AM
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
(1, 'Nguyen Van A', '1990-05-12', '0909123456', '789 Nguyễn Huệ', 5, 10000000, 'Quản lý', 'Tiếp tân', '2023-01-01', 'Chuyên hỗ trợ đặt sân', 'Dài hạn', 1000000, '123456789012', 'Nam', 'Vietcombank-123456', 'Hoạt động'),
(2, 'Tran Thi B', '1992-08-20', '0912123456', '456 Lý Tự Trọng', 6, 9000000, 'Nhân viên', 'Hậu cần', '2023-03-15', 'Phụ trách vệ sinh sân bãi', 'Thời vụ', 500000, '987654321098', 'Nữ', 'ACB-987654', 'Hoạt động'),
(3, 'Le Van C', '1992-11-30', '0923456789', '78 Lê Lợi, Đà Nẵng', 7, 12000000, 'Nhân viên', 'Trọng tài', '2022-06-20', NULL, 'Ngắn hạn', 1500000, '456789123', 'Nam', 'BIDV-4567891234', 'Hoạt động'),
(4, 'Pham Thi D', '1988-02-14', '0934567890', '56 Trần Phú, Nha Trang', 7, 13000000, 'Nhân viên', 'Hậu cần', '2019-09-05', NULL, 'Dài hạn', 1800000, '789123456', 'Nữ', 'MB Bank-7891234567', 'Nghỉ việc'),
(5, 'Hoang Van E', '1993-07-25', '0945678901', '89 Nguyễn Trãi, Huế', 8, 11000000, 'Nhân viên', 'Trọng tài', '2021-11-11', NULL, 'Trung hạn', 1200000, '321654987', 'Nam', 'Vietinbank-3216549870', 'Hoạt động'),
(6, 'Bui Thi F', '1996-04-18', '0956789012', '12 Phạm Văn Đồng, Hà Nội', 11, 9000000, 'Nhân viên', 'Thu ngân', '2023-02-25', NULL, 'Ngắn hạn', 800000, '654987321', 'Nữ', 'Agribank-6549873210', 'Nghỉ phép'),
(7, 'Nguyen Van G', '1991-09-09', '0967890123', '34 Hùng Vương, Hải Phòng', 5, 16000000, 'Quản lý', 'Quản lý sân', '2018-07-30', NULL, 'Dài hạn', 2500000, '147258369', 'Nam', 'Sacombank-1472583690', 'Hoạt động'),
(8, 'Tran Van H', '1989-12-12', '0978901234', '67 Lê Đại Hành, Đà Lạt', 8, 14000000, 'Nhân viên', 'Hậu cần', '2020-04-10', NULL, 'Trung hạn', 1700000, '258369147', 'Nam', 'VPBank-2583691470', 'Nghỉ việc');

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
(1, 'tranvanb', 'matkhau123', '2025-04-01', 'blocked'),
(2, 'lethic', 'matkhau456', '2025-04-01', 'user'),
(3, 'nguyenvand', 'matkhau789', '2025-04-01', 'user'),
(5, 'admin1', 'pass2', '2024-01-02', 'admin'),
(6, 'staff1', 'password1', '2025-04-21', 'staff'),
(7, 'staff2', 'password2', '2025-04-21', 'staff'),
(8, 'staff3', 'password3', '2025-04-21', 'staff'),
(9, 'staff4', 'password4', '2025-04-21', 'staff'),
(10, 'staff5', 'password5', '2025-04-21', 'staff'),
(11, 'staff6', 'password6', '2025-04-21', 'staff'),
(12, 'staff7', 'password7', '2025-04-21', 'staff'),
(13, 'staff8', 'password8', '2025-04-21', 'staff'),
(14, 'staff9', 'password9', '2025-04-21', 'staff'),
(15, 'staff10', 'password10', '2025-04-21', 'staff'),
(16, 'user1', 'pw1', '2025-02-15', 'user'),
(17, 'user2', 'pw2', '2025-01-05', 'user'),
(18, 'user3', 'pw3', '2025-01-20', 'user'),
(19, 'user4', 'pw4', '2025-03-05', 'user'),
(20, 'user5', 'pw5', '2025-03-25', 'user');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `nhanvien`
--
ALTER TABLE `nhanvien`
  ADD PRIMARY KEY (`IdNhanVien`),
  ADD KEY `IdTaiKhoan` (`IdTaiKhoan`);

--
-- Chỉ mục cho bảng `taikhoan`
--
ALTER TABLE `taikhoan`
  ADD PRIMARY KEY (`IdTaiKhoan`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `nhanvien`
--
ALTER TABLE `nhanvien`
  MODIFY `IdNhanVien` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT cho bảng `taikhoan`
--
ALTER TABLE `taikhoan`
  MODIFY `IdTaiKhoan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `nhanvien`
--
ALTER TABLE `nhanvien`
  ADD CONSTRAINT `nhanvien_ibfk_1` FOREIGN KEY (`IdTaiKhoan`) REFERENCES `taikhoan` (`IdTaiKhoan`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
