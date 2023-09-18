gol1 = 3000
gol2 = 3500
gol3 = 4000
gol4 = 5000
while True:
  gol = int(input("Masukkan golongan anda (1-4): "))
  if (gol == 1 or gol == 2 or gol == 3 or gol == 4):
    break
  else:
    print("Masukan golongan yang benar!!")

jam = int(input("Masukkan berapa lama jam kerja anda: "))
if (gol == 1):
  gaji = gol1 * jam
  if (jam > 40):
    gaji = 40 * gol1 + (jam - 40) * gol1 * 1.01
elif (gol == 2):
  gaji = gol2 * jam
  if (jam > 40):
    gaji = 40 * gol2 + (jam - 40) * gol2 * 1.01
elif (gol == 3):
  gaji = gol3 * jam
  if (jam > 40):
    gaji = 40 * gol3 + (jam - 40) * gol3 * 1.01
elif (gol == 4):
  gaji = gol4 * jam
  if (jam > 40):
    gaji = 40 * gol4 + (jam - 40) * gol4 * 1.01
  

print(f"\nGajimu = Rp.{int(gaji)}")
