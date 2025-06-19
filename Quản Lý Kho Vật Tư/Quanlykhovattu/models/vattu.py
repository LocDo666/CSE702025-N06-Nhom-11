from database.db_connector import get_connection

def get_all_vattu():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT vt.maVT, vt.tenVT, vt.donViTinh, vt.soLuongTon, vt.donGia, ncc.tenNCC
        FROM vat_tu vt
        JOIN nha_cung_cap ncc ON vt.maNCC = ncc.maNCC
    """)
    data = cursor.fetchall()
    conn.close()
    return data

def insert_vattu_if_not_exists(tenVT, dvt, soLuongTon, donGia, maNCC):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT maVT FROM vat_tu WHERE tenVT=%s", (tenVT,))
    result = cursor.fetchone()
    if result:
        cursor.execute("""
            UPDATE vat_tu SET soLuongTon = soLuongTon + %s WHERE maVT = %s
        """, (soLuongTon, result[0]))
        conn.commit()
        conn.close()
        return result[0]
    
    cursor.execute("""
        INSERT INTO vat_tu (tenVT, donViTinh, soLuongTon, donGia, maNCC)
        VALUES (%s, %s, %s, %s, %s)
    """, (tenVT, dvt, soLuongTon, donGia, maNCC))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id

def update_vattu(maVT, tenVT, dvt, donGia):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE vat_tu SET tenVT=%s, donViTinh=%s, donGia=%s WHERE maVT=%s
    """, (tenVT, dvt, donGia, maVT))
    conn.commit()
    conn.close()
