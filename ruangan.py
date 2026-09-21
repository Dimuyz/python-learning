ruangan = int(input("masukan ruangan pasien: "))
if ruangan > 200:
    print("ruangan tidak tersedia")
elif ruangan < 0:
    print("tidak ada ruangan lagi hanya ada basemen")
else:
    print("kamar tersedia")