import tkinter as tk
from tkinter import ttk
from ui.tab_nhanvien import create_tab_nhanvien
from ui.tab_vattu import create_tab_vattu
from ui.tab_nhacungcap import create_tab_nhacungcap
from ui.tab_phieunhap import create_tab_phieunhap
from ui.tab_phieuxuat import create_tab_phieuxuat
from ui.tab_lichsu import create_tab_lichsu

def style_theme():
    style = ttk.Style()
    style.theme_use('clam')

    # Treeview style
    style.configure("Custom.Treeview.Heading",
                    background="#007acc", foreground="white",
                    font=('Segoe UI', 10, 'bold'))
    style.configure("Custom.Treeview",
                    background="white", foreground="#000000",
                    rowheight=26, fieldbackground="white",
                    font=('Segoe UI', 10))
    style.map("Custom.Treeview",
              background=[('selected', '#cce6ff')],
              foreground=[('selected', '#000000')])

    # Button style
    style.configure("TButton",
                    font=('Segoe UI', 10),
                    padding=6,
                    background='#4da6ff',
                    foreground='white')
    style.map("TButton",
              background=[('active', '#3399ff')])

    # Notebook tab style
    style.configure("TNotebook", background="#e6f0fb", borderwidth=0)
    style.configure("TNotebook.Tab", background="#d0e3fa",
                    padding=(10, 5),
                    font=('Segoe UI', 10, 'bold'))
    style.map("TNotebook.Tab", background=[("selected", "#ffffff")])

def open_main_window():
    root = tk.Tk()
    root.title("Quản lý kho vật tư ô tô")
    root.geometry("1100x640")
    root.configure(bg="#e6f0fb")
    style_theme()

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both')

    tab_creators = [
        create_tab_nhanvien,
        create_tab_vattu,
        create_tab_nhacungcap,
        create_tab_phieunhap,
        create_tab_phieuxuat,
        create_tab_lichsu
    ]

    titles = ["Nhân viên", "Vật tư", "Nhà cung cấp", "Phiếu nhập", "Phiếu xuất", "Lịch sử"]

    for create_func, title in zip(tab_creators, titles):
        tab_frame = tk.Frame(notebook, bg="#e6f0fb")
        create_func(tab_frame)
        notebook.add(tab_frame, text=title)

    root.mainloop()

if __name__ == "__main__":
    open_main_window()
