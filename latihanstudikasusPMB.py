# daftar kode jurusan
kode_jurusan = {'SI': 'Sistem Informasi','SIA': 'Sistem Informasi Akuntansi'}

# daftar biaya kuliah
biaya_kuliah = {'SI': 2400000,'SIA': 2000000}

# input data mahasiswa
print('Pendaftaran Mahasiswa Baru')
nis = input('Masukkan NIS: ')
nama = input('Masukkan Nama: ')
jurusan = input('Masukkan Kode Jurusan (SI/SIA): ')

# validasi kode jurusan
while jurusan not in kode_jurusan.keys():
    jurusan = input('Kode jurusan salah, masukkan lagi (SI/SIA): ')

# hitung biaya kuliah
harga = biaya_kuliah[jurusan]

# output hasil pendaftaran
print('=====================================')
print('Data Mahasiswa Baru')
print('NIS:', nis)
print('Nama:', nama)
print('Jurusan:', kode_jurusan[jurusan])
print('Biaya Kuliah:', harga)
