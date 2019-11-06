#Penjelasan Alur algoritma Latihan1.py

num = int(input("Masukan Nilai N:")) --> input yang dimasukan

from random import random           --> Untuk menghasilkan Nilai random yang dibuat oleh sistem komputer
a = random()

jumlah = num+1           |
start = 0                |       --> Logika 
stop = jumlah            |   
step = 1                 |
for i in range ( start, stop, step):  --> Comand (for) untuk perulangan (i) untuk variabel didalam range
    print("Data ke:", i, "->",(a))    --> Output atau menghasilkan hasil yang akan dikeluarkan
print("Selesai")                      --> Output tambahan


#Penjelasan Alur algoritma Latihan2.py

a = int()                                   --> variabel bebas
maks = 0                                    --> Nilai yang digunakan untuk berhenti
while a >= 0:                               --> (While)Digunakan untuk perulangan jika lebih dari 0 akan dilakukan perulangan pada program input.
    a = int(input("Masukan bilangan :"))    --> input yang dimasukan
    if a > maks :                          |
            maks = a                       |
    if a == 0:                             |-->Logika dan jika diinputkan 0 maka program akan berhenti
        break                              |
print ("Angka terbesar adalah :",maks)      --> Output untuk hasil angka terbesar (Diambil dari variabel maks)


#Penjelasan Alur Algoritma Program1.py

modal = 100000000                                  --> input awal modal
laba = 0                                           --> Laba awal
untung = 0                                         --> Untung awal
for i in range (1,9,1):                            --> Comand (For) untuk perulangan di dalam range
  if(i<3):                                          ~~~~~~~~~|
    laba =0                                         ~~~~~~~~~|
    untung = untung + laba                          ~~~~~~~~~|
  elif (i<5):                                       ~~~~~~~~~|
    laba = modal*1/100                              ~~~~~~~~~| 
    untung = untung + laba                          ~~~~~~~~~|  LOGIKA
  elif (i<8):                                       ~~~~~~~~~|
    laba = modal*5/100                              ~~~~~~~~~|
    untung = untung + laba                          ~~~~~~~~~|
  else :                                            ~~~~~~~~~|
    laba = modal*2/100                              ~~~~~~~~~|
    untung = untung + laba                          ~~~~~~~~~|
  print ("Laba bulan Ke - ",i,"Sebesar", laba)     --> Output hasil laba
print ("Total laba adalah : " , untung )           --> Output Total laba