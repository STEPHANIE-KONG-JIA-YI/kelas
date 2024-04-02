# Atur cara menentukan petempatan kelas

nama = str(input("MAsukkan nama anda: "))
markah = float(input("Masukkan markah anda: "))

# Kategori kelas
if markah <=40:
    print("Anda ditempatkan di kelas Dedikasi")
elif markah <=60:
    print("Anda ditempatkan di kelas Credik")
elif markah <=80:
    print("Anda ditempatkan di kelas Bijak")
elif markah >80:
    print("Anda ditempaakan di kelas Amanah")
