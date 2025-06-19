from database.db_connector import get_connection

def get_all_nhanvien():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT maNV, tenNV, chucVu, boPhan
        FROM nhan_vien
        ORDER BY maNV ASC
    """)
    data = cursor.fetchall()
    conn.close()
    return data

def insert_nhanvien(tenNV, chucVu, boPhan):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO nhan_vien (tenNV, chucVu, boPhan)
        VALUES (%s, %s, %s)
    """, (tenNV, chucVu, boPhan))
    conn.commit()
    conn.close()

def update_nhanvien(maNV, tenNV, chucVu, boPhan):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE nhan_vien
        SET tenNV = %s,
            chucVu = %s,
            boPhan = %s
        WHERE maNV = %s
    """, (tenNV, chucVu, boPhan, maNV))
    conn.commit()
    conn.close()

def delete_nhanvien(maNV):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM nhan_vien
        WHERE maNV = %s
    """, (maNV,))
    conn.commit()
    conn.close()

def get_nhanvien_by_id(maNV):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT maNV, tenNV, chucVu, boPhan
        FROM nhan_vien
        WHERE maNV = %s
    """, (maNV,))
    result = cursor.fetchone()
    conn.close()
    return result
