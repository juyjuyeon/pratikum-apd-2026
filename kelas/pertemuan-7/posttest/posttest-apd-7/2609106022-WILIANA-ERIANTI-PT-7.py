print("====== SeriesView Yuk!=======")

import os
username = "wili"
password = "1234567890"
limit_login = 3

data_fitur = { 
    "CreView" : "Kamu bisa buat review tentang series atau film yang sudah kamu tonton",
    "SeeView" : "Kamu bisa melihat review yang sudah ada",
    "UpView" : "Kamu bisa update review yang sudah di posting",
    "DelView" : "Kamu bisa menghapus review yang sudah di posting",
    "Keluar" : "Keluar dari program"
}

def masukkan_data(): 
    judul = input("masukkan judul : ")
    rating = input("masukkan rating film/series 1-10: ")
    ulasan = input("masukkan review : ")
    return {"judul": judul, "rating": rating, "ulasan": ulasan}

def sapa_pengguna(username_input): 
    nama = username_input
    return nama

def batas_login(batas, percobaan):
    sisa_login = batas - (percobaan + 1)
    return sisa_login

def cetak_garis():
    print("=" * 30)

def total_review(): 
    total = len(daftar_review)
    print("review yang anda miliki adalah ", total)
    return total

def bersihkan_layar(): 
    os.system('cls')

def tampilkan_fitur(data_fitur):
    nomor = 1
    for key in data_fitur:
        print(f"{nomor}. {key} : {data_fitur[key]}")
        nomor += 1

def tampilkan_review(daftar_review): 
    print("=== Review anda saat ini ===")
    for i, review in enumerate (daftar_review):
        print(f"{i + 1}. {review}")

def keluar_menu():
    exit()

for i in range(limit_login):
    username_input = input("Masukkan username: ")
    password_input = input("Masukkan password: ")
    if username_input == username and password_input == password:  
        print("=== Selamat datang", sapa_pengguna(username_input),"===")
        break
    else: 
        print("Username atau password salah. Silakan coba lagi.")
        sisa_login = batas_login(limit_login, i)
        print("sisa percobaan login anda", sisa_login)
        if sisa_login == 0:
            print("=== Percobaan login habis. Silahkan coba lagi nanti ===")
            keluar_menu()


input("tekan enter untuk melanjutkan...")
bersihkan_layar()

cetak_garis()

input_review = "ya"
daftar_review = []

while True: 
    tampilkan_fitur(data_fitur)
    pilih_fitur = input("pilih menu yang ingin digunakan : ")
    if pilih_fitur == "1":
        while input_review.lower() == "ya":
            review = masukkan_data()
            daftar_review.append(review)
            input_review = input("mau masukkan review lagi? (ya/tidak) : ")
            print("review berhasil ditambahkan!")
            tampilkan_review(daftar_review)
            total_review()
            cetak_garis()
    elif pilih_fitur == "2": 
        for i, all_review in enumerate (daftar_review):
            print(f"{i + 1}. {all_review}")
        total_review()
    elif pilih_fitur == "3": 
        if len(daftar_review) == 0: 
            print("Belum ada review yang bisa diubah")
        else: 
            print("daftar review terbaru")
            tampilkan_review(daftar_review)
            nomor_ubah = input("masukkan nomor yang ingin diubah : ")
            if nomor_ubah.isdigit(): 
                nomor_ubah = int(nomor_ubah)
                if 1 <=  nomor_ubah <= len(daftar_review):
                    indeks = nomor_ubah - 1
                    review_baru = input(f"masukkan review baru untuk {nomor_ubah}: ")
                    daftar_review[indeks]["ulasan"] = review_baru
                    print("review berhasil di update!")
                    print(daftar_review)
                    total_review()
                else: 
                    print("masukkan angka yang valid!")
            else: 
                print("nomor review tidak valid")
    elif pilih_fitur == "4": 
        if len(daftar_review) == 0: 
            print("tidak ada yang bisa dihapus")
        else: 
            print("daftar review terbaru")
            tampilkan_review(daftar_review)
            nomor_hapus = int(input("masukkan nomor yang ingin dihapus: "))
            if 1 <= nomor_hapus <= len(daftar_review): 
                try: 
                    nomor_hapus
                except ValueError: 
                    print("masukkan angka!")
                indeks = nomor_hapus - 1
                del daftar_review[indeks]
                print(daftar_review)
                total_review()
            else: 
                print("nomor review tidak valid")
    elif pilih_fitur == "5":  
        keluar_menu()
    else: 
        print("masukkan nomor menu yang valid!")

