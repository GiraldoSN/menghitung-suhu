print("Penghitung Luas Bangun Ruang")

def menu ():
    print ("Pilih Bangun Ruang")
    print ("Masukkan angka 1-7")
    print ("1. Kubus")
    print ("2. Balok")
    print ("3. Limas")
    print ("4. Prisma")
    print ("5. Tabung")
    print ("6. Kerucut")
    print ("7. Bola")

from tracemalloc import start

#start
#print('volume\n')
#print('+'*100, '\n')

#rumus volume = sisi*sisi*sisi
sisi = float(input("masukkan sisi bangun ruang : "))
volume = sisi*sisi*sisi
print("volume kubus adalah : ",volume)
print("\n")
#luas kubus 
luas=6*sisi*sisi
print("luas kubus adalah : ", luas)
print("\n")
#volume balok
panjang=float(input("masukkan panjang balok : "))
lebar=float(input("masukkan lebar balok : "))
tinggi=float(input("masukkan tinggi balok : "))
rumus=panjang*lebar*tinggi
print("volume balok adalah : ", rumus)