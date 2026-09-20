
while True:
    print("========== KALKULATOR SEDERHANA ==========\n")
    print("silahkan mulai berhitung, jangan sampai")
    print("salah operator-!\n")
    angka1 = int(input("masukan angka pertama: "))
    operator = input("masukan operator (+,-,*,/): ")
    angka2 = int(input("masukan angka kedua: "))
    

    if operator == "+":
        hasil = angka1 + angka2
        print(f"hasil: {hasil}")
    elif operator == "-":
        hasil = angka1 - angka2
        print(f"hasil: {hasil}")
    elif operator == "*":
        print(f"hasil: {hasil}")
    elif operator == "/":
        if angka2 !=0 & angka1 !=0:
            hasil = angka1 / angka2
            print(f"hasil: {hasil}")
        else:
            print("angka tidak bisa dibagi 0")
    else:
        print("operator atau perhitungan tidak valid")
