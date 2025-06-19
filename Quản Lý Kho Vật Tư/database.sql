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


INSERT INTO nha_cung_cap (tenNCC, diaChi, soDienThoai) VALUES ('Công ty TNHH Thiên Long', '12 Trần Hưng Đạo, Hà Nội', '0999611975');
INSERT INTO nha_cung_cap (tenNCC, diaChi, soDienThoai) VALUES ('Công ty CP Hoà Bình', '89 Lê Lợi, TP.HCM', '0956193278');
INSERT INTO nha_cung_cap (tenNCC, diaChi, soDienThoai) VALUES ('Công ty TNHH Đại Phát', '45 Nguyễn Văn Cừ, Hải Phòng', '0982338451');
INSERT INTO nha_cung_cap (tenNCC, diaChi, soDienThoai) VALUES ('Công ty CP Hồng Hà', '77 Trần Phú, Đà Nẵng', '0946759640');
INSERT INTO nha_cung_cap (tenNCC, diaChi, soDienThoai) VALUES ('Công ty TNHH Việt Nhật', '33 Hai Bà Trưng, Hà Nội', '0977758054');
INSERT INTO nha_cung_cap (tenNCC, diaChi, soDienThoai) VALUES ('Công ty TNHH Minh Anh', '14 Nguyễn Trãi, TP.HCM', '0991794355');
INSERT INTO nha_cung_cap (tenNCC, diaChi, soDienThoai) VALUES ('Công ty CP Tân Tiến', '65 Điện Biên Phủ, Cần Thơ', '0997314172');
INSERT INTO nha_cung_cap (tenNCC, diaChi, soDienThoai) VALUES ('Công ty TNHH Nam Sơn', '10 Pasteur, Nha Trang', '0972693145');
INSERT INTO nha_cung_cap (tenNCC, diaChi, soDienThoai) VALUES ('Công ty TNHH Ánh Dương', '21 Phan Đình Phùng, Huế', '0915374748');
INSERT INTO nha_cung_cap (tenNCC, diaChi, soDienThoai) VALUES ('Công ty CP Thành Công', '88 Võ Thị Sáu, Biên Hòa', '0931594795');
INSERT INTO nha_cung_cap (tenNCC, diaChi, soDienThoai) VALUES ('Công ty TNHH Trường An', '22 Trường Chinh, Vũng Tàu', '0920338218');
INSERT INTO nha_cung_cap (tenNCC, diaChi, soDienThoai) VALUES ('Công ty CP Đại Hưng', '39 Cách Mạng Tháng Tám, Bình Dương', '0950586786');
INSERT INTO nha_cung_cap (tenNCC, diaChi, soDienThoai) VALUES ('Công ty TNHH Hữu Nghị', '56 Nguyễn Huệ, TP.HCM', '0945619696');
INSERT INTO nha_cung_cap (tenNCC, diaChi, soDienThoai) VALUES ('Công ty TNHH Đại Nam', '90 Lạc Long Quân, Quảng Ninh', '0913556205');
INSERT INTO nha_cung_cap (tenNCC, diaChi, soDienThoai) VALUES ('Công ty CP Đông Dương', '100 Phạm Văn Đồng, Hà Nội', '0919958871');



INSERT INTO nhan_vien (tenNV, chucVu, boPhan) VALUES ('Nguyễn Văn An', 'Thủ kho', 'Kho vật tư');
INSERT INTO nhan_vien (tenNV, chucVu, boPhan) VALUES ('Trần Thị Bình', 'Nhân viên', 'Tài chính');
INSERT INTO nhan_vien (tenNV, chucVu, boPhan) VALUES ('Lê Văn Cường', 'Kế toán', 'Quản trị');
INSERT INTO nhan_vien (tenNV, chucVu, boPhan) VALUES ('Phạm Thị Dung', 'Nhân viên', 'Kho vật tư');
INSERT INTO nhan_vien (tenNV, chucVu, boPhan) VALUES ('Hoàng Văn Em', 'Quản lý', 'Kỹ thuật');
INSERT INTO nhan_vien (tenNV, chucVu, boPhan) VALUES ('Đỗ Thị Hạnh', 'Kế toán', 'Tài chính');
INSERT INTO nhan_vien (tenNV, chucVu, boPhan) VALUES ('Vũ Văn Hải', 'Nhân viên', 'Kỹ thuật');
INSERT INTO nhan_vien (tenNV, chucVu, boPhan) VALUES ('Ngô Thị Hòa', 'Thủ kho', 'Kho vật tư');
INSERT INTO nhan_vien (tenNV, chucVu, boPhan) VALUES ('Bùi Văn Khánh', 'Nhân viên', 'Quản trị');
INSERT INTO nhan_vien (tenNV, chucVu, boPhan) VALUES ('Trịnh Thị Lan', 'Quản lý', 'Tài chính');


INSERT INTO vat_tu (maVT,tenVT, donViTinh, soLuongTon, donGia, maNCC) VALUES ('1','Mỡ bôi trơn', 'cái', 180, 180000, 2);
INSERT INTO vat_tu (maVT,tenVT, donViTinh, soLuongTon, donGia, maNCC) VALUES ('2','Lọc gió', 'cái', 75, 95000, 7);
INSERT INTO vat_tu (maVT,tenVT, donViTinh, soLuongTon, donGia, maNCC) VALUES ('3','Lọc nhớt', 'cái', 120, 110000, 5);
INSERT INTO vat_tu (maVT,tenVT, donViTinh, soLuongTon, donGia, maNCC) VALUES ('4','Má phanh xe du lịch', 'cái', 40, 250000, 3);
INSERT INTO vat_tu (maVT,tenVT, donViTinh, soLuongTon, donGia, maNCC) VALUES ('5','Má phanh xe tải', 'cái', 35, 300000, 6);


INSERT INTO phieu_nhap (ngayNhap, maNCC, maNV) VALUES ('2025-06-01', 1, 1);
INSERT INTO phieu_nhap (ngayNhap, maNCC, maNV) VALUES ('2025-06-02', 3, 5);
INSERT INTO phieu_nhap (ngayNhap, maNCC, maNV) VALUES ('2025-06-03', 2, 7);


INSERT INTO phieu_xuat (ngayXuat, boPhanNhan, maNV) VALUES ('2025-06-16', 'Bộ phận 1', 1);
INSERT INTO phieu_xuat (ngayXuat, boPhanNhan, maNV) VALUES ('2025-06-17', 'Bộ phận 2', 2);
INSERT INTO phieu_xuat (ngayXuat, boPhanNhan, maNV) VALUES ('2025-06-18', 'Bộ phận 3', 3);


