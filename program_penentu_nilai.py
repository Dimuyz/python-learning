#program menentukan nilai
#mengetahui dasar if, elif, else
#operator membandingkan (>=, <=), dan logikan pemrograman

Nama = input("Masukan nama siswa: ")
Nilai = int(input("Masukan nilai: "))

if Nilai == 100:
    print("sangat sempurna! pertahankan")
elif Nilai >= 90:
    print("Grade: A, sangat bagus! pertahankan")
elif Nilai >= 80:
    print("Grade: B, baik!")
elif Nilai >= 70:
    print("Grade: C, cukup baik")
elif Nilai >= 60:
    print("Grade: D, kurang tapi tetap semangat")
elif Nilai >= 0:
    print("Grade: E, kamu perlu belajar lagi")

