CREATE DATABASE IF NOT EXISTS kho_vattu;
USE kho_vattu;

CREATE TABLE nha_cung_cap (
    maNCC INT PRIMARY KEY AUTO_INCREMENT,
    tenNCC VARCHAR(100),
    diaChi VARCHAR(255),
    soDienThoai VARCHAR(20)
);

CREATE TABLE vat_tu (
    maVT INT PRIMARY KEY AUTO_INCREMENT,
    tenVT VARCHAR(100),
    donViTinh VARCHAR(50),
    soLuongTon INT,
    donGia DECIMAL(15,2),
    maNCC INT,
    FOREIGN KEY (maNCC) REFERENCES nha_cung_cap(maNCC)
);
CREATE TABLE nhan_vien (
    maNV INT PRIMARY KEY AUTO_INCREMENT,
    tenNV VARCHAR(100),
    chucVu VARCHAR(50),
    boPhan VARCHAR(100)
);

CREATE TABLE phieu_nhap (
    maPN INT PRIMARY KEY AUTO_INCREMENT,
    ngayNhap DATE,
    maNCC INT,
    maNV INT,
    FOREIGN KEY (maNCC) REFERENCES nha_cung_cap(maNCC),
    FOREIGN KEY (maNV) REFERENCES nhan_vien(maNV)
);

CREATE TABLE chi_tiet_phieu_nhap (
    maPN INT,
    maVT INT,
    soLuong INT,
    donGia DECIMAL(15,2),
    PRIMARY KEY (maPN, maVT),
    FOREIGN KEY (maPN) REFERENCES phieu_nhap(maPN),
    FOREIGN KEY (maVT) REFERENCES vat_tu(maVT)
);

CREATE TABLE phieu_xuat (
    maPX INT PRIMARY KEY AUTO_INCREMENT,
    ngayXuat DATE,
    boPhanNhan VARCHAR(100),
    maNV INT,
    FOREIGN KEY (maNV) REFERENCES nhan_vien(maNV)
);

CREATE TABLE chi_tiet_phieu_xuat (
    maPX INT,
    maVT INT,
    soLuong INT,
    donGia DECIMAL(15,2),
    PRIMARY KEY (maPX, maVT),
    FOREIGN KEY (maPX) REFERENCES phieu_xuat(maPX),
    FOREIGN KEY (maVT) REFERENCES vat_tu(maVT)
);



CREATE TABLE lich_su_giao_dich (
    ngayGiaoDich DATE,
    loaiGiaoDich VARCHAR(50),
    maVT INT,
    soLuong INT,
    maNV INT,
    ghiChu VARCHAR(255),
    FOREIGN KEY (maVT) REFERENCES vat_tu(maVT),
    FOREIGN KEY (maNV) REFERENCES nhan_vien(maNV)
);

SELECT * FROM kho_vattu.nha_cung_cap;

/* Inserting data  */

INSERT INTO nha_cung_cap (tenNCC, diaChi, soDienThoai) VALUES
('Công ty TNHH Minh Phát', '123 Lê Lợi, Q1, TP.HCM', '0909123456'),
('Công ty CP Thiết bị An Khang', '456 Trần Hưng Đạo, Q5, TP.HCM', '0912345678'),
('Công ty TNHH Phú Hưng', '789 Nguyễn Trãi, Q10, TP.HCM', '0938123456');

INSERT INTO vat_tu (tenVT, donViTinh, soLuongTon, donGia, maNCC) VALUES
('Đinh vít 5cm', 'Hộ	p', 500, 25000, 1),
('Sơn dầu trắng', 'Lon', 200, 120000, 2),
('Ống nước PVC 90cm', 'Cây', 150, 35000, 1),
('Xi măng Hà Tiên', 'Bao', 100, 75000, 3),
('Thép cuộn 8mm', 'Cuộn', 80, 1800000, 2);

INSERT INTO nhan_vien (tenNV, chucVu, boPhan) VALUES
('Nguyễn Văn An', 'Thủ kho', 'Kho'),
('Trần Thị Bình', 'Kế toán', 'Tài chính'),
('Lê Văn Cường', 'Nhân viên nhập hàng', 'Kho'),
('Phạm Thị Dung', 'Quản lý', 'Hành chính'),
('Đỗ Minh Tuấn', 'Nhân viên xuất hàng', 'Kho');

INSERT INTO phieu_nhap (ngayNhap, maNCC, maNV) VALUES
('2025-06-01', 1, 3),
('2025-06-02', 2, 3),
('2025-06-03', 3, 3);

INSERT INTO chi_tiet_phieu_nhap (maPN, maVT, soLuong, donGia) VALUES
(1, 1, 100, 24000),
(1, 3, 50, 34000),
(2, 2, 30, 115000),
(2, 5, 10, 1750000),
(3, 4, 20, 74000);

INSERT INTO phieu_xuat (ngayXuat, boPhanNhan, maNV) VALUES
('2025-06-04', 'Xây dựng', 5),
('2025-06-05', 'Bảo trì', 5);

INSERT INTO chi_tiet_phieu_xuat (maPX, maVT, soLuong, donGia) VALUES
(1, 1, 50, 25000),
(1, 4, 10, 75000),
(2, 2, 5, 120000),
(2, 3, 10, 35000);

INSERT INTO lich_su_giao_dich (ngayGiaoDich, loaiGiaoDich, maVT, soLuong, maNV, ghiChu) VALUES
('2025-06-01', 'Nhập', 1, 100, 3, 'Nhập lô đầu tiên từ nhà cung cấp Minh Phát'),
('2025-06-02', 'Nhập', 2, 30, 3, 'Nhập thêm sơn cho công trình A'),
('2025-06-04', 'Xuất', 1, 50, 5, 'Xuất cho bộ phận xây dựng'),
('2025-06-05', 'Xuất', 2, 5, 5, 'Xuất cho bộ phận bảo trì');




