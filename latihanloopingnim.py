ulang=2
for i in range(ulang):
    print("data ke - " + str(i+1))
    nama=input("Masukan Nim anda :")
    uts=int(input("Masukan Nilai UTS anda :"))
    uas=int(input("Masukan Nilai UAS anda :"))
    print("Nim anda adalah %s nilai UTS anda %i nilai UAS anda %i" % (nama,uts,uas))
    print("------------------------------------------\n")