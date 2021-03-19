#List nama teman
list_temanku = ["Efa", "Erysa", "Memed", "Tsania", "Danendra", "Ayu", "Rengga", "Hafizh", "Akrom", "Desyana"]
print("List nama teman :", "\n", list_temanku, "\n")
print("---------------------------------------INDEKS DALAM LIST---------------------------------------")

#Menampilkan list indeks No. 4, 6, dan 7
print("List indeks nomor 4 adalah", list_temanku[4])
print("List indeks nomor 6 adalah", list_temanku[6])
print("List indeks nomor 7 adalah", list_temanku[7])

#Mengubah list nama urutan 3, 5 ,dan 9
list_temanku[3] = "Dhea"
list_temanku[5] = "Candrika"
list_temanku[9] = "Denny"
list_temanku.append("Cristin")
list_temanku.append("Deadila")
print("\n")

#Menampilkan List dengan perulangan
print("----------------------------------------LIST NAMA TEMAN----------------------------------------")

for isi in list_temanku:
    print(isi)

#Menampilkan panjang list
print(" ")
print("panjang list teman saya adalah", len(list_temanku))
