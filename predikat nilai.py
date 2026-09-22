print("====== NILAI SISWA ======")

nama = input("Nama siswa : ")

nilai1 = int(input("Nilai 1 : "))
nilai2 = int(input("Nilai 2 : "))
nilai3 = int(input("Nilai 3 : "))

rata = (nilai1 + nilai2 + nilai3) / 3

print("Rata-rata:", rata)

if rata >= 80:
    print("luar biasa sempurna, pertahankan!")
elif rata >= 60:
    print("semangat sampai ke puncak!")
elif rata >= 30:
    print("tetap semangat!")
elif rata >= 0:
    print("belajar lagi!")
else:
    print("maaf nilai tidak terinput atau tidak terdeteksi")
