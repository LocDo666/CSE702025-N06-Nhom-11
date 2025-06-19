from database.db_connector import get_connection
from models.vattu import insert_vattu_if_not_exists

def get_phieu_nhap():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT pn.maPN, pn.ngayNhap, ncc.tenNCC, nv.tenNV
        FROM phieu_nhap pn
        JOIN nha_cung_cap ncc ON pn.maNCC = ncc.maNCC
        JOIN nhan_vien nv ON pn.maNV = nv.maNV
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def insert_phieu_nhap(maNCC, tenVT, dvt, soLuong, donGia, maNV):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        # Thêm phiếu nhập
        cursor.execute("""
            INSERT INTO phieu_nhap (ngayNhap, maNCC, maNV)
            VALUES (CURDATE(), %s, %s)
        """, (maNCC, maNV))
        maPN = cursor.lastrowid

        # Thêm hoặc lấy mã vật tư
        maVT = insert_vattu_if_not_exists(tenVT, dvt, soLuong, donGia, maNCC)

        # Ghi chi tiết phiếu nhập
        cursor.execute("""
            INSERT INTO chi_tiet_phieu_nhap (maPN, maVT, soLuong, donGia)
            VALUES (%s, %s, %s, %s)
        """, (maPN, maVT, soLuong, donGia))

        # Ghi lịch sử
        cursor.execute("""
            INSERT INTO lich_su_giao_dich (ngayGiaoDich, loaiGiaoDich, maVT, soLuong, maNV, ghiChu)
            VALUES (CURDATE(), 'Nhập', %s, %s, %s, %s)
        """, (maVT, soLuong, maNV, f'Nhập từ NCC mã {maNCC}'))

        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()
