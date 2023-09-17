#Nama: Dave Koagow
#Prodi: Informatika
#Kelas: Komputer Programing
#Tanggal Pembuatan: 17-Sep-2023

### SOAL 1 ###
from time import sleep as timeout
from random import *

rand = int(uniform(1, 2))
print("S", end = "")
timeout(rand)
print("O", end = "")
timeout(rand)
print("A", end = "")
timeout(rand)
print("L", end = "")
timeout(rand)
print(" 1\n")
timeout(2)

masuk = int(input("Masukan jam masuk (format 23 jam): "))
keluar = int(input("Masukan jam keluar (format 23 jam): "))
parkir1 = 2000 #2 jam pertama
parkir2 = 500 #per jam berikutnya
lama_parkir = keluar - masuk
if (lama_parkir < 2):
  biaya = parkir1
  print(f"Biaya parkir = Rp.{biaya}")
else:
  biaya = parkir1 + (lama_parkir - 2) * parkir2
  print(f"Biaya parkir = Rp.{biaya}")
