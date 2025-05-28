-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th5 28, 2025 lúc 04:44 PM
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
-- Cấu trúc bảng cho bảng `hoadon`
--

CREATE TABLE `hoadon` (
  `IdHoaDon` int(11) NOT NULL,
  `Ngay` date DEFAULT NULL,
  `TongTien` decimal(10,2) DEFAULT NULL,
  `PhuongThuc` varchar(50) DEFAULT NULL,
  `TrangThai` int(11) DEFAULT 0,
  `IdNhanVien` int(11) DEFAULT NULL,
  `IdNguoiDung` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `hoadon`
--

INSERT INTO `hoadon` (`IdHoaDon`, `Ngay`, `TongTien`, `PhuongThuc`, `TrangThai`, `IdNhanVien`, `IdNguoiDung`, `status`) VALUES
(1, '2025-04-15', 200000.00, 'Chuyển khoản', 2, 1, 1, 1),
(2, '2025-04-14', 250000.00, 'Tiền mặt', 2, 2, 2, 1),
(3, '2025-04-13', 300000.00, 'Tiền mặt', 2, 2, 3, 1),
(4, '2025-04-12', 150000.00, 'Chuyển khoản', 2, 4, 2, 1),
(5, '2025-05-22', 400000.00, 'Tiền mặt', 2, 6, 2, 1),
(6, '2025-02-15', 450000.00, 'Chuyển khoản', 0, 3, 1, 1),
(7, '2025-01-10', 350000.00, 'Tiền mặt', 0, 1, 2, 1),
(8, '2025-01-20', 700000.00, 'Chuyển khoản', 0, 4, 3, 1),
(9, '2025-03-05', 500000.00, 'Tiền mặt', 0, 2, 1, 1),
(10, '2025-03-15', 650000.00, 'Chuyển khoản', 1, 7, 2, 1),
(11, '2025-03-25', 800000.00, 'Tiền mặt', 2, 5, 3, 1),
(12, '2025-05-22', 200000.00, 'Tiền mặt', 2, NULL, 2, 1);

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
  `IdTaiKhoan` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `nguoidung`
--

INSERT INTO `nguoidung` (`IdNguoiDung`, `HoTen`, `NgaySinh`, `SDT`, `Email`, `IdTaiKhoan`, `status`) VALUES
(1, 'Tran Van B', '2000-05-11', '0911002200', 'tranvanb@example.com', 1, 1),
(2, 'Le Thi C', '2001-03-22', '0933344556', 'lethic@example.com', 2, 1),
(3, 'Nguyen Van D', '1997-09-10', '0909988776', 'nguyenvand@example.com', 3, 1),
(5, 'Pham Thi E', '1995-05-15', '0987654321', 'phamthie@example.com', 16, 1),
(6, 'Vo Van F', '1998-11-30', '0977123456', 'vovanf@example.com', 17, 1),
(7, 'Tran Thi G', '2000-07-22', '0918234567', 'tranthig@example.com', 18, 1),
(8, 'Le Van H', '1993-02-18', '0901122334', 'levanh@example.com', 19, 1),
(9, 'Nguyen Thi K', '1999-12-05', '0934455667', 'nguyenthik@example.com', 20, 1),
(10, 'tuilaai', NULL, '0123123123', 'danhc@gmail.com', 30, 1);

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
  `hoatdong` varchar(100) DEFAULT NULL,
  `gmail` varchar(100) DEFAULT NULL,
  `status` int(11) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `nhanvien`
--

INSERT INTO `nhanvien` (`IdNhanVien`, `HoTen`, `NgaySinh`, `SDT`, `DiaChi`, `IdTaiKhoan`, `luong`, `chuc_vu`, `vi_tri`, `ngayvaolam`, `mota`, `hopdong`, `phucap`, `cccd`, `gioitinh`, `nganhang`, `hoatdong`, `gmail`, `status`) VALUES
(1, 'Nguyen Van A', '1990-05-12', '0909123456', '789 Nguyễn Huệ', 5, 10000000, 'Quản lý', 'Tiếp tân', '2023-01-01', 'Chuyên hỗ trợ đặt sân', 'Dài hạn', 1000000, '123456789012', 'Nam', 'Vietcombank-123456', 'Hoạt động', 'abc@gmail.com', 1),
(2, 'Tran Thi B', '1992-08-20', '0912123456', '456 Lý Tự Trọng', 6, 9000000, 'Nhân viên', 'Hậu cần', '2023-03-15', 'Phụ trách vệ sinh sân bãi', 'Thời vụ', 500000, '987654321098', 'Nữ', 'ACB-987654', 'Hoạt động', 'nhanvien2@example.com', 1),
(3, 'Le Van C', '1992-11-30', '0923456789', '78 Lê Lợi, Đà Nẵng', 7, 12000000, 'Nhân viên', 'Trọng tài', '2022-06-20', NULL, 'Ngắn hạn', 1500000, '456789123', 'Nam', 'BIDV-4567891234', 'Hoạt động', 'hoang.le123@gmail.com', 1),
(4, 'Pham Thi D', '1988-02-14', '0934567890', '56 Trần Phú, Nha Trang', 7, 13000000, 'Nhân viên', 'Hậu cần', '2019-09-05', NULL, 'Dài hạn', 1800000, '789123456', 'Nữ', 'MB Bank-7891234567', 'Nghỉ việc', 'minh.tran456@yahoo.com', 1),
(5, 'Hoang Van E', '1993-07-25', '0945678901', '89 Nguyễn Trãi, Huế', 8, 11000000, 'Nhân viên', 'Trọng tài', '2021-11-11', NULL, 'Trung hạn', 1200000, '321654987', 'Nam', 'Vietinbank-3216549870', 'Hoạt động', 'hien.nguyen789@outlook.com', 1),
(6, 'Bui Thi F', '1996-04-18', '0956789012', '12 Phạm Văn Đồng, Hà Nội', 11, 9000000, 'Nhân viên', 'Thu ngân', '2023-02-25', NULL, 'Ngắn hạn', 800000, '654987321', 'Nữ', 'Agribank-6549873210', 'Nghỉ phép', 'tuan.pham2025@gmail.com', 1),
(7, 'Nguyen Van G', '1991-09-09', '0967890123', '34 Hùng Vương, Hải Phòng', 5, 16000000, 'Quản lý', 'Quản lý sân', '2018-07-30', NULL, 'Dài hạn', 2500000, '147258369', 'Nam', 'Sacombank-1472583690', 'Hoạt động', 'linh.dang321@gmail.com', 1),
(8, 'Tran Van H', '1989-12-12', '0978901234', '67 Lê Đại Hành, Đà Lạt', 8, 14000000, 'Nhân viên', 'Hậu cần', '2020-04-10', NULL, 'Trung hạn', 1700000, '258369147', 'Nam', 'VPBank-2583691470', 'Nghỉ việc', 'nam.vo147@yahoo.com', 1),
(11, 'tuilaai', '2005-01-05', '0123123123', '123a', 21, 123123, 'Nhân viên', 'Nhân viên lễ tân / tiếp tân', '2025-05-09', '', 'Dài hạn', 123, '123123123123', 'Nam', '123', 'Hoạt động', 'nga.nguyen654@gmail.com', 1),
(12, 'tuilaai', '2005-01-05', '0123123123', '123a', 22, 123123, 'Nhân viên', 'Nhân viên lễ tân / tiếp tân', '2025-05-09', '', 'Dài hạn', 123, '123123123123', 'Nam', '123', 'Hoạt động', 'trung.bui159@outlook.com', 1),
(13, '123', '2005-01-13', '0123123123', '123', 23, 123, 'Nhân viên', 'Nhân viên kỹ thuật / bảo trì', '2025-05-22', '123', 'Dài hạn', 123, '123', 'Nam', '123', 'Hoạt động', NULL, 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `phieughi`
--

CREATE TABLE `phieughi` (
  `IdPhieuGhi` int(11) NOT NULL,
  `Ngay` datetime DEFAULT NULL,
  `KhungGio` varchar(20) DEFAULT NULL,
  `GiaTien` decimal(10,2) DEFAULT NULL,
  `IdSan` int(11) DEFAULT NULL,
  `IdHoaDon` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `phieughi`
--

INSERT INTO `phieughi` (`IdPhieuGhi`, `Ngay`, `KhungGio`, `GiaTien`, `IdSan`, `IdHoaDon`, `status`) VALUES
(1, '2025-04-15 08:00:00', '8:00 - 10:00', 200000.00, 1, 1, 1),
(2, '2025-04-14 10:00:00', '10:00 - 12:00', 250000.00, 2, 2, 1),
(3, '2025-04-13 14:00:00', '14:00 - 16:00', 300000.00, 3, 3, 1),
(4, '2025-05-21 00:00:00', '16:00 - 18:00', 150000.00, 1, 4, 1),
(5, '2025-05-22 00:00:00', '06:00-08:00', 400000.00, 1, 5, 1),
(6, '2025-02-15 08:00:00', '08:00 - 10:00', 450000.00, 1, 6, 1),
(7, '2025-01-05 10:00:00', '10:00 - 12:00', 350000.00, 2, 7, 1),
(8, '2025-01-20 14:00:00', '14:00 - 16:00', 700000.00, 3, 8, 1),
(9, '2025-03-05 16:00:00', '16:00 - 18:00', 500000.00, 1, 9, 1),
(10, '2025-03-15 18:00:00', '18:00 - 20:00', 650000.00, 2, 10, 1),
(11, '2025-03-25 20:00:00', '20:00 - 22:00', 800000.00, 3, 11, 1),
(12, '2025-05-22 00:00:00', '10:40-11:40', 200000.00, 1, 12, 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `san`
--

CREATE TABLE `san` (
  `IdSan` int(11) NOT NULL,
  `CoSan` varchar(20) DEFAULT NULL,
  `DiaChi` varchar(255) DEFAULT NULL,
  `HinhAnh` varchar(255) DEFAULT NULL,
  `SoSan` int(11) DEFAULT NULL,
  `MoTa` text DEFAULT 'Chưa có mô tả',
  `TrangThai` tinyint(4) DEFAULT 1,
  `GiaSan` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `san`
--

INSERT INTO `san` (`IdSan`, `CoSan`, `DiaChi`, `HinhAnh`, `SoSan`, `MoTa`, `TrangThai`, `GiaSan`, `status`) VALUES
(1, '11', '123 Lê Lợi, Quận 1', 'asset/san1_1.jpg', 1, 'Chưa có mô tả', 1, 200000, 0),
(2, '7', '456 Trần Phú, Quận 5', 'asset/san1_2.jpg', 2, 'Chưa có mô tả', 1, 300000, 0),
(3, '11', '789 Nguyễn Huệ, Quận 1', 'asset/san4_2.jpg', 3, 'Chưa có mô tả', 1, 350000, 1),
(11, '5', 'Số 12, Quận Tân Bình', NULL, 1, 'Sân cỏ nhân tạo aaa', 1, 300000, 1),
(12, '5', 'Số 45, Huyện Bình Chánh', 'san1_2.jpg', 2, 'Sân mới đẹp', 1, 300000, 1),
(13, '7', 'Số 78, Quận Gò Vấp', 'san2_1.jpg', 1, 'Sân có đèn chiếu sáng', 1, 450000, 1),
(14, '7', 'Số 32, Quận 7', 'san3_2.jpg', 2, 'Chưa có mô tả', 1, 450000, 0),
(15, '11', 'Số 90, Quận Thủ Đức', 'san4_1.jpg', 1, 'Sân tiêu chuẩn quốc gia', 1, 700000, 1),
(16, '5', 'tuilaai', 'asset/default.jpg', 2, 'tuila1congdan', 1, 2147483647, 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `taikhoan`
--

CREATE TABLE `taikhoan` (
  `IdTaiKhoan` int(11) NOT NULL,
  `TenTaiKhoan` varchar(50) DEFAULT NULL,
  `MatKhau` varchar(255) DEFAULT NULL,
  `NgayTao` date DEFAULT NULL,
  `AccType` varchar(20) DEFAULT NULL,
  `status` int(11) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `taikhoan`
--

INSERT INTO `taikhoan` (`IdTaiKhoan`, `TenTaiKhoan`, `MatKhau`, `NgayTao`, `AccType`, `status`) VALUES
(1, 'tranvanb', 'matkhau123', '2025-04-01', 'blocked', 1),
(2, 'lethic', 'matkhau456', '2025-04-01', 'user', 1),
(3, 'nguyenvand', 'matkhau789', '2025-04-01', 'user', 1),
(5, 'admin1', 'pass2', '2024-01-02', 'admin', 1),
(6, 'staff1', 'password1', '2025-04-21', 'staff', 1),
(7, 'staff2', 'password2', '2025-04-21', 'staff', 1),
(8, 'staff3', 'password3', '2025-04-21', 'staff', 1),
(9, 'staff4', 'password4', '2025-04-21', 'staff', 1),
(10, 'staff5', 'password5', '2025-04-21', 'staff', 1),
(11, 'staff6', 'password6', '2025-04-21', 'staff', 1),
(12, 'staff7', 'password7', '2025-04-21', 'staff', 1),
(13, 'staff8', 'password8', '2025-04-21', 'staff', 1),
(14, 'staff9', 'password9', '2025-04-21', 'staff', 1),
(15, 'staff10', 'password10', '2025-04-21', 'staff', 1),
(16, 'user1', 'pw1', '2025-02-15', 'user', 1),
(17, 'user2', 'pw2', '2025-01-05', 'user', 1),
(18, 'user3', 'pw3', '2025-01-20', 'user', 1),
(19, 'user4', 'pw4', '2025-03-05', 'user', 1),
(20, 'user5', 'pw5', '2025-03-25', 'user', 1),
(21, 'tuilaai', '1231231231', '2025-05-22', 'Nhân viên', 1),
(22, 'tuilaai', '1231231231', '2025-05-22', 'Nhân viên', 1),
(23, '123', '123', '2025-05-22', 'Nhân viên', 1),
(24, '123', '123', '2025-05-22', 'Nhân viên', 1),
(25, '123', '123', '2025-05-22', 'Nhân viên', 1),
(26, '123', '123', '2025-05-22', 'Nhân viên', 1),
(27, '123123', '123123', '2025-05-22', 'Nhân viên', 1),
(28, '123', '123', '2025-05-22', 'Nhân viên', 1),
(29, '123', '123', '2025-05-22', 'Nhân viên', 1),
(30, 'abc', '123123', '2025-05-28', 'user', 1);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `hoadon`
--
ALTER TABLE `hoadon`
  ADD PRIMARY KEY (`IdHoaDon`),
  ADD KEY `IdNhanVien` (`IdNhanVien`),
  ADD KEY `IdNguoiDung` (`IdNguoiDung`);

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
  ADD KEY `IdHoaDon` (`IdHoaDon`);

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
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `hoadon`
--
ALTER TABLE `hoadon`
  MODIFY `IdHoaDon` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT cho bảng `nguoidung`
--
ALTER TABLE `nguoidung`
  MODIFY `IdNguoiDung` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT cho bảng `nhanvien`
--
ALTER TABLE `nhanvien`
  MODIFY `IdNhanVien` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT cho bảng `phieughi`
--
ALTER TABLE `phieughi`
  MODIFY `IdPhieuGhi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT cho bảng `san`
--
ALTER TABLE `san`
  MODIFY `IdSan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT cho bảng `taikhoan`
--
ALTER TABLE `taikhoan`
  MODIFY `IdTaiKhoan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `hoadon`
--
ALTER TABLE `hoadon`
  ADD CONSTRAINT `hoadon_ibfk_1` FOREIGN KEY (`IdNhanVien`) REFERENCES `nhanvien` (`IdNhanVien`),
  ADD CONSTRAINT `hoadon_ibfk_2` FOREIGN KEY (`IdNguoiDung`) REFERENCES `nguoidung` (`IdNguoiDung`);

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
  ADD CONSTRAINT `phieughi_ibfk_2` FOREIGN KEY (`IdHoaDon`) REFERENCES `hoadon` (`IdHoaDon`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
