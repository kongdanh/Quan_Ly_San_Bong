CREATE DATABASE FootBallRenting
USE FootBallRenting

-- 1. TaiKhoan
CREATE TABLE TaiKhoan (
    IdTaiKhoan INT IDENTITY(1,1) PRIMARY KEY,  -- Auto-incremented primary key
    TenTaiKhoan NVARCHAR(50),
    MatKhau NVARCHAR(255),
    NgayTao DATE,
    AccType NVARCHAR(20)
);

-- Example data
INSERT INTO TaiKhoan (TenTaiKhoan, MatKhau, NgayTao, AccType) VALUES 
('user1', 'pass1', '2024-01-01', 'user'),
('admin1', 'pass2', '2024-01-02', 'admin');

-- 2. NguoiDung
CREATE TABLE NguoiDung (
    IdNguoiDung INT IDENTITY(1,1) PRIMARY KEY,  -- Auto-incremented primary key
    HoTen NVARCHAR(100),
    NgaySinh DATE,
    SDT NVARCHAR(15),
    DiaChi NVARCHAR(255),
    IdTaiKhoan INT FOREIGN KEY REFERENCES TaiKhoan(IdTaiKhoan)
);

-- Example data
INSERT INTO NguoiDung (HoTen, NgaySinh, SDT, DiaChi, IdTaiKhoan) VALUES 
('Nguyen Van A', '2000-05-05', '0901234567', 'Ha Noi', 1);

-- 3. NhanVien
CREATE TABLE NhanVien (
    IdNhanVien INT IDENTITY(1,1) PRIMARY KEY,  -- Auto-incremented primary key
    HoTen NVARCHAR(100),
    NgaySinh DATE,
    SDT NVARCHAR(15),
    DiaChi NVARCHAR(255),
    IdTaiKhoan INT FOREIGN KEY REFERENCES TaiKhoan(IdTaiKhoan)
);

-- Example data
INSERT INTO NhanVien (HoTen, NgaySinh, SDT, DiaChi, IdTaiKhoan) VALUES 
('Tran Thi B', '1995-08-08', '0912345678', 'Da Nang', 2);

-- 4. San
CREATE TABLE San (
    IdSan INT IDENTITY(1,1) PRIMARY KEY,  -- Auto-incremented primary key
    CoSan NVARCHAR(20),
    DiaChi NVARCHAR(255)
);

-- Example data
INSERT INTO San (CoSan, DiaChi) VALUES 
('5 vs 5', '123 Le Loi'),
('7 vs 7', '456 Tran Phu');

-- 5. PhieuGhi
CREATE TABLE PhieuGhi (
    IdPhieuGhi INT IDENTITY(1,1) PRIMARY KEY,  -- Auto-incremented primary key
    BatDau DATETIME,
    KetThuc DATETIME,
    TrangThai NVARCHAR(20),
    GiaTien DECIMAL(10, 2),
    IdSan INT FOREIGN KEY REFERENCES San(IdSan),
    IdNguoiDung INT FOREIGN KEY REFERENCES NguoiDung(IdNguoiDung)
);

-- Example data
INSERT INTO PhieuGhi (BatDau, KetThuc, TrangThai, GiaTien, IdSan, IdNguoiDung) VALUES 
('2024-04-16 08:00', '2024-04-16 09:00', 'Dat', 200000, 1, 1);

-- 6. HoaDon
CREATE TABLE HoaDon (
    IdHoaDon INT IDENTITY(1,1) PRIMARY KEY,  -- Auto-incremented primary key
    Ngay DATE,
    TongTien DECIMAL(10, 2),
    IdNhanVien INT FOREIGN KEY REFERENCES NhanVien(IdNhanVien)
);

-- Example data
INSERT INTO HoaDon (Ngay, TongTien, IdNhanVien) VALUES 
('2024-04-16', 200000, 1);

-- 7. ChiTietHoaDon
CREATE TABLE ChiTietHoaDon (
    IdHoaDon INT, 
    IdPhieuGhi INT,
    ThoiDiemDat DATETIME,
    KhungGio NVARCHAR(50),
    Tien DECIMAL(10,2),
    PRIMARY KEY (IdHoaDon, IdPhieuGhi),
    FOREIGN KEY (IdHoaDon) REFERENCES HoaDon(IdHoaDon),
    FOREIGN KEY (IdPhieuGhi) REFERENCES PhieuGhi(IdPhieuGhi)
);

-- Example data
INSERT INTO ChiTietHoaDon (IdHoaDon, IdPhieuGhi, ThoiDiemDat, KhungGio, Tien) VALUES 
(1, 1, '2024-04-15 10:00', '08:00 - 09:00', 200000);

-- 8. ThanhToan
CREATE TABLE ThanhToan (
    IdThanhToan INT IDENTITY(1,1) PRIMARY KEY,  -- Auto-incremented primary key
    Ngay DATE,
    TongTien DECIMAL(10, 2),
    PhuongThuc NVARCHAR(50),
    TrangThai NVARCHAR(20),
    IdNguoiDung INT FOREIGN KEY REFERENCES NguoiDung(IdNguoiDung)
);
-- Example data
INSERT INTO ThanhToan (Ngay, TongTien, PhuongThuc, TrangThai, IdNguoiDung) VALUES 
('2024-04-16', 200000, 'Tien mat', 'Da thanh toan', 1);

-- 9. ChiTietThanhToan
CREATE TABLE ChiTietThanhToan (
    IdPhieuGhi INT, 
    IdThanhToan INT,
    NgayThue DATE,
    KhungGioThue NVARCHAR(50),
    Tien DECIMAL(10,2),
    PRIMARY KEY (IdPhieuGhi, IdThanhToan),
    FOREIGN KEY (IdPhieuGhi) REFERENCES PhieuGhi(IdPhieuGhi),
    FOREIGN KEY (IdThanhToan) REFERENCES ThanhToan(IdThanhToan)
);

-- Example data
INSERT INTO ChiTietThanhToan (IdPhieuGhi, IdThanhToan, NgayThue, KhungGioThue, Tien) VALUES 
(1, 1, '2024-04-16', '08:00 - 09:00', 200000);





SELECT * FROM TaiKhoan;
SELECT * FROM NguoiDung;
SELECT * FROM NhanVien;
SELECT * FROM San;
SELECT * FROM PhieuGhi;
SELECT * FROM HoaDon;
SELECT * FROM ChiTietHoaDon;
SELECT * FROM ChiTietThanhToan;
SELECT * FROM ThanhToan;
