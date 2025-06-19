import tkinter as tk
from tkinter import ttk
from models.lichsu import get_lich_su

def create_tab_lichsu(frame):
    frame.configure(bg='#e6f0fb')  # Nền xanh nhạt đồng bộ

    title = tk.Label(frame, text="Lịch sử giao dịch",
                     font=('Segoe UI', 14, 'bold'),
                     bg='#e6f0fb', fg='#003366')
    title.pack(pady=10)

    # Cột
    columns = ("Ngày", "Loại", "Tên VT", "Số lượng", "Đơn giá", "Nhân viên", "Ghi chú")
    tree = ttk.Treeview(frame, columns=columns, show='headings', style="Custom.Treeview")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')  # Canh giữa đẹp hơn

    tree.pack(fill='both', expand=True, padx=20, pady=10)

    # Nút làm mới
    def load_data():
        tree.delete(*tree.get_children())
        for row in get_lich_su():
            ngay, loai, ten_vt, so_luong, gia, ten_nv, ghi_chu = row
            gia_fmt = f"{gia:,.0f}₫" if gia else "0₫"
            tree.insert('', 'end', values=(ngay, loai, ten_vt, so_luong, gia_fmt, ten_nv, ghi_chu or ""))

    btn_refresh = ttk.Button(frame, text="Làm mới", command=load_data)
    btn_refresh.pack(pady=10)

    load_data()
