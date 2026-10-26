kalimat = input("Masukkan sebuah kalimat: ")

# (a) Menghitung jumlah kata
kata = kalimat.split()
jumlah_kata = len(kata)

# (b) Menghitung jumlah karakter
jumlah_karakter = len(kalimat)

# (c) Menampilkan kata terpanjang
kata_terpanjang = max(kata, key=len)

# (d) Menampilkan kalimat dalam title case
kalimat_title = kalimat.title()

print("\nHasil:")
print("Jumlah kata:", jumlah_kata)
print("Jumlah karakter:", jumlah_karakter)
print("Kata terpanjang:", kata_terpanjang)
print("Kalimat title case:", kalimat_title)