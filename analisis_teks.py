from collections import Counter

# Membaca teks dari file
with open("teks.txt", "r", encoding="utf-8") as file:
    teks = file.read()

# Mengubah teks menjadi huruf kecil dan membersihkan tanda baca
teks = teks.lower()

for tanda in ".,!?;:":
    teks = teks.replace(tanda, "")

kata = teks.split()

# (a) Menghitung frekuensi setiap kata menggunakan dictionary
frekuensi = {}

for k in kata:
    frekuensi[k] = frekuensi.get(k, 0) + 1

# (b) Menampilkan 10 kata paling sering muncul
sepuluh_teratas = Counter(kata).most_common(10)

# (c) Mengidentifikasi kata yang hanya muncul sekali
hapax_legomena = {k for k, jumlah in frekuensi.items() if jumlah == 1}

# (d) Menghitung type-token ratio
jumlah_kata = len(kata)
jumlah_kata_unik = len(set(kata))

ttr = jumlah_kata_unik / jumlah_kata

print("Frekuensi setiap kata:")
print(frekuensi)

print("\n10 kata paling sering muncul:")
for kata_item, jumlah in sepuluh_teratas:
    print(kata_item, ":", jumlah)

print("\nKata yang hanya muncul sekali (hapax legomena):")
print(hapax_legomena)

print("\nType-Token Ratio (TTR):", ttr)