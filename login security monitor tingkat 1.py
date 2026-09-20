data = {
    "username" : "Dimaz1121",
    "password" : "Cronos12"
}


print("======= LOGIN SECURITY =======")
user = input("username: ")
log = input("pasword: ")
if user == data["username"] and log == data["password"]:
    print("berhasil masuk")
else:
    print("maaf silahkan ulang")
