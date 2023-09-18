R1 = int(input("Masukan R1: "))
R2 = int(input("Masukan R2: "))
R3 = int(input("Masukan R3: "))
inp = input("Ketik seri/paralel!\nBisa juga dengan memilih 1 untuk seri dan 2 utk paralel..\n> ")
if (inp == "seri" or inp == "1"):
  hasil = R1 + R2 + R3
  print(f"Jumlah Resistor = {hasil}")
elif (inp == "paralel" or inp == "2"):
  rgab = 1/R1 + 1/R2 + 1/R3
  hasil = 1/rgab
  print(f"Jumlah Resistor = {hasil}")
else:
  print("Terjadi kesalahan..")
  
