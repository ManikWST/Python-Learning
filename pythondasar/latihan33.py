import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tkinter.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False, False)
window.title("Registrasi")

depan_nama = tkinter.StringVar()
belakang_nama = tkinter.StringVar()

back_input = ttk.Frame(window)
back_input.pack(padx=10, pady=10, fill="x", expand=True)

nama_depan = ttk.Label(back_input, text="Nama Depan :")
nama_depan.pack(padx=10, pady=5, fill="x", expand=True)

nama_depan_entry = ttk.Entry(back_input, textvariable = depan_nama)
nama_depan_entry.pack(padx=10, pady=5, fill="x", expand=True)

nama_belakang = ttk.Label(back_input, text="Nama Belakang :")
nama_belakang.pack(padx=10, pady=5, fill="x", expand=True)

nama_belakang_entry = ttk.Entry(back_input, textvariable = belakang_nama)
nama_belakang_entry.pack(padx=10, pady=5, fill="x", expand=True)

def click():
    print(f"Heloo {depan_nama.get()} {belakang_nama.get()}, Welcome tO my Universe")
    notif = "Data Berhasil Dibuat"
    showinfo(title="Allert", message=notif)

submit = ttk.Button(back_input, text="Submit", command=click)
submit.pack(fill="x", pady=10, padx=10, expand=True)

window.mainloop()