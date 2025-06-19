import tkinter as tk
from tkinter import ttk, messagebox
from models.phieuxuat import get_phieu_xuat, insert_phieu_xuat
from models.vattu import get_all_vattu

def create_tab_phieuxuat(frame):
    frame.configure(bg='#e6f0fb')

    title = tk.Label(frame, text="Quản lý phiếu xuất",
                     font=('Segoe UI', 14, 'bold'),
                     bg='#e6f0fb', fg='#003366')
    title.pack(pady=10)

    cols = ("Mã PX", "Ngày", "Bộ phận nhận", "Nhân viên")
    tree = ttk.Treeview(frame, columns=cols, show='headings', style='Custom.Treeview')
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')
    tree.pack(fill='both', expand=True, padx=20, pady=10)

    def load():
        tree.delete(*tree.get_children())
        for row in get_phieu_xuat():
            tree.insert('', 'end', values=row)

    def xuat():
        win = tk.Toplevel(frame)
        win.title("Thêm phiếu xuất")
        win.configure(bg='#e6f0fb')

        vattus = get_all_vattu()
        ten_vattus = [v[1] for v in vattus]

        labels = ["Tên VT", "Số lượng", "Giá", "Bộ phận nhận", "Mã NV"]
        entries = {}

        for i, label in enumerate(labels):
            tk.Label(win, text=label, font=('Segoe UI', 10), bg='#e6f0fb').grid(
                row=i, column=0, padx=10, pady=5, sticky='e')

            if label == "Tên VT":
                var = tk.StringVar()
                cb = ttk.Combobox(win, textvariable=var, values=ten_vattus,
                                  font=('Segoe UI', 10), state='readonly')
                cb.grid(row=i, column=1, padx=10, pady=5, sticky='w')
                entries[label] = cb
            else:
                e = tk.Entry(win, font=('Segoe UI', 10))
                e.grid(row=i, column=1, padx=10, pady=5, sticky='w')
                entries[label] = e

        def autofill_price(event):
            ten = entries["Tên VT"].get()
            for v in vattus:
                if v[1] == ten:
                    entries["Giá"].delete(0, tk.END)
                    entries["Giá"].insert(0, str(v[3]))
                    break

        entries["Tên VT"].bind("<<ComboboxSelected>>", autofill_price)

        def luu():
            try:
                ten_vt = entries["Tên VT"].get().strip()
                sl_raw = entries["Số lượng"].get().strip()
                gia_raw = entries["Giá"].get().strip()
                bo_phan = entries["Bộ phận nhận"].get().strip()
                ma_nv_raw = entries["Mã NV"].get().strip()

                # Kiểm tra dữ liệu bắt buộc
                if not ten_vt or not sl_raw or not gia_raw or not bo_phan or not ma_nv_raw:
                    messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ các trường.")
                    return

                # Kiểm tra số nguyên
                if not sl_raw.isdigit():
                    messagebox.showerror("Lỗi", "Số lượng phải là số nguyên.")
                    return
                if not ma_nv_raw.isdigit():
                    messagebox.showerror("Lỗi", "Mã nhân viên phải là số nguyên.")
                    return
                try:
                    gia = float(gia_raw)
                except ValueError:
                    messagebox.showerror("Lỗi", "Giá phải là số thực hợp lệ.")
                    return

                sl = int(sl_raw)
                ma_nv = int(ma_nv_raw)

                # Tìm mã vật tư
                ma_vt = next((v[0] for v in vattus if v[1] == ten_vt), None)
                if ma_vt is None:
                    raise Exception("Không tìm thấy vật tư phù hợp.")

                # ✅ Gọi đúng thứ tự tham số
                insert_phieu_xuat(bo_phan, ma_vt, sl, gia, ma_nv)

                win.destroy()
                load()

            except Exception as e:
                messagebox.showerror("Lỗi", str(e))

        ttk.Button(win, text="Xuất", command=luu).grid(row=len(labels), columnspan=2, pady=10)

    ttk.Button(frame, text="Thêm phiếu xuất", command=xuat).pack(pady=10)

    load()
