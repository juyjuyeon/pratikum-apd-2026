
nama_panggilan = input("Nama Panggilan : ")
nim = input("NIM : ")

if nama_panggilan == "wili" and nim == "22":
    print("Pilih Jenis BBM : ")
    print("1. Pertalite = 10.000")
    print("2. Pertamax = 12.500")
    print("3. Pertamax Turbo = 15.000")

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

        if jumlah_liter >= 10:
            Diskon = Total_Harga * 0.10          
        elif jumlah_liter <= 5:
            Diskon = Total_Harga * 0.05
        else:
            Diskon = 0  

        Status_Keanggotaan = input("Status Keanggotaan (Ya/Tidak): ")
        if  Status_Keanggotaan == "Ya":
            Status_Keanggotaan = "Member"
            Diskon_member = Total_Harga * 0.02
        else:
            Status_Keanggotaan = "Non-Member"
            Diskon_member = 0
        Total_Diskon = Diskon + Diskon_member
        Total_Harga = Total_Harga - Total_Diskon

        Total_Bayar = Total_Harga - Diskon 
        print("\n--- Total Pembayaran ---")
        print(f"Total Harga : Rp{int(Total_Harga):,}".replace(",", "."))
        print(f"Diskon      : Rp{int(Diskon):,}".replace(",", "."))
        print(f"Total Bayar : Rp{int(Total_Bayar):,}".replace(",", "."))

else:
    print("Login Gagal, Silahkan coba lagi") 

garis1 = "-" * 88
garis2 = "=" * 88

print("\n" + garis2)
print("                                 STRUK TRANSAKSI BBM                                  ")
print(garis1)
print(f" Nama_Panggilan  : {nama_panggilan}")
print(f" NIM             : {nim}")
print(f" Status Member   : {Status_Keanggotaan}")
print(garis2)
print(f"| {'Pilihan_BBM':<15} | {'Harga/L':<10} | {'Liter':<7} | {'Total Awal':<12} | {'Total Diskon':<12} | {'Total Bayar':<12} |")
print(garis1)
print(f"| {pilihan_bbm:<15} | Rp{harga_bbm_per_liter:<8} | {jumlah_liter:<7.1f} | Rp{Total_Harga:<10.0f} | Rp{Total_Diskon:<10.0f} | Rp{Total_Bayar:<10.0f} |")
print(garis2)
print(" Rincian Diskon:")
print(f" - Diskon Pembelian : Rp {Diskon:,.0f}")
print(f" - Diskon Member    : Rp {Diskon_member:,.0f}")
print(garis2)
        

