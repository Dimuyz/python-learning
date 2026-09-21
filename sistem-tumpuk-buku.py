#belajar praktek stack
print("===== SISTEM TUMPUKAN BUKU PERPUSTAKAAN =====")

stack = []
stack.append("Buku Git")
stack.append("Buku cheat GTA")
stack.append("Buku python")
stack.append("Buku C++")
stack.append("buku C#")
stack.append("Buku Javascript")
print(stack)

print("Mengambil buku.....")
print(stack.pop())
print(stack.pop())

print("Sisa buku di lemari sekarang: ")
print(stack)

print("jumlah buku: ", len(stack))