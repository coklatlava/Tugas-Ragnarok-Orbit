# -*- coding: utf-8 -*-
"""Rabu_02_Maret_Pagi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1viB6iz-3LcAiBXvXjG-bxRPtmmT1IqKt

NOMOR 1
"""

a = False
b = True
c = False

print(b and c)
print(b or c)
print(not a and b)
print((a and b) or not c)
print(not b and not c (a or c))

"""NOMOR 2"""

print('Hello!')
something = input("Enter something: ")
print(('You entered: ', something))

"""NOMOR 3"""

print('Hallo!')
something = input("Enter something: ")
if something == 'hello':
  print("Hello for you too!")

elif something == 'hi':
  print('Hi there')
else:
  print("I don't know what", something, "means.")

"""NOMOR 4"""

ulang = 100

for i in range(ulang):
    print(f"Halo hai ke-{i}")

"""NOMOR 5"""

from random import randint
t = ["Batu", "Kertas", "Gunting"]
computer = t[randint(0,2)]
player = False
 
while player == False:

    player = input("Batu, Gunting, Kertas ? ")
    if player == computer:
        print("Seri!")
    elif player == "Batu":
        if computer == "Kertas":
            print("Anda Kalah!", computer, "menutup", player)
        else:
            print("Anda Menang!", player, "memukul", computer)
    elif player == "Kertas":
        if computer == "Gunting":
            print("Anda Kalah!", computer, "memotong", player)
        else:
            print("Anda Menang!", player, "menutup", computer)
    elif player == "Gunting":
        if computer == "Batu":
            print("Anda Kalah...", computer, "memukul", player)
        else:
            print("Anda Menang!", player, "memotong", computer)
    else:
        print("Input tidak valid!. Gunakan “batu”, “ gunting” dan “kertas” tanpa tanda kutip!")

    player = False
    computer = t[randint(0,2)]

"""NOMOR 6"""

jawab = 'lanjut'
hitung = 0

while(True):
    hitung += 1
    jawab = input("Lanjut atau berhenti ? ")
    if jawab == 'berhenti':
        break

print(f"Total perulagan: {hitung}")

"""NOMOR 7"""

menu = "y" or "Y"
while menu == "y" or "Y":
    print(" ========================================")
    print(" Selamat Datang")
    print(" List Jajanan Pasar")
    print(" ========================================")
    print(" 1. Donat               : Rp 1.250")
    print(" 2. Bakwan              : Rp 1.000")
    print(" 3. Onde-onde           : Rp   800")
    print(" 4. Lemper              : Rp 1.250")
    print(" 5. Risol               : Rp.1.500")
    print(" ========================================")
    listMenu=str(input(" Masukkan angka sesuai dengan menu yang tersedia = "))
    jumlahPesanan=int(input(" Jumlah = "))
    if listMenu == "1":
        namaMenu= " Donat "
        harga=(1250*jumlahPesanan)
        if jumlahPesanan >= 5:
            totalHarga=int(harga)
        else:
            totalHarga=int(harga)
    elif listMenu == "2":
        namaMenu= " Bakwan "
        harga = (1000*jumlahPesanan)
        if jumlahPesanan >= 5:
            totalHarga =int(harga)
        else:
            totalHarga =int(harga)
    elif listMenu == "3":
        namaMenu= " Onde-onde "
        harga=int(800*jumlahPesanan)
        totalHarga=int(harga)
    elif listMenu == "4":
        namaMenu= " Lemper"
        harga=int(1250*jumlahPesanan)
        totalHarga = int(harga)
    elif listMenu == "5":
        namaMenu= " Risol"
        harga=int(1500*jumlahPesanan)
        totalHarga = int(harga)
    else:
        menu=input(" Maaf,Menu yang dipilih tidak tersedia di sini")

    print(" kamu memesan",namaMenu)
    print(" dengan harga", harga)
    jawab = input(" Lanjut atau cukup ? ")
    if jawab == 'cukup':
      break

print(f"Terima kasih sudah berbelanja jajanan pasar kami!")

"""NOMOR 8"""

menu = "y" or "Y"
while menu == "y" or "Y":
    print(" ========================================")
    print(" Selamat Datang")
    print(" List Jajanan Pasar")
 
    print(" ========================================")
    print(" 1. Donat               : Rp 1.250")
    print(" 2. Bakwan              : Rp 1.000")
    print(" 3. Onde-onde           : Rp   800")
    print(" 4. Lemper              : Rp 1.250")
    print(" 5. Risol               : Rp.1.500")
    print(" ========================================")
    listMenu=str(input(" Masukkan angka sesuai dengan menu yang tersedia = "))
    jumlahPesanan=int(input(" Jumlah = "))
    if listMenu == "1":
        namaMenu= " Donat "
        harga=(1250*jumlahPesanan)
        if jumlahPesanan >= 5:
            totalHarga=int(harga)
        else:
            totalHarga=int(harga)
    elif listMenu == "2":
        namaMenu= " Bakwan "
        harga = (1000*jumlahPesanan)
        if jumlahPesanan >= 5:
            totalHarga =int(harga)
        else:
            totalHarga =int(harga)
    elif listMenu == "3":
        namaMenu= " Onde-onde "
        harga=int(800*jumlahPesanan)
        totalHarga=int(harga)
    elif listMenu == "4":
        namaMenu= " Lemper"
        harga=int(1250*jumlahPesanan)
        totalHarga = int(harga)
    elif listMenu == "5":
        namaMenu= " Risol"
        harga=int(1500*jumlahPesanan)
        totalHarga = int(harga)
    else:
        menu=input(" Maaf,Menu yang dipilih tidak tersedia di sini")
 
    print(" ------------------------------")
    print(" Menu :",namaMenu)
    print(" Jumlah Pesanan :", jumlahPesanan)
    print(" Harga :", harga)
    print(" ------------------------------")
    print(" Total Pembayaran :", totalHarga)
    print(" ------------------------------")
    menu=input(" Mau pesan lagi? pilih Y jika Ya, pilih N jika Tidak (Y/N) = ")

