from database.db_connector import get_connection

def get_phieu_xuat():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT px.maPX, px.ngayXuat, px.boPhanNhan, nv.tenNV
        FROM phieu_xuat px
        JOIN nhan_vien nv ON px.maNV = nv.maNV
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def insert_phieu_xuat(boPhanNhan, maVT, soLuong, donGia, maNV):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Kiểm tra tồn kho
        cursor.execute("SELECT soLuongTon FROM vat_tu WHERE maVT = %s", (maVT,))
        row = cursor.fetchone()
        if not row:
            raise Exception("Không tìm thấy vật tư.")
        so_ton = row[0]
        if so_ton < soLuong:
            raise Exception(f"Tồn kho không đủ. Hiện có {so_ton}, cần xuất {soLuong}.")

        # Thêm phiếu xuất
        cursor.execute("""
            INSERT INTO phieu_xuat (ngayXuat, boPhanNhan, maNV)
            VALUES (CURDATE(), %s, %s)
        """, (boPhanNhan, maNV))
        maPX = cursor.lastrowid

        # Thêm chi tiết
        cursor.execute("""
            INSERT INTO chi_tiet_phieu_xuat (maPX, maVT, soLuong, donGia)
            VALUES (%s, %s, %s, %s)
        """, (maPX, maVT, soLuong, donGia))

        # Cập nhật tồn kho
        cursor.execute("""
            UPDATE vat_tu SET soLuongTon = soLuongTon - %s WHERE maVT = %s
        """, (soLuong, maVT))

        # Ghi lịch sử
        cursor.execute("""
            INSERT INTO lich_su_giao_dich (ngayGiaoDich, loaiGiaoDich, maVT, soLuong, maNV, ghiChu)
            VALUES (CURDATE(), 'Xuất', %s, %s, %s, %s)
        """, (maVT, soLuong, maNV, f'Xuất cho {boPhanNhan}'))

        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()
