mahasiswa1 = {
    "nama": "Manik Wastika",
    "nim": "22010101124",
    "kelas": "M"
}

mahasiswa2 = {
    "nama": "Agus Dharma",
    "nim": "2201010245",
    "kelas": "M"
}

mahasiswa3 = {
    "nama": "kusuma Putra",
    "nim": "2201010456",
    "kelas": "M"
}

data_mahasiswa = {
    "maha001": mahasiswa1,
    "maha002": mahasiswa2,
    "maha003": mahasiswa3
}

print(f"\n\t\t Key \t\t|\t\t Nama \t\t\t|\t\t\t NIM \t\t|\t\t Kelas")
for mahasiswa in data_mahasiswa:
    key = mahasiswa

    Nama = data_mahasiswa[key]["nama"]
    NIM = data_mahasiswa[key]["nim"]
    Kelas = data_mahasiswa[key]["kelas"]

    print(f"\t {key} \t\t|\t\t {Nama} \t\t|\t\t {NIM} \t\t|\t\t {Kelas}")
