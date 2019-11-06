a = int()
maks = 0
while a >= 0:
    a = int(input("Masukan bilangan :"))
    if a > maks :
            maks = a
    if a == 0:
        break
print ("Angka terbesar adalah :",maks)
