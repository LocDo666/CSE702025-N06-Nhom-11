import tkinter as tk
from tkinter import ttk, messagebox
from models.nhanvien import get_all_nhanvien, insert_nhanvien, update_nhanvien, delete_nhanvien

def create_tab_nhanvien(frame):
    frame.configure(bg='#e6f0fb')

    title = tk.Label(frame, text="Quản lý nhân viên", font=('Segoe UI', 14, 'bold'),
                     bg='#e6f0fb', fg='#003366')
    title.pack(pady=10)

    cols = ("Mã NV", "Tên NV", "Chức vụ", "Bộ phận")
    tree = ttk.Treeview(frame, columns=cols, show="headings", style="Custom.Treeview")
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')
    tree.pack(fill='both', expand=True, padx=20, pady=10)

    def load():
        tree.delete(*tree.get_children())
        for row in get_all_nhanvien():
            tree.insert('', 'end', values=row)

    def them():
        win = tk.Toplevel(frame)
        win.title("Thêm nhân viên")
        win.configure(bg='#e6f0fb')

        entries = [tk.Entry(win, font=('Segoe UI', 10)) for _ in range(3)]
        labels = ["Tên", "Chức vụ", "Bộ phận"]
        for i, lbl in enumerate(labels):
            tk.Label(win, text=lbl, font=('Segoe UI', 10), bg='#e6f0fb').grid(row=i, column=0, padx=10, pady=5, sticky='e')
            entries[i].grid(row=i, column=1, padx=10, pady=5, sticky='w')

        def luu():
            insert_nhanvien(*[e.get() for e in entries])
            win.destroy()
            load()

        ttk.Button(win, text="Lưu", command=luu).grid(row=3, columnspan=2, pady=10)

    def sua():
        sel = tree.selection()
        if not sel: return
        old = tree.item(sel)['values']

        win = tk.Toplevel(frame)
        win.title("Sửa nhân viên")
        win.configure(bg='#e6f0fb')

        entries = [tk.Entry(win, font=('Segoe UI', 10)) for _ in range(3)]
        for i, e in enumerate(entries): e.insert(0, old[i+1])
        labels = ["Tên", "Chức vụ", "Bộ phận"]
        for i, lbl in enumerate(labels):
            tk.Label(win, text=lbl, font=('Segoe UI', 10), bg='#e6f0fb').grid(row=i, column=0, padx=10, pady=5, sticky='e')
            entries[i].grid(row=i, column=1, padx=10, pady=5, sticky='w')

        def luu():
            update_nhanvien(old[0], *[e.get() for e in entries])
            win.destroy()
            load()

        ttk.Button(win, text="Cập nhật", command=luu).grid(row=3, columnspan=2, pady=10)

    def xoa():
        sel = tree.selection()
        if not sel: return
        if messagebox.askyesno("Xoá", "Bạn chắc chắn xoá?"):
            delete_nhanvien(tree.item(sel)['values'][0])
            load()

    btn_frame = tk.Frame(frame, bg='#e6f0fb')
    btn_frame.pack(pady=10)
    for lbl, cmd in [("Thêm", them), ("Sửa", sua), ("Xoá", xoa), ("Làm mới", load)]:
        ttk.Button(btn_frame, text=lbl, command=cmd, width=12).pack(side='left', padx=10)

    load()
