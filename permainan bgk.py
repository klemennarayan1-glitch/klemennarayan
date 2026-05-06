import random

def permainan_bgk():
    pilihan = ['Batu', 'Gunting', 'Kertas']
    komputer = random.choice(pilihan)
    pemain = input("Masukan pilihanmu (Batu, Gunting, Kertas): ").lower()

    print(f"Komputer memilih: {komputer}")

    if pemain == komputer:
        print("Seri!")
    elif (pemain == 'batu' and komputer == 'Gunting') or \
         (pemain == 'gunting' and komputer == 'Kertas') or \
         (pemain == 'kertas' and komputer == 'Batu'):
        print("Kamu Menang!")
    else:
        print("Komputer Menang!")

permainan_bgk()