username = "wili"
password = "22"
batas = 3

print("====== login ======")
for i in range(batas):
    username_input = input("Masukkan username: ")
    password_input = input("Masukkan password: ")
    if username_input == "wili" and password_input == "22":
        print("=== Login berhasil! ===")
        break
    else:
        print("Username atau password salah. Silakan coba lagi.")
        sisa = batas - (i + 1)
        if sisa == 0:
            print("Percobaan login habis. Program dihentikan.")
            exit()  
            
print("====== input data siswa ======")

nama_siswa = input("masukkan nama siswa : ")
kelas_siswa = input(f"masukkan kelas siswa {nama_siswa} : ")

mengikuti_ujian_atau_tidak = "ya" or "tidak"
while mengikuti_ujian_atau_tidak == "ya":
    mengikuti_ujian_atau_tidak = input(f"apakah siswa {nama_siswa} mengikuti ujian? : ")
    if mengikuti_ujian_atau_tidak == "ya":
        jumlah_benar = int(input(f"jumlah jawaban benar {nama_siswa} : "))
        jumlah_salah = int(input(f"jumlah jawaban salah {nama_siswa} : "))
        nilai_ujian = jumlah_benar * 5  
        print(f"siswa {nama_siswa} nilai ujian {nilai_ujian}")
    else:
        print(f"siswa {nama_siswa} nilai ujian 0")  
        break
        if nilai_ujian >= 80:
            print(f"nilai ujian sangat baik")
        elif nilai_ujian >= 60:
            print(f"nilai ujian baik")
        elif nilai_ujian >= 40:
            print(f"nilai ujian cukup")
        else: 
            print(f"perlu belajar lagi")
    break 

perlu_input_data = "ya"

perlu_input_data = "ya"
print("====== input data siswa ======")

while perlu_input_data == "ya":
    nama_siswa = input("masukkan nama siswa : ")
    kelas_siswa = input(f"masukkan kelas siswa {nama_siswa} : ")
    
    mengikuti_ujian_atau_tidak = input("apakah siswa mengikuti ujian? (ya/tidak) : ")
    
    if mengikuti_ujian_atau_tidak == "tidak":
        print(f"siswa {nama_siswa} nilai ujian 0")
    else:
        jumlah_benar = int(input(f"jumlah jawaban benar {nama_siswa} : "))
        jumlah_salah = int(input(f"jumlah jawaban salah {nama_siswa} : "))
        nilai_ujian = jumlah_benar * 5
        print(f"siswa {nama_siswa} nilai ujian {nilai_ujian}")
        
        if nilai_ujian >= 80:
            print("nilai ujian sangat baik")
        elif nilai_ujian >= 60:
            print("nilai ujian baik")
        elif nilai_ujian >= 40:
            print("nilai ujian cukup")
        else:
            print("perlu belajar lagi")
            
    print("-" * 30)
    perlu_input_data = input("apakah perlu input data lagi? (ya/tidak) : ")

print("Selesai menginput data.")

pengelompokkan_kelas = {
    "Kelas A": [
            {"nama_siswa": nama_siswa, "kelas_siswa": kelas_siswa, "mengikuti_ujian_atau_tidak": mengikuti_ujian_atau_tidak, "nilai_ujian": nilai_ujian}
    ],
    "Kelas B": [
            {"nama_siswa": nama_siswa, "kelas_siswa": kelas_siswa, "mengikuti_ujian_atau_tidak": mengikuti_ujian_atau_tidak, "nilai_ujian": nilai_ujian}
    ],  
    "Kelas C": [
            {"nama_siswa": nama_siswa, "kelas_siswa": kelas_siswa, "mengikuti_ujian_atau_tidak": mengikuti_ujian_atau_tidak, "nilai_ujian": nilai_ujian}
    ]
}   

for nama_kelas, data_siswa in pengelompokkan_kelas.items():
    print(f"=== KELAS {nama_kelas} ===")
    for siswa in data_siswa:
        print(f"Nama Siswa: {nama_siswa}")
        print(f"Kelas Siswa: {kelas_siswa}")   
        print(f"Mengikuti Ujian: {mengikuti_ujian_atau_tidak}")
        print(f"Nilai Ujian: {nilai_ujian}")
        print("------------------------")
    
    
    
