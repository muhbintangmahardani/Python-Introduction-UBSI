# Membuat dictionary untuk data jurusan dan biaya kuliah
jurusan = {"SI": "Sistem Informasi", "SIA": "Sistem Informasi Akuntansi"}
biaya_kuliah = {"SI": 2400000, "SIA": 2000000}

# Meminta input dari pengguna
NIS = input("Masukkan NIS: ")
nama = input("Masukkan nama: ")
print("Pilih jurusan:")
for kode_jurusan, nama_jurusan in jurusan.items():
    print(kode_jurusan + " - " + nama_jurusan)
jurusan_pilihan = input("Kode jurusan: ")

# Memeriksa apakah kode jurusan yang dimasukkan benar
while jurusan_pilihan not in jurusan.keys():
    print("Kode jurusan salah. Silakan coba lagi.")
    print("Pilih jurusan:")
    for kode_jurusan, nama_jurusan in jurusan.items():
        print(kode_jurusan + " - " + nama_jurusan)
    jurusan_pilihan = input("Kode jurusan: ")

# Menghitung biaya kuliah
biaya = biaya_kuliah[jurusan_pilihan]

# Menampilkan hasil
print("Data pendaftaran mahasiswa baru:")
print("NIS: " + NIS)
print("Nama: " + nama)
print("Jurusan: " + jurusan[jurusan_pilihan])
print("Biaya kuliah: Rp " + str(biaya))