# Input data karyawan
print("PROGRAM HITUNG GAJI KARYAWAN")
print("============================")
nama = input("Masukkan Nama Karyawan: ")
golongan = int(input("Masukkan golongan jabatan (1/2/3): "))
pendidikan = input("Masukkan tingkat pendidikan karyawan (SMA/D1/D3/S1): ")
jam_kerja = int(input("Masukkan jumlah jam kerja karyawan: "))

# Hitung gaji pokok
gaji_pokok = 300000

# Hitung tunjangan jabatan
if golongan == 1:
    tunjangan_jabatan = 0.05 * gaji_pokok
elif golongan == 2:
    tunjangan_jabatan = 0.1 * gaji_pokok
else:
    tunjangan_jabatan = 0.15 * gaji_pokok

# Hitung tunjangan pendidikan
if pendidikan == "SMA":
    tunjangan_pendidikan = 0.025 * gaji_pokok
elif pendidikan == "D1":
    tunjangan_pendidikan = 0.05 * gaji_pokok
elif pendidikan == "D3":
    tunjangan_pendidikan = 0.2 * gaji_pokok
else:
    tunjangan_pendidikan = 0.3 * gaji_pokok

# Hitung honor lembur
if jam_kerja > 8:
    honor_lembur = (jam_kerja - 8) * 3500
else:
    honor_lembur = 0

# Hitung total gaji
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur

# Cetak hasil perhitungan
print("----------------------------------------------------------------")
print("                 GAJI KARYAWAN PT DINGIN DAMAI")
print("----------------------------------------------------------------")
print("Nama karyawan:", nama)
print("Gaji pokok:", int(gaji_pokok))
print("Tunjangan jabatan:", int(tunjangan_jabatan))
print("Tunjangan pendidikan:",int(tunjangan_pendidikan))
print("Honor lembur:", int(honor_lembur))
print("========================================+")
print("Total gaji:", int(total_gaji))
