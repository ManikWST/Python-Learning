import datetime as dt
import os
import string
import random

template = {
    "nama": "",
    "nim": "",
    "sks_lulus": "",
    "lahir": ""
}

data_mahasiswa = {}

while True:
    os.system("cls")
    print("Masukan Data Mahasiswa")

    mahasiswa = dict.fromkeys(template.keys())
    mahasiswa["nama"] = input("masukan nama mahasiswa : ")
    mahasiswa["nim"] = input("masukan NIM mahasiswa : ")
    mahasiswa["sks_lulus"] = int(input("SKS lulus : "))
    TAHUN = int(input("masukan tahun lahir (YYYY) : "))
    BULAN = int(input("masukan Bulan Lahir (1-12) : "))
    TANGGAL = int(input("masukan tanggal lahir (1-31) :"))
    mahasiswa["lahir"] = dt.datetime(TAHUN,BULAN,TANGGAL)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))

    data_mahasiswa.update({KEY:mahasiswa})

    print(f"\n{"Key":<6} {"Nama":<17} {"NIM":<10} {"SKS Lulus":<10} {"Lahir":<10}")
    for mahasiswa in data_mahasiswa:
        key = mahasiswa

        nama = data_mahasiswa[key]["nama"]
        nim = data_mahasiswa[key]["nim"]
        sks_lulus = data_mahasiswa[key]["sks_lulus"]
        lahir = data_mahasiswa[key]["lahir"].strftime("%X")

        print(f"{key:<6} {nama:<17} {nim:<10} {sks_lulus:^10} {lahir:^10}")

    tanyakan = input("lanjut menambahkan data mahasiswa ? (Y/N) : ")

    if tanyakan == "n" or tanyakan == "N":
        break