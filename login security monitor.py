import time

user = {"username": "dimaz123"
        ,"password": "cronos03"
        ,"email": "masdim03@gmail.com"
        ,"numb": "087812943102"
        ,"IP": "192.333.333"
        }

percobaan = 0
batas_cobaan = 3
blokir = False
nama = "Dimaz"

def login():
    global percobaan, blokir

    while True:
        print("===== LOGIN SECURITY MONITORING =====")
        username = int(input("masukan username: "))
        password = int(input("masukan password: "))
        if username == user["username"] and password == user["password"]:
            print("harap tunggu proses")
            time.sleep(5)
            print("login sukses! selamat datang",nama)
            print("Email:", user["email"])
            print("numb:", user["numb"])
            print("IP:", user["IP"])
            print("percobaan:", percobaan + 1)
            break
        else:
            percobaan += 1
            print("login gagal!!")
            print("percobaan:", percobaan)

            if percobaan >= batas_cobaan:
                blokir = True
                print("AKUN ANDA DI BLOKIR!!!")
                print("alasan: akun anda telah mencoba login lebih dari 3x")
                print("harap coba dalam jangka waktu 3 hari lagi")
                break
            else:
                sisa = batas_cobaan - percobaan
                print("sisa percobaan:", sisa)
login()
            



