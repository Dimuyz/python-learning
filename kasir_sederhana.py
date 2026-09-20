#membuat project kasih sederhana
#mengetahui dasar input(), variabel, tipe data (int), operasi matematika, print

import time
print("===== STRUK TOKO PYTHON =====")

nama = input("Nama pembeli: ")
barang = input("Nama barang: ")
harga = int(input("Harga barang: "))
jumlah = int(input("Jumlah: "))

print("sedang menghitung input harga dan jumlah...")
time.sleep(1)
Total = (harga * jumlah)
print(f"hasil: {Total}")


