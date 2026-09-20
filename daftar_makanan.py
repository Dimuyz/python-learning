#project list makanan
print("===== LIST MAKANAN WARTEG =====")

makanan = []
makanan.append("Nasi goreng")
makanan.append("Rendang")
makanan.append("Gudeg")
makanan.append("Rawon")
makanan.append("Pempek")
makanan.append("Mie aceh")
makanan.append("Soto betawi")
print(makanan)

#lewat sebaris

print(makanan.pop()) #makanan terakhir > teratas akan menghasilkan soto betawi
print(makanan.pop()) #makanan kedua dari terakhir > mie aceh
print(makanan.pop()) #makanan ketiga dari terakhir > pempek

print("Merubah ke menu baru: ")
print(makanan)
print("Melihat sisa data menu: ", len(makanan))
print(makanan)


