DROP DATABASE IF EXISTS kho_vattu;
CREATE DATABASE kho_vattu;
USE kho_vattu;

-- Bảng nhân viên
CREATE TABLE nhan_vien (
    maNV INT AUTO_INCREMENT PRIMARY KEY,
    tenNV VARCHAR(100),
    chucVu VARCHAR(50),
    boPhan VARCHAR(100)
);

-- Bảng nhà cung cấp
CREATE TABLE nha_cung_cap (
    maNCC INT AUTO_INCREMENT PRIMARY KEY,
    tenNCC VARCHAR(100),
    diaChi VARCHAR(200),
    soDienThoai VARCHAR(20)
);

-- Bảng vật tư
CREATE TABLE vat_tu (
    maVT INT AUTO_INCREMENT PRIMARY KEY,
    tenVT VARCHAR(100),
    donViTinh VARCHAR(20),
    soLuongTon INT DEFAULT 0,
    donGia DECIMAL(12, 2),
    maNCC INT,
    FOREIGN KEY (maNCC) REFERENCES nha_cung_cap(maNCC)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Phiếu nhập
CREATE TABLE phieu_nhap (
    maPN INT AUTO_INCREMENT PRIMARY KEY,
    ngayNhap DATE,
    maNCC INT,
    maNV INT,
    FOREIGN KEY (maNCC) REFERENCES nha_cung_cap(maNCC)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (maNV) REFERENCES nhan_vien(maNV)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Chi tiết phiếu nhập
CREATE TABLE chi_tiet_phieu_nhap (
    maPN INT,
    maVT INT,
    soLuong INT,
    donGia DECIMAL(12, 2),
    PRIMARY KEY (maPN, maVT),
    FOREIGN KEY (maPN) REFERENCES phieu_nhap(maPN)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (maVT) REFERENCES vat_tu(maVT)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

-- Phiếu xuất
CREATE TABLE phieu_xuat (
    maPX INT AUTO_INCREMENT PRIMARY KEY,
    ngayXuat DATE,
    boPhanNhan VARCHAR(100),
    maNV INT,
    FOREIGN KEY (maNV) REFERENCES nhan_vien(maNV)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Chi tiết phiếu xuất
CREATE TABLE chi_tiet_phieu_xuat (
    maPX INT,
    maVT INT,
    soLuong INT,
    donGia DECIMAL(12, 2),
    PRIMARY KEY (maPX, maVT),
    FOREIGN KEY (maPX) REFERENCES phieu_xuat(maPX)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (maVT) REFERENCES vat_tu(maVT)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

-- Lịch sử giao dịch
CREATE TABLE lich_su_giao_dich (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngayGiaoDich DATE,
    loaiGiaoDich ENUM('Nhập', 'Xuất'),
    maVT INT,
    soLuong INT,
    maNV INT NULL,
    ghiChu TEXT,
    FOREIGN KEY (maVT) REFERENCES vat_tu(maVT)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (maNV) REFERENCES nhan_vien(maNV)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
