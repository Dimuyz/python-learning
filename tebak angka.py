angka_rahasia = 6
percobaan = 0
maximal = 3

while True:
    print("======= program tebak angka =======")
    print("tebak angka dari 1-10")
    print("anda memiliki 3 kali kesempatan")
    jawab = int(input("masukan angka tebakan anda: "))

    percobaan = percobaan + 1

    if jawab == 6:
        print("jawaban anda benar-!")
        print("anda berhasil menebak di percobaan ke: ", percobaan)
    else:
        print("jawaban anda salah-!")
        print("anda telah mecoba sebanyak: ", percobaan + 1, "kali")
        if percobaan < 3:
            print("maaf percobaan anda habis")
    print("game selesai")
