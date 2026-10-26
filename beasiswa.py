beasiswa_a = ["SI001", "SI002", "SI003", "SI004", "SI005"]
beasiswa_b = ["SI003", "SI004", "SI006", "SI007", "SI008"]

set_a = set(beasiswa_a)
set_b = set(beasiswa_b)

# (a) Mahasiswa yang menerima kedua beasiswa
kedua_beasiswa = set_a & set_b

# (b) Mahasiswa yang hanya menerima beasiswa A
hanya_a = set_a - set_b

# (c) Mahasiswa yang menerima beasiswa B tetapi tidak A
hanya_b = set_b - set_a

# (d) Semua mahasiswa unik yang menerima beasiswa
semua_penerima = set_a | set_b

print("Penerima kedua beasiswa:", kedua_beasiswa)
print("Hanya penerima beasiswa A:", hanya_a)
print("Penerima beasiswa B tetapi tidak A:", hanya_b)
print("Semua penerima beasiswa:", semua_penerima)