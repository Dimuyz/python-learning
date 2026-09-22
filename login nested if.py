print("Login System Python")

username_benar = "admin" 
password_benar = "admin123"

while True:

    username = input("\nUsername : ")
    password = input("\nPassword : ")

    print("\nMengecek login....")

    if username == username_benar and password == password_benar:

        print("\nLogin berhasil")

        break

    else:

        print("\nUsername atau Password salah!")

        print("Silahkan coba kembali")

print("\nProgram selesai")

