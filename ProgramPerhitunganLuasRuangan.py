# Program perhitungan luas ruangan

# Meminta satuan yang dipilih user
satuan = str(input("Masukkan satuan yang diinginkan: "))

# Mendapatkan panjang dan lebar ruang untuk dihitung
panjang = int(input("Masukkan nilai panjang: "))
lebar = int(input("Masukkan nilai lebar: "))
luas = panjang * lebar

# Menampilkan hasil luas ruang
print('Luas ruangan adalah: ', luas, satuan, 'persegi')