#Cara menghapus pada Dictionary Python

dict = {'Nama': 'Cita', 'Umur': '19', 'Hobi': 'Main Game'}

del dict['Nama']      #Menghapus entri dengan key 'Nama'
dict.clear()          #Menghapus semua entri di dict
del dict              #Menghapus dictionary yang sudah ada

print("dict['Nama']", dict['Nama'])
print("dict['Umur']", dict['Umur'])
