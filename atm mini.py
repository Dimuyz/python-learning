import time
pin = "877777"
saldo = 10000000
nama = "Dimaz"
noncard = 1
card = 2
#pemisah untuk variabel ke 1


print("====== SELAMAT DATANG DI ATM JAYA ======\n")

while True:
    time.sleep(3)
    print("Halo,selamat datang di ATM JAYA WIJAYA silahkan pilih metode")
    print("ambil uangmu!\n")

    print("mohon tunggu sebentar....")
    time.sleep(3)
    print("CARDLESS (1) / DEBIT (2)")
    pas = int(input("silahkan masukan nomor metode yang diinginkan: "))
    if pas == noncard:
        print("mohon maaf saat ini sedang tidak tersedia metode cardless")
        continue
    elif pas == card:
        print("baik! silahkan masukan kartu!")
        time.sleep(5)
        print("masukan kartu sukses, tunggu sebentar....")
        time.sleep(2)
        p2 = input("silahkan masukan password: ")
        if p2 == pin:
            print("wopaaa! berhasil kita akan arahkan kamu ke menu!\n")
        else:
            print("silahkan coba lagi!")
            break
        time.sleep(3)

        #pemisah untuk variabel kedua
        cs = 1
        tt = 2
        st = 3
        out = 4
        #pemisah 
        #pemisah untuk variabel ketiga
        limpul = 50000
        cepe = 100000
        cego = 150000
        cepepe = 200000
        wangah = 250000
        cepelu = 300000
        #pemisah
        
        print("===== ATM =====")
        print("1. Cek Saldo")
        print("2. Tarik Tunai")
        print("3. Setor Tunai")
        print("4. Keluar")
        print("===============")
        time.sleep(3)

        print("pilih dengan angka: (1),(2),(3),(4)")
        cek = int(input("masukan metode mana yang di inginkan: "))
        if cek == cs:
            print(saldo)
        elif cek == tt:
            print("baik silahkan pilih berapa yang ingin di ambil")
            print("baik silahkan pilih berapa yang ingin di ambil")
            print("mohon di perhatikan bahwa pengambilan uang")
            print("hanya bisa berupa genap")
            time.sleep(2)
            print("50.000,100.000,150.000,200.000,250.000,300.000")
            time.sleep(2)
            ceksal = int(input("silahkan masukan yang di inginkan: "))
            if ceksal == limpul:
                print(saldo - 50000)
            elif ceksal == cepe:
                print(saldo - 100000)
            elif ceksal == cego:
                print(saldo - 150000)
            elif ceksal == cepepe:
                print(saldo - 200000)
            elif ceksal == wangah:
                print(saldo - 250000)
            elif ceksal == cepelu:
                print(saldo - 300000)
            else:
                print("maaf metode yang di pilih salah silahkan coba lagi")
        elif cek == st:
            print("sedang tidak menerima setor tunai cuy")
        elif cek == out:
            print("terimakasih sudah menggunakan program kecil kecilan saya!!")
           
