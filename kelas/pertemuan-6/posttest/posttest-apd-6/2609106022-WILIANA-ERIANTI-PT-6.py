print("====== SeriesView Yuk!=======")

username = "wili"
password = "1234567890"
batas = 3

for i in range(batas):
    username_input = input("Masukkan username: ")
    password_input = input("Masukkan password: ")
    if username_input == "wili" and password_input == "1234567890": 
        print("=== Login berhasil! ===")
        break
    else: 
        print("Username atau password salah. Silakan coba lagi.")
        sisa = batas - (i + 1)
        if sisa == 0:
            print("=== Percobaan login habis. Silahkan coba lagi nanti ===")
            exit()

input("tekan enter untuk melanjutkan...")
import os
os.system("cls")

garis = "=" * 23
print(garis)
fitur = { 
    "CreView" : "Kamu bisa buat review tentang series atau film yang sudah kamu tonton",
    "SeeView" : "Kamu bisa melihat review yang sudah ada",
    "UpView" : "Kamu bisa update review yang sudah di posting",
    "DelView" : "Kamu bisa menghapus review yang sudah di posting"
}
for key, value in fitur.items(): 
    print(f"{key} : {value}")
input_review = "ya"
daftar_review = []
semua_review = [daftar_review]
while True: 
    print("==== menu ====")
    print("1. CreView")
    print("2. SeeView")
    print("3. UpView")
    print("4. DelView")
    print("5. Keluar")
    pilih_fitur = input("pilih menu yang ingin digunakan : ")
    if pilih_fitur == "1":
        while input_review == "ya":
            input_lagi = input(f"masukkan judul : ") 
            input_rating = input(f"masukkan rating film/series 1-10: ")
            input_ulasan = input(f"masukkan review : ")
            daftar_review.append({"judul" : input_lagi, "rating" : input_rating, "ulasan" : input_ulasan})
            input_review = input("mau masukkan review lagi? (ya/tidak) ")
            if input_review == "ya": 
                break
            for i, review in enumerate (daftar_review):
                print(f"{i + 1}. {review}")
    elif pilih_fitur == "2": 
        for i in semua_review:
            print(i)
    elif pilih_fitur == "3": 
        if len(daftar_review) == 0: 
            print("Belum ada review yang bisa diubah")
        else: 
            print("daftar review terbaru")
            for i, review in enumerate (daftar_review):
                print(f"{i + 1}. {review}")
            nomor_ubah = input("masukkan nomor yang ingin diubah : ")
            if nomor_ubah.isdigit(): 
                nomor_ubah = int(nomor_ubah)
                if 1 <=  nomor_ubah <= len(daftar_review):
                    indeks = nomor_ubah - 1
                    review_baru = input(f"masukkan review baru untuk {nomor_ubah}: ")
                    daftar_review[indeks]["ulasan"] = review_baru
                    print("review berhasil di update!")
                    print(semua_review)
                else: 
                    print("masukkan angka yang valid!")
            else: 
                print("nomor review tidak valid")
    elif pilih_fitur == "4": 
        if len(daftar_review) == 0: 
            print("tidak ada yang bisa dihapus")
        else: 
            print("daftar review terbaru")
            for i, review in enumerate(daftar_review): 
                print(f"{i + 1}. {review}")
            nomor_hapus = int(input("masukkan nomor yang ingin dihapus: "))
            if 1 <= nomor_hapus <= len(daftar_review): 
                indeks = nomor_hapus - 1
                del daftar_review[indeks]
                print(semua_review)
            else: 
                print("nomor review tidak valid")
    elif pilih_fitur == "5":  
        exit()
    else: 
        print("masukkan nomor menu yang valid!")

