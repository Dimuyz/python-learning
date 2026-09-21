print("\n===== STACK BUKU =====")
buku = []

for i in range(3):
    nama_buku = input("masukan nama buku mu: ")
    buku.append(nama_buku)

print("\n===== BUKU YANG DI PINJAM ======")
print(f"buku yang di pinjamkan: {buku.pop()}")
for i, nama in enumerate(buku, start=1):
    print(f"{i}. {nama}")

print("\n===== ISI RAK BUKU SEKARANG =====")
for i, nama in enumerate(buku, start=1):
    print(f"{i}. {nama}")


print("\n===== JUMLAH BUKU =====")
print("jummlahnya sekarang adalah: ", len(buku))



