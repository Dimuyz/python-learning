#projek password login sederhana
import time
username_asli = "dimaz"
password_asli = "python123"
print("====LOGIN USERNAME DAN PASSWORD====")

username = input("masukan username: ")
if username == username_asli:
    print("username benar silahkan tunggu dan masukan password")
    time.sleep(2)
else:
    print("maaf salah silahkan ulang")
    exit()

password = input("masukan password: ")
if password == password_asli:
    print("password benar silahkan masuk")
    time.sleep(3)
else:
    print("maaf password tidak benar silahkan mengulang dari awal")
    exit()
time.sleep(1)
print("===================")
print("LOGIN BERHASIL")
print("Selamat datang dimaz")
print("===================")

time.sleep(3)

muy = input("apakah ingin melanjutkan program? (yes/no):")
if muy.lower() == "yes":
    print("melanjutkan program...")
elif muy.lower() == "no":
    print("mengakhiri program...terimkasih sudah menggunakan program")
else:
    print("perintah tidak valid")
