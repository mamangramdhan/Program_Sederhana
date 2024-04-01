def Tambah(x,y):
    return x+y

def Kurang(x,y):
    return x-y

def Kali(x,y):
    return x*y

def Bagi(x,y):
    return x/y

print("#"*33)
print("#\t1.Penambahan\t\t#")
print("#\t2.Penambahan\t\t#")
print("#\t3.Penambahan\t\t#")
print("#\t4.Penambahan\t\t#")
print("#"*33)

while True:
    Menu = input("Pilih Angka (1/2/3/4) : ")
    if Menu in ('1','2','3','4'):
        try:
            Num1 = int(input("Masukan Nilai X : "))         
            Num2 = int(input("Masukan Nilai Y : "))         
        except ValueError:
            print("Masukan Nilai Angka")
            continue

    if Menu == '1':
        print(f"Hasil Dari {Num1} + {Num2} = ", Tambah(Num1,Num2))
    elif Menu == '2':
        print(f"Hasil Dari {Num1} - {Num2} = ", Kurang(Num1,Num2))
    elif Menu == '3':
        print(f"Hasil Dari {Num1} x {Num2} = ", Kali(Num1,Num2))
    elif Menu == '4':
        print(f"Hasil Dari {Num1} : {Num2} = ", Bagi(Num1,Num2))
    else:
        print("Menu Tidak Tersedia")
        continue

    Tanya = input("Apakah Ingin Lanjut ? (Y/y) (T/t) : ")
    if Tanya == 'Y' or Tanya == 'y':
        continue
    elif Tanya == 'T' or Tanya == 't':
        print("Terimakasih")
        break
    else:
        print("Perintah Salah")