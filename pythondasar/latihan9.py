import datetime as dt

print("\nkalkulasi umur dan tahun anda")
tanggal = int(input("Masukan Tanggal lahir \t : "))
bulan = int(input("Masukan Bulan Lahir \t : "))
tahun = int(input("Masukan Tahun lahir \t : "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"\nTanggal lahir anda adalah {tanggal_lahir}")
print(f"Harinya Adalah {tanggal_lahir:%A}")

hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
print(f"\nhari ini tanggal {hari_ini}")
print(f"umur harinya adalah {umur_hari}")
print(f"umur ku adalah {umur_tahun} tahun")

