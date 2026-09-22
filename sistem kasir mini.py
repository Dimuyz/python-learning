#sistem kasir mini
tambah = 1
lihat = 2
hapus = 3
chekout = 4
keluar = 5

data1 = "y"
data2 = "n"
barang = {}
keranjang = []
saldo = 450000 #terkena penilaian (saldo tidak berguna)

while True:
    print("======= KASIR MINI =======\n")
    print("1. tambah barang")
    print("2. lihat keranjang")
    print("3. hapus barang")
    print("4. chekout")
    print("5. keluar")
    pilih = int(input("pilih: "))
    print("==========================")
    if pilih == 1:
        tambah = input("masukan nama barang: ")
        harga = int(input("masukan harga barang: "))
        jumlah = int(input("masukan jumlah barang: "))

        barang = {
            "nama": tambah,
            "harga": harga,
            "jumlah": jumlah,
        }
        keranjang.append(barang)
        print("apakah anda ingin melanjutkan?")
        print("y/n")
        pilih1 = input("pilihan: ")
        if pilih1 == "y":
            continue
        elif pilih1 == "n":
            break
        else:
            print("ngetik apa janco")

    elif pilih == 2:
        for barang in keranjang:
            print("jumlah jenis barang: ", len(keranjang))
            print()

            print("====== KERANJANG ======")
            print("Nama   :", barang[tambah])
            print("Harga  :", barang[harga])
            print("Jumlah :", barang[jumlah])
            print("-----------------------")
            print("apakah ingin melanjutkan? ")
            print("y/n")
            pilih2 = input("pilihan: ")
            if pilih2 == "y":
                continue
            elif pilih2 == "n":
                break
            else:
                print("ngetik apa dek?")

    elif pilih == 3:
        print("anda yakin ingin menghapus orderan?")
        print("y/n")
        jawab = input("pilihan")
        if jawab == "y":
            print("============ HAPUS BARANG ============")
            print("silahkan barang apa yang ingin dihapus")
            for i, barang in enumerate(keranjang, start=1):
                 print(i, ".", barang["nama"])
                 hapus = int(input("pilih yang ingin dihapus: "))
                 keranjang.pop(hapus - 1)
                 print("barang berhasil di hapus! ")

        elif jawab == "n":
            print("terimakasih sudah menggunakan sistem")
            break
        else:
            print("perintah tidak ditemukan")

    elif pilih == 4:
        total = 0
        for barang in keranjang:
            subtotal = barang["harga"] * barang["jumlah"]
            total += subtotal
            print("======= CHECKOUT =======")
            print("Total belanja:", total)
            uang = int(input("Masukkan uang pembayaran: "))
                        
            if uang >= total:
                                kembalian = uang - total
                                print("Kembalian:", kembalian)
                                print("Terima kasih sudah berbelanja!")
            else:
                 print("Uang anda tidak cukup!")

    elif pilih == 5:
         print("apakah anda yakin ingin keluar?")
         print("y/n")
         jawab = input("masukan pilihan: ")
         if jawab == "y":
              print("terimakasih sudah menggunakan sistem")
              break
         elif jawab == "n":
              print("baik sistem di lanjutkan")
              continue
         else:
              print("perintah tidak di temukan")   
    