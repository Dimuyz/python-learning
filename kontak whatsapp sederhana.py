#belajar menggunakan dictionary
kontak = {}
for i in range(2):
    nama = input("Masukan nama kontak: ")
    nomor = input("Masukan nomor kontak: +62")
    kontak[nama] = nomor
for i, nama in enumerate(kontak, start=1):
    print(f"{i}. {nama}")
