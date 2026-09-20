#mengetahui queue

import time
import random

pasien = []

while True:
    print("=========== ANTREAN RUMAH SAKIT ===========\n")
    print("1. tambah 5 pasien")
    print("2. lihat pasien")
    print("3. lihat antrean")
    print("4. panggil pasien") #ini ada dua mau pasien pertama yang di panggil atau pasien acak
    print("5. exit")
    jawaban = int(input("jawaban: "))

    if (jawaban == 1):
        while True:
           print("baik kita menambah pasien..")
           time.sleep(1)
           for i in range(5):
              nama = input("masukan nama: ")
              pasien.append(nama)
           time.sleep(1)
           print("nama pasien berhasil di tambah")
           print("apakah ingin menambah data pasien lagi? (yes/no)")
           jawaban = input("jawaban: ")
           if (jawaban.lower() == "yes"):
                  print("baik kita lanjut menambah pasien sebanyak 5")
                  continue
           elif (jawaban.lower() == "no"):
                  print("baik kita ke menu awal")
                  break
           else:
                  print("maaf perintah salah")
                  break

    elif (jawaban == 2):
        time.sleep(1)
        while True:
           print("==== lihat pasien ====")
           print("1. lihat salah satu pasien")
           print("2 lihat semua pasien")
           print("silahkan pilih dengan angka (1/2)")
           jawaban = int(input("jawaban: "))

           if (jawaban == 1):
                print("masukan nama pasien-!")
                nama = input("nama pasien: ")
                if nama in pasien:
                    time.sleep(1)
                    print("\nnama pasien ditemukan-!")
                    print("apakah ingin lanjut mencari nama pasien? (yes/no)")
                    jawaban = input("jawaban: ")
                    if jawaban.lower() == "yes":
                          print("baik kita teruskan mencari nama pasien")
                          continue   
                    elif jawaban.lower() == "no":
                          print("baik kita kembali ke menu awal")
                          break
                    else:
                          print("maaf perintah atau nama tidak valid")
                          break
                else:
                     print("nama pasien tidak ditemukan")
                     print("apakah ingin melanjutkan pencarian data? (yes/no)")
                     jawaban = input("jawaban: ")
                     if jawaban.lower() == "yes":
                         print("baik kita mengulan ke proses awal")
                         continue
                     elif jawaban.lower() =="no":
                         print("baik kita kembali ke menu awal")
                         break
                     else:
                         print("perintah atau nama tidak valid")
                         break
           elif (jawaban == 2):
                print("baik pencarian semua data pasien akan di proses")
                time.sleep(3)
                print("nama data pasien telah ditemukan")
                print("berikut adalah nama nama pasien:")
                for i, nama in enumerate(pasien, start=1):
                     print(f"{i}, {nama}")
                print("apakah anda ingin lanjut mencari nama pasien? (yes/no)")
                jawaban = input("jawaban: ")
                if jawaban.lower() == "yes":
                     print("baik kita akan lanjut pencarian nama")
                     continue
                elif jawaban.lower() == "no":
                     print("baik kita kembali ke menu awal")
                     break
                else:
                     print("maaf perintah atau nama tidak valid")
                     break
                
    elif (jawaban == 3):
         while True:
           print("===== ANTREAN PASIEN =====")
           time.sleep(1)
           print("berikut antrean para pasien: ")
           for i, nama in enumerate(pasien, start=1):
              print(f"{i}, {nama}")
           print("antrian pasien selesai di perlihatkan-!")
           print("apakah kamu ingin kembali ke menu awal? (yes/no)")
           jawaban = input("jawaban: ")
           if jawaban.lower() == "yes":
              print("baik kita lanjutkan ke menu awal")
              break
           elif jawaban.lower() == "no":
              print("baik teteap berada di antrean")
              continue
           else:
              print("maaf perintah atau antrean tidak valid")
              break

    elif (jawaban == 4):
         while True:
             print("===== PEMANGGILAN PASIEN =====")
             print("1. panggil pasien manual")
             print("2. panggil pasien acak")
             jawaban = int(input("jawaban: "))
             if jawaban == 1:
                  time.sleep(1)
                  nama = input("baik, silahkan panggil nama pasien: ")
                  if nama in pasien:
                      print(f"Atas nama: {nama}")
                      pasien.remove(nama)
                      print("===== RUANGAN =====")
                      print("1. manual")
                      print("2. acak")
                      jawaban = int(input("jawaban: "))
                      if jawaban == 1:
                           print("baik silahkan masukan angka ruangan untuk pasien")
                           ruangan = int(input("ruangan: "))
                           if ruangan > 200:
                                print("maaf ruangan tidak tersedia di atau 200")
                           elif ruangan < 0:
                                print("maaf tidak tersedia ruangan di bawah mines")
                           else:
                                print("ruangan tersedia!")
                                print(f"diinfokan untuk pasien segera memasuki ruangan: {ruangan}")
                                print("nama yang tersisa sekarang adalah: ")
                                for i, nama in enumerate(pasien, start=1):
                                     print(f"{i}. {nama}")
                                print("jumlah pasien saat ini ada: ", len(pasien))
                                print("apakah ingin lanjut memanggil pasien? (yes/no)")
                                jawaban = input("jawaban: ")
                                if jawaban.lower() == "yes":
                                         print("baik kita lanjutkan memanggil pasien")
                                         continue
                                elif jawaban.lower() == "no":
                                         print("baik kembali ke menu awal")
                                         break
                                else:
                                         print("maaf perintah atau pemanggilan pasien tidak valid")
                                         break
                      elif (jawaban == 2):
                            time.sleep(1)
                            print("==== RUANGAN ACAK =====")
                            ruangan = random.randint(0,200)
                            print(f"atas nama pasien: {nama}")
                            print(f"silahkan masuk ke ruangan acak: {ruangan}")
                            print("apakah ingin lanjut pemanggilan pasien? (yes/no) ")
                            jawaban = input("jawaban: ")
                            if jawaban.lower() == "yes":
                                 print("baik kita lanjutkan pemanggilan")
                                 continue
                            elif jawaban.lower() == "no":
                                 print("baik kembali ke menu utam")
                                 break
                            else:
                                 print("maaf perintah atau pemanggilan tidak valid")
                                 break
             elif jawaban == 2:
                  print("========== PERINGATAN =========")
                  print("apakah yakin mengacak pasien?")
                  print("hal ini bisa menimbulkan protes")
                  print("yakin/tidak")
                  jawaban = input("jawaban: ")
                  if jawaban.lower() == "yakin":
                       print("baik kita lanjut ke proses...")
                       time.sleep(1)
                       print("pengambilan nama...")
                       time.sleep(1)
                       print("pengambilan data...")
                       time.sleep(1)
                       print("baik nama sudah keluar!")
                       ruangan = random.randint(0,200)
                       pilihan = random.choice(pasien)
                       print("atas nama: ", (pilihan))
                       print(f"silahkan memasuki ruangan acak: {ruangan}")
                       print("apakah anda ingin melanjutkan pemanggilan lagi? (yes/no)")
                       jawaban = input("jawaban: ")
                       if jawaban.lower() == "yes":
                            print("baik kita ulang proses lagi")
                            continue
                       elif jawaban.lower() == "no":
                            print("baik kembali ke menu utama")
                            break
                       else:
                            print("perintah atau pemanggilan tidak valid")
                            break
                  elif jawaban.lower() == "tidak":
                       print("baik kembali ke menu pemanggilan")
                       time.sleep(1)
                       continue
    elif (jawaban == 5):
         print("baik apakah kamu yakin akan mengakhiri program ini? (yes/no)")
         jawaban = input("jawaban: ")
         if jawaban.lower() == "yes":
              print("terimakasih sudah menggunakan program!")
              break
         elif jawaban.lower() == "no":
              print("baik kita kembali ke menu utama")
              continue
         else:
              print("perintah tidak valid")
              continue