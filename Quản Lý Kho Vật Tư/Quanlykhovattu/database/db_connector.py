import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",  # Cập nhật nếu có mật khẩu
        database="kho_vattu"
    )
