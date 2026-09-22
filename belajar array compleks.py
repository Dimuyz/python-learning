import time

nama = []

while True:
     print("======= DAFTAR NAMA =======")
     print("1. tambah nama")
     print("2. lihat semua nama")
     print("3. hapus nama")
     print("4. keluar")
     user = int(input("pilihan: "))
     print("---------------------------")

    ################
    
     if user == 1:
         nama1 = input("masukan nama: ").lower()
         nama.append(nama1)
         print("tunggu sebentar...")
         time.sleep(2)
         print("proses berhasil-!")
         print("apakah ingin melanjutkan?")
         print("y/n")
         pilihan1 = input("pilih: ").lower()
         if pilihan1 == "y":
              time.sleep(1)
              print("baik program dilanjutkan")
              time.sleep(1)
              continue
         elif pilihan1 == "n":
              print("yakin? karna akan langsung keluar program (y/n)")
              user = input("jawaban: ").lower()
              if user == "y":
                   print("baik terimakasih sudah menggunakan program")
                   break
              elif user == "n":
                   print("baik kembali ke menu utama")
                   continue
              else:
                   print("perintah tidak valid")
                   break
         else:
              print("maaf perintah tidak valid")
              break
         
    ################

     elif user == 2:
         while True:
          print("----------- DATA NAMA ---------")
          print("1. lihat nama manual")
          print("2. lihat semua nama")
          user = int(input("jawaban: "))
          if user == 1:
               print("baik silahkan masukan nama yang ingin dilihat")
               user = input("nama: ")
               if user in nama:
                    print(f"nama berhasil di temukan: {user}")
                    print("apakah ingin lanjut lihat nama? (y/n)")
                    user = input("jawaban: ").lower()
                    if user == "y":
                        print("baik kita ke menu lihat nama")
                        continue
                    elif user == "n":
                        print("baik kembali ke menu utama")
                        break
                    else:
                        print("perintah tidak valid")
                        break
               else:
                   print("maaf nama tidak ditemukan")
                   break
          elif user == 2:
               print("baik kita lihat semua data nama-!")
               time.sleep(2)
               print("semua data nama telah di temukan")
               for i, nama in enumerate(nama, start=1):
                   print(f"{i}. {nama}")
               print("apakah ingin lanjut mencari nama? (y/n)")
               user = input("jawaban: ").lower()
               if user == "y":
                   print("baik kembali ke menu lihat nama")
                   continue
               elif user == "n":
                   print("baik kita kembali ke menu utama")
                   break
               else:
                   print("maaf perintah tidak valid")
                   break

#####################

     elif user == 3:
        while True:
          print("---------- HAPUS NAMA ----------")
          print("apakah kamu yakin ingin hapus nama?")
          print("y/n")
          user = input("jawaban: ")
          if user == "y":
               print("baik kita cari nama yang ingin dihapus")
               print("silahkan ketik nama yang ingin dihapus")
               print(nama)
               user = input("nama yang ingin dihapus: ")
               time.sleep(2)
               if user in nama:
                    nama.remove(user)
                    print("nama telah berhasil di hapus")
                    print(f"nama terhapus: {user}")
                    print("kini tersisa", len(nama), "orang")
                    print(nama)
               print("apakah kamu ingin lanjut menghapus nama? (y/n)")
               user = input("jawaban: ")
               if user == "y":
                   print("baik kita lanjut kembali")
                   continue
               elif user == "n":
                   print("baik kembali kemenu utama")
                   break
               else:
                   print("perintah salah")
                   break        
          elif user == "n":
               print("baik kembali ke menu utama")
               break

###############

     elif user == 4:
          print("apakah kamu yakin ingin keluar? (y/n)")
          user = input("jawaban: ")
          if user == "y":
             print("terimakasih sudah menggunakan program")
             break
          elif user == "n":
             print("baik kita kembali ke menu utama")
             continue
          else:
              print("command error")
              continue