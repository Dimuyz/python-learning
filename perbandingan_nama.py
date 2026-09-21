#perbandingan umur
import time

nama_1 = input("siapa namamu?")
print(f"oalah halo", nama_1)

time.sleep(1)

umur_1 = int(input("kalo umur berapa?"))
print(f"shees jadi umur lu", umur_1)

nama_2 = input("kalo nama lu siapa")
print("oalaaa halo", nama_2)

time.sleep(1)

umur_2 = int(input("kalo lu? umur berapa?"))
print("owh ternyata", umur_2 ,"tahun")

if umur_1 > umur_2:
    print("wih umur si", nama_1 ,"lebih gede dari si", nama_2)
elif umur_2 > umur_1:
    print("wih umur si", nama_2 ,"lebih gede dari si", nama_1)
elif umur_1 == umur_2:
    print("wahh umurnya sama ternyata yakk")

