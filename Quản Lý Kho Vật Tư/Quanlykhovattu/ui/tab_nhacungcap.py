import tkinter as tk
from tkinter import ttk
from models.nhacungcap import get_all_ncc

def create_tab_nhacungcap(frame):
    # Màu nền tổng thể
    frame.configure(bg='#e6f0fb')

    # Thiết lập style hiện đại cho Treeview
    style = ttk.Style()
    style.theme_use("default")

    style.configure("Custom.Treeview",
                    background="#ffffff",
                    foreground="#000000",
                    rowheight=26,
                    fieldbackground="#ffffff",
                    bordercolor="#cccccc",
                    borderwidth=1,
                    font=('Segoe UI', 10))
    style.map("Custom.Treeview",
              background=[('selected', '#cbe6ff')],
              foreground=[('selected', '#000000')])

    style.configure("Custom.Treeview.Heading",
                    background="#d0e3fa",
                    foreground="#000000",
                    font=('Segoe UI', 10, 'bold'))

    style.layout("Custom.Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

    # Label tiêu đề
    title = tk.Label(frame, text="Quản lý nhà cung cấp",
                     font=('Segoe UI', 14, 'bold'),
                     bg='#e6f0fb', fg='#0b4f75')
    title.pack(pady=10)

    # Cột
    cols = ("Mã", "Tên", "Địa chỉ", "SĐT")
    tree = ttk.Treeview(frame, columns=cols, show='headings', style="Custom.Treeview")
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')

    tree.pack(fill='both', expand=True, padx=20, pady=(5, 10))

    # Nút làm mới 
    btn_frame = tk.Frame(frame, bg='#e6f0fb')
    btn_frame.pack(pady=(0, 10))
    ttk.Button(btn_frame, text="Làm mới", command=lambda: load()).pack()

    # Load dữ liệu
    def load():
        tree.delete(*tree.get_children())
        for row in get_all_ncc():
            tree.insert('', 'end', values=row)

    load()
