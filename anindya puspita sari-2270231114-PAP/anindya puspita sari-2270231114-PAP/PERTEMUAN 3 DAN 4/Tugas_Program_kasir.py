import sys
total = []

print("--------------------------------")
print("------WARUNG MAKAN DOA IBU------")
print("--------------------------------")

input("Tanggal pembelian: ")
nama = input("Nama kasir: ")
nama = input("Nama Pembeli: ")
print("JL.ABDUL MUIS NO.68 JAKARTA PUSAT")
print("Telp. 021-3505574")
print("-------------------------------")

def daftar_barang():
    print(" No | Nama Barang | Harga")
    print("-------------------------------")
    print(" 1  | Ayam Geprek        | 15000")
    print(" 2  | Ayam Goreng        | 15000")
    print(" 3  | Ayam Penyet        | 18000")
    print(" 4  | Ayam Bakar         | 18000")
    print(" 5  | Ayam Sambal Matah  | 20000")
    print(" 6  | Bebek Goreng       | 20000")
    print(" 7  | Bebek Bakar        | 22000")
    print(" 8  | Bebek Penyet       | 22000")
    print(" 9  | Bebek Rica rica    | 25000")
    print(" 10 | Es Teh Manis       | 5000")
    print(" 11 | Es Jeruk           | 8000")
    print(" 12 | Teh Manis Hangat   | 6000")
    print(" 13 | Ovaltine           | 10000")
    print(" 14 | Good Day           | 10000")
    print(" 15 | Air Mineral        | 5000")
    print("-------------------------------")
    kode = int(input("Masukkan angka barang  : "))
    if kode == 1:
        jumlah1 = int(input("Masukkan jumlah barang : "))
        total1 = 15000 * jumlah1
        total.append(total1)
        tanya()
    elif kode == 2:
        jumlah2 = int(input("Masukkan jumlah barang : "))
        total2 = 15000 * jumlah2
        total.append(total2)
        tanya()
    elif kode == 3:
        jumlah3 = int(input("Masukkan jumlah barang : "))
        total3 = 18000 * jumlah3 
        total.append(total3)
        tanya()
    elif kode == 4:
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 18000 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 5:
        jumlah5 = int(input("Masukkan jumlah barang : "))
        total5 = 20000 * jumlah5   
        total.append(total5)
        tanya()
    elif kode == 6:
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 20000 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 7:
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 22000 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 8:
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 22000 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 9:
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 25000 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 10:
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 5000 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 11:
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 6000 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 12:
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 8000 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 13:
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 10000 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 14:
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 10000 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 15:
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 5000 * jumlah4
        total.append(total4)
        tanya()
    return

def tanya():
    print("\n-------------------------------")
    tanya = input("Ingin tambah barang? [y/t] : ")
    print("-------------------------------")
    if tanya == "y":
        daftar_barang()
    elif tanya == "t":
        akhir()
    else:
        print("Pilihan yang anda masukan salah!")

def akhir():
    for harga in total:
        print("SubTotal         : ", sum(total))
        diskon = 0
        a = sum(total)
        if a > 500000:
            diskon = a * 8/100
        elif a > 300000:
            diskon = a * 5/100
        elif a > 200000:
            diskon = a * 3/100
        elif a > 100000:
            diskon = a * 1/100
        else:
            diskon = 0
        print("Potongan Harga   : ", diskon)
        totalakhir = a - diskon
        print("Total            : ", totalakhir)
        print("-------------------------------")
        bayar = int(input("Bayar            :  "))
        kembalian = bayar - totalakhir
        print("Kembalian        : ", kembalian)
        print("-------------------------------")
        print("          Terima Kasih         ")
        print("-------------------------------")

daftar_barang()