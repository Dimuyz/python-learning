#password id sederhana
import time
IP = 1001001
PASSWORD = "muyzxranz10011"

add = int(input("input the ip address: "))
pas = input("input the password: ")

if add == IP:
    if pas == PASSWORD:
        print("you may enter the freaking room")
    else:
        print("hold a seconde buddy, who are you? ")
else:
    print("who the freaking are you? ")


