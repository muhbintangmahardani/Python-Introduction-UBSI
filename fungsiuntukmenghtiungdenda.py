# Fungsi untuk menghitung denda
def hitung_denda(lama_pinjam, kode_film):
    if lama_pinjam > 15 and kode_film == 1:
        return 5000
    elif lama_pinjam > 15 and kode_film == 2:
        return 10000
    else:
        return 15000

# Meminta input jumlah pinjaman
banyak_pinjaman = int(input("Masukkan jumlah pinjaman: "))

# Inisialisasi variabel untuk menyimpan hasil pinjaman
data_pinjaman = []

# Memproses setiap data pinjaman
for i in range(banyak_pinjaman):
    print(f"\nData Pinjaman ke-{i+1}:")
    nama_peminjam = input("Nama Peminjam: ")
    alamat = input("Alamat: ")
    lama_pinjam = int(input("Lama Pinjam (dalam hari): "))
    kode_film = int(input("Kode Film (1: Indonesia, 2: Barat, 3: Korea): "))
    harga_sewa = 0

    if kode_film == 1:
        jenis_film = "Indonesia"
        harga_sewa = 20000
    elif kode_film == 2:
        jenis_film = "Barat"
        harga_sewa = 30000
    elif kode_film == 3:
        jenis_film = "Korea"
        harga_sewa = 25000

    kategori_penyewa = input("Kategori Penyewa (P: Pelanggan, U: Umum): ")
    diskon = 0
    if kategori_penyewa == 'P':
        diskon = 0.02

    denda = hitung_denda(lama_pinjam, kode_film)
    total_sewa = harga_sewa * lama_pinjam
    potongan_diskon = total_sewa * diskon
    total_bayar = total_sewa - potongan_diskon + denda

    # Menambahkan data pinjaman ke dalam list
    data_pinjaman.append({
        'nama_peminjam': nama_peminjam,
        'alamat': alamat,
        'jenis_film': jenis_film,
        'harga_sewa': harga_sewa,
        'lama_pinjam': lama_pinjam,
        'total_sewa': total_sewa,
        'denda': denda,
        'potongan_diskon': potongan_diskon,
        'total_bayar': total_bayar
    })


# Menampilkan hasil data pinjaman
print("============================================================================================================")
print("No. Nama Peminjam  Alamat    Jenis Film  Harga Sewa Lama Pinjam  Total Sewa  Denda  Diskon  Total Bayar")
print("============================================================================================================")
for i, data in enumerate(data_pinjaman):
    print("{:3d} {:<15s} {:<10s} {:<11s} {:9d} {:12d} {:11d} {:6d} {:7.2f} {:11.2f}".format(
        i+1, data['nama_peminjam'], data['alamat'], data['jenis_film'], data['harga_sewa'],
        data['lama_pinjam'], data['total_sewa'], data['denda'], data['potongan_diskon'],
        data['total_bayar']
    ))

print("Keterangan: ")
print("Nama Peminjam : ",nama_peminjam)
print("Alamat : ",alamat)

while True: 
    banyak_pinjaman += 1

    mau_input_lagi = input("\nMau input lagi [y/t]? ")
    if mau_input_lagi.lower() != 'y':
        break