#Tugas Gerobak Chicken - Muh Bintang Mahardani 17225123

print("+------------------------------------+")
print("|    WINNER WINNER CHICKEN DINNER    |")
print("+------------------------------------+")
print("| Kode | JenisPotong | Harga         |")
print("|  D   |    Dada     | Rp.2500       |")
print("|  P   |    Paha     | Rp.2000       |")
print("|  S   |    Sayap    | Rp.1500       |")
print("+------------------------------------+")

#
banyak_jenis=int(input("Banyak jenis :"))
kode=[]
banyak_potong=[]
jenis=[]
harga=[]
jumlah=[]
i=0
for i in range(banyak_jenis):
    print("Jenis ke-", i+1)
    kode.append(input("Kode Potong [D/P/S] :"))
    banyak_potong.append(int(input("Banyak Potong :")))

    if kode[i]=="D":
        jenis.append("Dada")
        harga.append("2500")
        jumlah.append(banyak_potong[i] * int("2500"))
    elif kode[i]=="P":
        jenis.append("Paha")
        harga.append("2000")
        jumlah.append(banyak_potong[i] * int("2000"))
    elif kode[i]=="S":
        jenis.append("Sayap")
        harga.append("1500")
        jumlah.append(banyak_potong[i] * int("1500"))
    else:
        jenis.append("kode salah")
        harga.append("0")
        jumlah.append(banyak_potong[i] * int("0"))

print("+--------------------------------------+")
print("|      WINNER WINNER CHICKEN DINNER    |")
print("+--------------------------------------+")
print("No   Jenis     Harga        Banyak    Jumlah")
print("     Potong    Satuan       Beli      Harga ")
print("+--------------------------------------+")

jumlah_bayar=0
a=0
while a<banyak_jenis:
    jumlah_bayar=jumlah_bayar+jumlah[a]
    print("%i    %s       %s        %i         %i" % (a+1, jenis[a], harga[a], banyak_potong[a], jumlah[a]))
    a = a + 1

pajak = jumlah_bayar * 0.1 
total_bayar = jumlah_bayar + pajak
print("Pajak 10 % Rp. ", int(pajak))
print("Total Bayar Rp. ", int(total_bayar))