def tambah(*tambah):
    output = 0
    for angka in tambah:
        output += angka
    return output

def kali(*kali):
    output = 1
    for angka in kali:
        output *= angka
    return output