import tkinter as tk
from tkinter import ttk, messagebox
from models.vattu import get_all_vattu, update_vattu

def create_tab_vattu(frame):
    frame.configure(bg='#e6f0fb')

    title = tk.Label(frame, text="Quản lý vật tư", font=('Segoe UI', 14, 'bold'),
                     bg='#e6f0fb', fg='#003366')
    title.pack(pady=10)

    cols = ("Mã VT", "Tên VT", "ĐVT", "Tồn", "Giá", "NCC")
    tree = ttk.Treeview(frame, columns=cols, show='headings', style='Custom.Treeview')
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')
    tree.pack(fill='both', expand=True, padx=20, pady=10)

    def load():
        tree.delete(*tree.get_children())
        for row in get_all_vattu():
            maVT, tenVT, dvt, ton, gia, ncc = row
            gia_fmt = f"{gia:,.0f}₫" if gia else "0₫"
            tree.insert('', 'end', values=(maVT, tenVT, dvt, ton, gia_fmt, ncc))

    def sua():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Chưa chọn", "Vui lòng chọn một vật tư để sửa.")
            return
        old = tree.item(sel)['values']

        win = tk.Toplevel(frame)
        win.title("Sửa vật tư")
        win.configure(bg='#e6f0fb')

        labels = ["Tên vật tư", "Đơn vị tính", "Đơn giá"]
        entries = []
        for i, label in enumerate(labels):
            tk.Label(win, text=label, font=('Segoe UI', 10), bg='#e6f0fb').grid(row=i, column=0, padx=10, pady=5, sticky='e')
            e = tk.Entry(win, font=('Segoe UI', 10))
            e.grid(row=i, column=1, padx=10, pady=5, sticky='w')
            entries.append(e)

        # Gán giá trị cũ
        entries[0].insert(0, old[1])
        entries[1].insert(0, old[2])
        entries[2].insert(0, old[4].replace("₫", "").replace(",", ""))

        def capnhat():
            try:
                don_gia = int(entries[2].get().replace(",", ""))
                update_vattu(old[0], entries[0].get(), entries[1].get(), don_gia)
                win.destroy()
                load()
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể cập nhật vật tư.\n{e}")

        ttk.Button(win, text="Lưu", command=capnhat).grid(row=3, columnspan=2, pady=10)

    # Khung nút
    btn_frame = tk.Frame(frame, bg='#e6f0fb')
    btn_frame.pack(pady=10)
    ttk.Button(btn_frame, text="Sửa", command=sua).pack(side='left', padx=10)
    ttk.Button(btn_frame, text="Làm mới", command=load).pack(side='left', padx=10)

    load()
