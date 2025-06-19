import tkinter as tk
from tkinter import messagebox
import json
import os
from ui.main_window import open_main_window

# Đường dẫn file lưu tài khoản
USER_FILE = "database/users.json"

# Load tài khoản từ file
def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    try:
        with open(USER_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

# Lưu tài khoản vào file
def save_users(users_data):
    os.makedirs(os.path.dirname(USER_FILE), exist_ok=True)
    with open(USER_FILE, "w", encoding="utf-8") as f:
        json.dump(users_data, f, indent=4)

# Biến toàn cục lưu người dùng
users = load_users()

def login_screen():
    global users  # Cho phép cập nhật users khi đăng ký mới

    root = tk.Tk()
    root.title("Đăng nhập hệ thống")
    root.geometry("400x350")
    root.configure(bg="#f0f2f5")
    root.resizable(False, False)

    tk.Label(root, text="Đăng nhập hệ thống", font=("Segoe UI", 16, "bold"), bg="#f0f2f5")\
        .pack(pady=20)

    form = tk.Frame(root, bg="#f0f2f5")
    form.pack(pady=10)

    tk.Label(form, text="Tên đăng nhập:", font=("Segoe UI", 10), bg="#f0f2f5")\
        .grid(row=0, column=0, padx=10, pady=8, sticky='e')
    entry_user = tk.Entry(form, font=("Segoe UI", 10), width=25)
    entry_user.grid(row=0, column=1, padx=10, pady=8)

    tk.Label(form, text="Mật khẩu:", font=("Segoe UI", 10), bg="#f0f2f5")\
        .grid(row=1, column=0, padx=10, pady=8, sticky='e')
    entry_pass = tk.Entry(form, show='*', font=("Segoe UI", 10), width=25)
    entry_pass.grid(row=1, column=1, padx=10, pady=8)

    def dang_nhap():
        username = entry_user.get().strip()
        password = entry_pass.get().strip()
        if username in users and users[username] == password:
            root.destroy()
            open_main_window()
        else:
            messagebox.showerror("Lỗi đăng nhập", "Tên đăng nhập hoặc mật khẩu không đúng.")

    def mo_cua_so_dang_ky():
        def luu_tai_khoan():
            global users
            new_user = entry_new_user.get().strip()
            new_pass = entry_new_pass.get().strip()
            if not new_user or not new_pass:
                messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ tài khoản và mật khẩu.")
                return
            if new_user in users:
                messagebox.showerror("Trùng tài khoản", "Tài khoản đã tồn tại.")
                return
            users[new_user] = new_pass
            save_users(users)
            messagebox.showinfo("Thành công", "Tạo tài khoản thành công!")
            top.destroy()

        top = tk.Toplevel(root)
        top.title("Đăng ký tài khoản")
        top.geometry("300x200")
        top.resizable(False, False)
        top.configure(bg="#ffffff")

        tk.Label(top, text="Tên đăng nhập mới:", bg="#ffffff").pack(pady=(15, 5))
        entry_new_user = tk.Entry(top, width=30)
        entry_new_user.pack(pady=5)

        tk.Label(top, text="Mật khẩu:", bg="#ffffff").pack(pady=(10, 5))
        entry_new_pass = tk.Entry(top, show="*", width=30)
        entry_new_pass.pack(pady=5)

        tk.Button(top, text="Tạo tài khoản", command=luu_tai_khoan,
                  bg="#007acc", fg="white", relief="flat").pack(pady=15)

    # Nút đăng nhập
    tk.Button(root, text="Đăng nhập", command=dang_nhap,
              font=("Segoe UI", 10, "bold"), bg="#007acc", fg="white",
              padx=10, pady=5, relief="flat", width=20).pack(pady=10)

    # Nút tạo tài khoản mới
    tk.Button(root, text="Thêm tài khoản", command=mo_cua_so_dang_ky,
              font=("Segoe UI", 9), bg="#e0e0e0", fg="black",
              padx=10, pady=3, relief="flat").pack()

    root.mainloop()
