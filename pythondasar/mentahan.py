def tambah(*args):
    ouput = 0
    for tam in args:
        ouput += tam
    return ouput

def kali(*agros):
    output = 1
    for kal in agros:
        output *= kal
    return output

def pangkat(pang:int)->int:
    return lambda angka:angka**pang