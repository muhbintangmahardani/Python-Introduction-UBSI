#variable yang berulang menggunakan List/matriks
list_nim=[]
list_uts=[]
list_uas=[]
list_total=[]

ulang=2
for i in range(ulang):
    print("data Ke -" +str(i+1))
    list_nim.append(input("Masukan Nilai Nim anda :"))
    list_uts.append(int(input("Masukan Nilai UTS anda :")))
    list_uas.append(int(input("Masukan UAS anda :")))
#Proses
for i in range(ulang):
    list_total.append((list_uas[i] + list_uts[i])/2)

#Cetak
print("==================================")
print("Nim  nilai uts   nilai uas   total")
print("==================================")
for i in range(ulang):
    print("%s\t%i\t\t%i\t\t\t%i"% (list_nim[i],list_uts[i], list_uas[i], list_total[i]))

print("==============================================")