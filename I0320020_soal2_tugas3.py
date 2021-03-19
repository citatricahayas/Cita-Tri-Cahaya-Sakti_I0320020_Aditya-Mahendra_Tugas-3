#Dictionary Cita
dict = {'Nama': 'Cita Tri Cahaya Sakti', 'Hobi': ['Main Game', 'Berenang', 'Nonton Film'],
        'SosMed': ['line = 28022002cita', 'Wa = 085259970915', 'IG = cita_sakti'],
        'lagu Kesukaan': ['Unstoppable','Immortal Hero', 'Born For This'],
        'Makanan Kesukaan': ['Gudeg', 'Mie Instan', 'Bubur'] }
print("Dictionary Cita :", "\n", dict, "\n")

#Mengubah Hobi Cita
dict['Hobi'][1] = 'Makan'

#Mengubah SosMed Cita
dict['SosMed'][2] = 'Facebook = Cita Tri'

#Menghapus dua makanan kesukaan
del dict['Makanan Kesukaan'][1:]
#Menambahkan Hobi Cita
dict['Hobi'].append('Traveling')

#Dictionary sesudah diupdate
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>DICTIONARY SESUDAH DIUPDTADE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print(" ")
print("Dictionary Cita :", "\n", dict)
