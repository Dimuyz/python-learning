#mencari angka terbesar
angka = [47, 12, 98, 35, 76, 21, 84, 53, 9, 65]
print("====DAFTAR NILAI====")
for i in angka:
    print(i)
print("angka terbesar", angka[-8])
print("angka terkecil", angka[-2])

nilai = int(input("masukan nilai: "))

if nilai > 50:
    print("KAMU LULUS")
else:
    print("COBA LAGI DI UJIAN BULAN DEPAN")


