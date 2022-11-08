def Biodata(tahun, nama, asal):
    tahun_sekarang = 2020
    print("\nPerkenalkan Nama Saya :", nama)
    print("Umur Saya :", tahun_sekarang - tahun)
    print("Saya adalah Angkatan:", tahun_sekarang)
    print("Asal Saya dari :", asal)

for i in range(2):
    tahun = int(input())
    nama = input()
    asal = input()
    Biodata(tahun, nama, asal)
    print("\n")