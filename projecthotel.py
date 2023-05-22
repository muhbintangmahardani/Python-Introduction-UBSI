from datetime import datetime, date
from threading import Thread
import threading

#pendefinisian class dengan nama Hotel
class Hotel:
    #inisialisasi 5 object pada class
    def __init__(self, hotel_type= '', check_in= '00-00-0000', days= 0, member= '', harga= 0.0):
        self._hotel_type= hotel_type
        self._check_in= check_in
        self._days= days
        self._member= member
        self._harga= harga
    #inheritance pewarisan method prenotasi kedalam output
    def __str__(self):
        return '\n\nSPESIFIKASI PEMESANAN\n\nNama Hotel : %s\nCheck in pada tanggal: %s\nLama menginap: %s malam\nHarga total: Rp %d.000,00\n' % (self._hotel_type, self._check_in, self._days, self._harga)

#enkapsulasi tiap object dengan getter dan setter
    #setter object hotel
    def set_hotel_type (self, hotel_type):
        while True:
            try:
                try:                
                    rooms = open ('rooms.txt', 'r')
                except IOError:
                    print ('Gagal membuka file Hotel\n')
                listing = [] 
                for daftar in rooms:                  
                    room = daftar.strip()
                    listing.append(room) 
                rooms.close()
                print ('\nSilahkan pilih hotel yang anda inginkan:')
                room=input('')
                if room in listing:
                    hotel_type= room 
                    self._hotel_type= hotel_type
                    break
                elif room.islower(): 
                    raise ValueError
                else:
                    print('Mohon maaf, silahkan pilih hotel yang tersedia pada menu\n')           
            except ValueError:
                print('Tuliskan pilihan dengan karakter sesuai dengan pilihan\n')


    #getter object hotel
    def get_hotel_type (self):
        return self._hotel_type

    #setter check in
    def set_check_in (self, check_in):
        date_today = date.today()
        print('Silahkan masukkan tanggal anda hendak melakukan Check In :')
        while True:
            data = select_date()
            if data >= date_today:          
                check_in = data
                self._check_in = check_in
                break
            else:
                print('\nMaaf, kamar sudah tidak tersedia pada tanggal tersebut\n')

    #getter check in
    def get_check_in (self):
        return self._check_in

    #setter tanggal
    def set_days(self, days):
        while True:
            try:
                print ('Berapa malam anda hendak menginap di hotel?')
                ndays=int(input(''))
                if ndays >= 1:
                    days=ndays
                    self._days= days
                    break
                else:
                     ndays = 0
                     print ('Mohon masukkan data dengan benar')

            except ValueError:
                print ('Masukkan karakter angka!')

    #getter tanggal
    def get_days (self):
        return self._days

    #setter member
    def set_member(self, apa_member):
        while True:
            try:
                print ('Apakah anda ingin memesan sebagai member? (ya/tidak)')
                apa_member = input ('')
                if apa_member == 'ya':
                    member = apa_member
                    self._member = member
                    break
                elif apa_member == 'tidak':
                    member = apa_member
                    self._member = member
                    break
                elif apa_member.islower(): 
                    raise ValueError
                else:
                     apa_member != 'ya' or 'tidak'
                     print('Masukkan antara ya atau tidak!\n')            
            except ValueError:
                print('Masukkan antara ya atau tidak!\n')

    #getter member
    def get_member(self):
        return self._member

    #setter harga
    def set_harga(self, harga):
        try:
            cal_price= open ('price_rooms.txt', 'r') 
        except IOError:
            print ('Gagal membuka file harga hotel')
        for tipe in cal_price:
            daftar= tipe.strip()
            listing= tipe.split()
            if listing[0] == self._hotel_type and listing[1] == self._member: 
                harga = float(listing [2])*self._days
                self._harga = harga
                break
        cal_price.close()

#polymorphism check_in dengan method select_date
def select_date():
    date_today = date.today() 
    tahun = date_today.year 
    while True:
        try:
            print('Masukkan tanggal (1-30) :')
            day = int(input(''))
            print('Masukkan bulan (1-12):')
            month = int(input(''))
            while True:
                try:
                    print('Masukkan tahun : (harus tahun ini atau tahun mendatang)')
                    year = int(input(''))
                    if tahun <= year: 
                        break
                    else:
                        if year < tahun:
                            print('Masukkan data dengan benar!')
                except ValueError:
                    print('Masukkan karakter angka')
            data = date(year, month, day)  
            break
        except ValueError:
            print('Masukkan data dengan benar')
    return data

#method pemanggilan tiap pbject ke dalam kesimpulan terakhir
def prenotazione (sema, op):
    sema.acquire() 
    op.set_hotel_type('hotel_type')
    op.set_check_in('check_in')
    op.set_days('days')
    op.set_member('member')
    op.set_harga('harga')
    print(op)
    global a, b, c, d
    if op._hotel_type == 'hotelA' and a > 0:
        a = a -1
    elif op._hotel_type == 'hotelB' and b > 0:
        b = b -1
    elif op._hotel_type == 'hotelC' and c > 0:
        c = c -1
    elif op._hotel_type == 'hotelD' and d > 0:
        d = d -1
    else:
        print ('Mohon maaf, pilihan hotel belum tersedia')

    sema.release() 

print('Selamat datang di Sistem Pemesanan Hotel \n\nBerikut daftar hotel yang tersedia di lokasi anda : \n')

try:
    roomsdisp = open('rooms.txt','r')
except IOError:
    print ('Gagal memuat file Hotel')
listing = []
for daftar in roomsdisp:
    rooms = daftar.strip() 
    listing.append(rooms) 
    print (rooms)
roomsdisp.close()   

a= 1 
b= 2
c= 1
d= 1
#polymorphism class Hotel
reservation= Hotel () 
sema = threading.Semaphore (1)
t1 = Thread(target = prenotazione, args = (sema, reservation,)) 
reservation2 = Hotel()
t2 = Thread(target = prenotazione, args = (sema, reservation2,))
reservation3 = Hotel()
t3 = Thread(target =prenotazione, args = (sema,reservation3,))

t1.start()
t2.start()
t3.start()