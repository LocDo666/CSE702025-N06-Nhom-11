from database.db_connector import get_connection

def get_lich_su():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            ls.ngayGiaoDich,
            ls.loaiGiaoDich,
            vt.tenVT,
            ls.soLuong,
            COALESCE(
                (
                    SELECT ctpn.donGia
                    FROM chi_tiet_phieu_nhap ctpn
                    JOIN phieu_nhap pn ON ctpn.maPN = pn.maPN
                    WHERE ls.loaiGiaoDich = 'Nhập'
                        AND ctpn.maVT = ls.maVT
                    ORDER BY pn.ngayNhap DESC
                    LIMIT 1
                ),
                (
                    SELECT ctx.donGia
                    FROM chi_tiet_phieu_xuat ctx
                    JOIN phieu_xuat px ON ctx.maPX = px.maPX
                    WHERE ls.loaiGiaoDich = 'Xuất'
                        AND ctx.maVT = ls.maVT
                    ORDER BY px.ngayXuat DESC
                    LIMIT 1
                ),
                0
            ) AS gia,
            COALESCE(nv.tenNV, '(Đã xoá)') AS tenNV,
            ls.ghiChu
        FROM lich_su_giao_dich ls
        JOIN vat_tu vt ON ls.maVT = vt.maVT
        LEFT JOIN nhan_vien nv ON ls.maNV = nv.maNV
        ORDER BY ls.ngayGiaoDich DESC
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows
