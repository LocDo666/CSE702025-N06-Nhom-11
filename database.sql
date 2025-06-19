CREATE DATABASE IF NOT EXISTS kho_vattu;
/*  drop database kho_vattu; */
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
