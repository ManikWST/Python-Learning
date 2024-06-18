import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tkinter.Tk()
window.configure(bg="white")
window.geometry("450x550")
window.resizable(False, False)
window.title("Tambah Data Buku")

urutan = tkinter.StringVar()
judul_buku = tkinter.StringVar()
penulis = tkinter.StringVar()
penerbit = tkinter.StringVar()
tahun_terbit = tkinter.StringVar()

frame = ttk.Frame(window)
frame.pack(padx=50, pady=60, fill="x", expand=True)

# ID/key
label_ID = ttk.Label(frame, text="Masukan ID Buku Baru")
label_ID.pack(padx=6, pady=6, fill="x", expand=True)
input_ID = ttk.Entry(frame, textvariable= urutan)
input_ID.pack(padx=6, pady=6, fill="x", expand=True)

# input Judul
label_judul = ttk.Label(frame, text="Masukan Judul Buku")
label_judul.pack(padx=6, pady=6, fill="x", expand=True)
input_judul = ttk.Entry(frame, textvariable=judul_buku)
input_judul.pack(padx=6, pady=6, fill="x", expand=True)

# input penulis
label_penulis = ttk.Label(frame, text="Masukan Penulis Buku")
label_penulis.pack(padx=6, pady=6, fill="x", expand=True)
input_penulis = ttk.Entry(frame, textvariable=penulis)
input_penulis.pack(padx=6, pady=6, fill="x", expand=True)

# input Penerbit
label_penerbit = ttk.Label(frame, text="Masukan Penerbit Buku")
label_penerbit.pack(padx=6, pady=6, fill="x", expand=True)
input_penerbit = ttk.Entry(frame, textvariable=penerbit)
input_penerbit.pack(padx=6, pady=6, fill="x", expand=True)

# input Tahun terbit
label_thn_terbit = ttk.Label(frame, text="Masukan Tahun terbit Buku")
label_thn_terbit.pack(padx=6, pady=6, fill="x", expand=True)
input_thn_terbit = ttk.Entry(frame, textvariable=tahun_terbit)
input_thn_terbit.pack(padx=6, pady=6, fill="x", expand=True)
# Instruksi
print("\t NO. \t|\t Judul Buku \t|\t Penulis Buku \t|\t Penerbit Buku \t|\t Tahun Terbit")
def click():
    print(f"\t {urutan.get()} \t|\t {judul_buku.get()} \t|\t {penulis.get()} \t|\t {penerbit.get()} \t|\t {tahun_terbit.get()}")
    notif = "Data Buku Baru, Berhasil Ditambahkan"
    showinfo(title="pemberitauan", message=notif)

# button
submit = ttk.Button(frame, text="Submit", command=click)
submit.pack(padx=10, pady=10, fill="x", expand=True)




window.mainloop()