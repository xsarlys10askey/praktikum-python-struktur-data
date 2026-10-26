nilai = [85, 77, 92, 65, 70, 88, 56, 90, 76, 83]

# (a) Menghitung rata-rata
rata_rata = sum(nilai) / len(nilai)

# (b) Menentukan nilai tertinggi dan terendah
nilai_tertinggi = max(nilai)
nilai_terendah = min(nilai)

# (c) Mengelompokkan nilai ke kategori A/B/C/D/E
kategori = []

for n in nilai:
    if n >= 85:
        kategori.append("A")
    elif n >= 75:
        kategori.append("B")
    elif n >= 65:
        kategori.append("C")
    elif n >= 50:
        kategori.append("D")
    else:
        kategori.append("E")

# (d) Menghitung frekuensi setiap kategori menggunakan dictionary
frekuensi = {}

for k in kategori:
    frekuensi[k] = frekuensi.get(k, 0) + 1

print("Nilai mahasiswa:", nilai)
print("Rata-rata:", rata_rata)
print("Nilai tertinggi:", nilai_tertinggi)
print("Nilai terendah:", nilai_terendah)
print("Kategori:", kategori)
print("Frekuensi kategori:", frekuensi)