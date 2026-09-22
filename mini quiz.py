python = "a"
angka4 = "d"
skor = 0

print("===== MINI QUIZ =====")
print("bahasa pemrograaman apa yang bisa di pakai untuk latih logika")
print("a. Python")
print("b. JavaScipt")
print("c. HTML")
print("d. CSS")
jawaban1 = input("silahkan masukan jawaban: ")
if jawaban1 == "a":
    print("jawaban anda benar!")
    skor += 50
else:
    print("jawaban anda kurang tepat")

print("2 + 2 = ?")
print("a. 9")
print("b. 6")
print("c. 3")
print("d. 4")
jawaban2 = input("silahkan masukan jawaban: ")
if jawaban2 == angka4:
    print("betul jawaban anda sudah benar!")
    skor += 50
else:
    print("maaf belajar lagi ya!")

print("======================")
print("skor kamu: ", skor)
print("======================")
