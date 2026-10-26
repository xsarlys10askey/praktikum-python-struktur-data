inventaris = {
    "Laptop": (7500000, 5),
    "Mouse": (150000, 10),
    "Keyboard": (300000, 7),
    "Monitor": (2000000, 4)
}


# (a) Menambah barang baru
def tambah_barang(nama, harga, stok):
    inventaris[nama] = (harga, stok)


# (b) Mengupdate stok barang
def update_stok(nama, stok_baru):
    if nama in inventaris:
        harga, stok = inventaris[nama]
        inventaris[nama] = (harga, stok_baru)
    else:
        print("Barang tidak ditemukan.")


# (c) Mencari barang dengan harga dalam rentang tertentu
def cari_berdasarkan_harga(harga_min, harga_max):
    hasil = {}

    for nama, (harga, stok) in inventaris.items():
        if harga_min <= harga <= harga_max:
            hasil[nama] = (harga, stok)

    return hasil


# (d) Menghitung total nilai inventaris
def total_nilai_inventaris():
    total = 0

    for harga, stok in inventaris.values():
        total += harga * stok

    return total


# Contoh penggunaan
tambah_barang("Printer", 1200000, 3)
update_stok("Mouse", 15)

print("Data inventaris:")
for nama, data in inventaris.items():
    print(nama, ":", data)

print("\nBarang dengan harga Rp100.000 - Rp2.000.000:")
print(cari_berdasarkan_harga(100000, 2000000))

print("\nTotal nilai inventaris: Rp", total_nilai_inventaris())