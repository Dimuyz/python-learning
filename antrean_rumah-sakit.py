#mengetahui queue

print("====== ANTREAN RUMAH SAKT =====")

pasien = [] #bikin antrian

for ses in range(5): #mengulang 3 kali
    nama = input("Nama anda siapa: ") # bertanya
    pasien.append(nama) # menambah kedalam list
print(pasien) #munculkan ke output

print("memanggil pasien.....")
print("Pasien bernama", pasien.pop(0), "silahkan masuk")
print("Nama pasien yang tersisa di tempat duduk sekarang adalah:", pasien)
print("Jumlahnya ada:", len(pasien))

if pasien == []:
    print("belum ada antrean, silahkan daftar ulang")
else:
    print("silahkan lanjut antrian")

lanjut = "yes"
tidak = "no"

hm1 = input("apakah ingin lanjut antrian? ")
if hm1 == "yes":
    print("silahkan lanjut")
elif hm1 == "no":
    print("silahkan pergi dan jangan kembali, candan njing")
else:
    print("MANTOG GOBLOG")


