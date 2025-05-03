-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th4 22, 2025 lúc 10:01 AM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.2.12
create database footballrenting;
use footballrenting;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";



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
(1, 1, '2024-04-15 10:00:00', '8-10', 200000.00);

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
  `Email` varchar(255) DEFAULT NULL,
  `IdTaiKhoan` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `nguoidung`
--

INSERT INTO `nguoidung` (`IdNguoiDung`, `HoTen`, `NgaySinh`, `SDT`, `Email`, `IdTaiKhoan`) VALUES
(1, 'Nguyen Van A', '2000-05-05', 'nguyenvanA@gmail.com', 'Ha Noi', 1);

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
(26, 'Pham Van K', '1994-06-06', '0990123456', '23 Điện Biên Phủ, Vinh', 10, 15500000, 'Quản lý', 'Quản lý sân', '2019-12-01', NULL, 'Dài hạn', 2200000, '741852963', 'Nam', 'TPBank-7418529630', 'Nghỉ phép');

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
(1, '2024-04-16', '8:00 - 9:00', 'Dat', 200000.00, 1, 1);

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
(9, '5', '347 Tân Bình');

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
(12, 'staff10', 'password10', '2025-04-21', 'staff');

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
  MODIFY `IdNhanVien` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT cho bảng `phieughi`
--
ALTER TABLE `phieughi`
  MODIFY `IdPhieuGhi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `san`
--
ALTER TABLE `san`
  MODIFY `IdSan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT cho bảng `taikhoan`
--
ALTER TABLE `taikhoan`
  MODIFY `IdTaiKhoan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

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

