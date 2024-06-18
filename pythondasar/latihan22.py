teman_teman = {
    "cup" : "Ucup Surucup",
    "ags" : "Agus Sudirjo",
    "ati" : "Yati Sumanti",
    "Yn" : "Yono Yasono"
}

key = teman_teman.keys()
print(f"\nkeynya adalah = {key}")

value = teman_teman.values()
print(f"Valuenya adalah = {value}")

item = teman_teman.items()
print(f"semua item = {item}\n")

#for
print("INI ADALAH KEY")
for key in teman_teman.keys():
    print(f"keynya adalah = {key}")

print("\nINI ADALAH VALUE/ISI")
for value in teman_teman.values():
    print(f"ISInya adalah = {value}")
print("\ndan\n")
for pa in teman_teman:
    print(teman_teman.get(pa))

print("\nItems, untuk keys dan valuenya")
for key,value in teman_teman.items():
    print(f"Keysnya = {key}, Valunya = {value}")