import tkinter as tk
from tkinter import ttk, messagebox
from models.phieunhap import get_phieu_nhap, insert_phieu_nhap
from models.nhacungcap import get_all_ncc, insert_ncc_if_not_exists

def create_tab_phieunhap(frame):
    frame.configure(bg='#e6f0fb')

    title = tk.Label(frame, text="Quản lý phiếu nhập", font=('Segoe UI', 14, 'bold'), bg='#e6f0fb', fg='#003366')
    title.pack(pady=10)

    cols = ("Mã PN", "Ngày", "Nhà cung cấp", "NV nhập")
    tree = ttk.Treeview(frame, columns=cols, show='headings', style='Custom.Treeview')
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')
    tree.pack(fill='both', expand=True, padx=20, pady=10)

    def load():
        tree.delete(*tree.get_children())
        for row in get_phieu_nhap():
            tree.insert('', 'end', values=row)

    def nhap():
        win = tk.Toplevel(frame)
        win.title("Thêm phiếu nhập")
        win.configure(bg='#e6f0fb')

        nccs = get_all_ncc()
        ten_nccs = [n[1] for n in nccs]

        labels = ["Tên VT", "ĐVT", "SL", "Giá", "Tên NCC", "Địa chỉ", "SĐT", "Mã NV"]
        entries = {}

        for i, label in enumerate(labels):
            tk.Label(win, text=label, font=('Segoe UI', 10), bg='#e6f0fb').grid(row=i, column=0, padx=10, pady=5, sticky='e')
            e = tk.Entry(win, font=('Segoe UI', 10))
            e.grid(row=i, column=1, padx=10, pady=5, sticky='w')
            entries[label] = e

        # ComboBox cho Tên NCC (cho phép gõ hoặc chọn)
        var_ncc = tk.StringVar()
        cb = ttk.Combobox(win, textvariable=var_ncc, values=ten_nccs, font=('Segoe UI', 10), state="normal")
        cb.grid(row=4, column=1, padx=10, pady=5, sticky='w')
        entries["Tên NCC"] = cb

        def autofill_ncc(event):
            ten = entries["Tên NCC"].get().strip()
            for n in nccs:
                if n[1] == ten:
                    entries["Địa chỉ"].delete(0, tk.END)
                    entries["Địa chỉ"].insert(0, n[2])
                    entries["SĐT"].delete(0, tk.END)
                    entries["SĐT"].insert(0, n[3])
                    break

        entries["Tên NCC"].bind("<<ComboboxSelected>>", autofill_ncc)

        def luu():
            try:
                # Lấy thông tin NCC
                ten_ncc = entries["Tên NCC"].get().strip()
                dia_chi = entries["Địa chỉ"].get().strip()
                sdt = entries["SĐT"].get().strip()

                # Kiểm tra nhập thiếu
                if not ten_ncc:
                    messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập tên nhà cung cấp")
                    return

                # Lấy mã NCC, thêm nếu chưa có
                ma_ncc = insert_ncc_if_not_exists(ten_ncc, dia_chi, sdt)

                # Gọi thêm phiếu nhập
                insert_phieu_nhap(
                    ma_ncc,
                    entries["Tên VT"].get().strip(),
                    entries["ĐVT"].get().strip(),
                    int(entries["SL"].get()),
                    float(entries["Giá"].get()),
                    int(entries["Mã NV"].get())
                )
                win.destroy()
                load()
            except Exception as e:
                messagebox.showerror("Lỗi", str(e))

        ttk.Button(win, text="Nhập", command=luu).grid(row=len(labels), columnspan=2, pady=10)

    ttk.Button(frame, text="Thêm phiếu nhập", command=nhap).pack(pady=10)

    load()
