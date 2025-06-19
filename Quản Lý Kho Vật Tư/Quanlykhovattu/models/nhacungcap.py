from database.db_connector import get_connection

def get_all_ncc():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT maNCC, tenNCC, diaChi, soDienThoai FROM nha_cung_cap")
    rows = cursor.fetchall()
    conn.close()
    return rows

def insert_ncc_if_not_exists(tenNCC, diaChi, sdt):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT maNCC FROM nha_cung_cap WHERE tenNCC=%s", (tenNCC,))
    result = cursor.fetchone()
    if result:
        return result[0]
    cursor.execute("""
        INSERT INTO nha_cung_cap (tenNCC, diaChi, soDienThoai)
        VALUES (%s, %s, %s)
    """, (tenNCC, diaChi, sdt))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id
