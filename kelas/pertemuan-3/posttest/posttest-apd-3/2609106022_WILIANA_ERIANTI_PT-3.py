
print("Nota Transaksi BBM")
nama_panggilan = input("Nama Panggilan : ")
nim = input("NIM : ")

if nama_panggilan == "wili" and nim == "22":
    print("Pilih Jenis BBM : ")
    print("1. Pertalite = 10.000")
    print("2. Pertamax = 12.500")
    print("3. Pertamax Turbo = 15.000")
else: 
    print("Login Gagal, Silahkan coba lagi")

pilihan_bbm = input("Masukkan pilihan BBM (1/2/3): ")
jumlah_liter = float(input("Jumlah Liter: "))

if pilihan_bbm == "1":
    harga_bbm_per_liter = 10000
elif pilihan_bbm == "2":
    harga_bbm_per_liter = 12500  
elif pilihan_bbm == "3":
    harga_bbm_per_liter = 15000
else:
    print("Pilihan BBM tidak valid.")

if harga_bbm_per_liter > 0:
    Total_Harga = harga_bbm_per_liter * jumlah_liter
    
if jumlah _liter >= 10:
    Diskon = Total_Harga * 0.1  # Misalnya diskon 10%   
elif jumlah_liter >= 5:
    Diskon = Total_Harga * 0.2  # Misalnya diskon 20%
else:
    Diskon = 0  
    print("Tidak ada diskon untuk pembelian kurang dari 5 liter.")
    

Total_Harga = harga_bbm_per_liter * jumlah_liter
Diskon = Total_Harga * 0.1  # Misalnya diskon 10%
Total_Bayar = Total_Harga - Diskon
