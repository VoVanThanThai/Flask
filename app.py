import tkinter as tk
from tkinter import font

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Tên của tôi")
window.geometry("400x200")  # Kích thước cửa sổ
window.configure(bg="#40E0D0")  # Background màu xanh ngọc (turquoise)

# Tạo font chữ đẹp
custom_font = font.Font(family="Helvetica", size=24, weight="bold")

# Tạo nhãn (label) để hiển thị tên
label = tk.Label(window, 
                 text="Võ Văn Thần Thái", 
                 font=custom_font, 
                 fg="white",  # Màu chữ trắng
                 bg="#40E0D0",  # Background khớp với cửa sổ
                 pady=50)  # Padding dọc để căn giữa
label.pack(expand=True)  # Căn giữa nhãn trong cửa sổ

# Chạy ứng dụng
window.mainloop()
