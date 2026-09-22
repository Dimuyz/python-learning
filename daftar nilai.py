print("======DAFTAR NILAI SISWA=====")
nama = []
nilai = []
for i in range(5):
    nama1 = input("masukan nama siswa: ")
    nilai1 = int(input("masukan nilai siswa: "))
    nama.append(nama1)
    nilai.append(nilai1)

print("======HASIL SELURUHNYA=====")

print(nama)
print(nilai)
print("Jumlah siswa semuanya:", len(nilai))
print("nilai terendah di raih siswa:  ", min(nilai), "maaf ga nyindir kok")

print("=====HASIL RATA RATA SELURUHNYA=====")
total = nilai[0] + nilai[1] + nilai[2] + nilai[3] + nilai[4]
print("total semua rata rata kelas: ", total / len(nilai))
