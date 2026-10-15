# # # formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]
# # # print(formula1)

# list_nama = ["jeno", "jaemin", "mark", "renjun", "chenle", "jisung"]
# print(list_nama)
# # for i in (list_nama[:3]):
# #     print(i)

# list_nama.append("haechan")
# print(list_nama)
#     # for i in (list_nama):
#     # print(i)

# list_nama.extend(["jaehyun", "jungwoo"])
# print(list_nama)

# list_nama.insert(0, "winwin")
# print(list_nama)

# list_nama[4] = "yuta"
# print(list_nama)

# del list_nama[5]
# print(list_nama)

# list_nama.remove("jeno")
# print(list_nama)

# ambil = list_nama.pop(2)
# print(list_nama)
# print(ambil)

# poin1 = [1, 2, 3, 4, 5, 6, 7]
# # print(poin)
# # poin[4:6] = [11, 12, 13]
# # # print(poin) ganti list
# # print(poin[0:6:1]) # mengambil list
# poin2 = [8, 9, 10] 
# poin = poin1 + poin2
# print(poin)

# line_up = [
# ["Ferrari", "Leclerc", 16],
# ["Mercedes", "Hamilton", 44],
# ["Red Bull", "Verstappen", 1],
# ["McLaren", "Norris", 4]
# ]
# print(line_up[2][1])

# for i in line_up:
#     for j in i: 
#         print(j)    

# nama = ["mingyu", "wonwoo", "seungkwan", "jeonghan", "hoshi"]
# print(nama)

# hapus = int(input("masukkan nama yang ingin dihapus: "))
# del nama[hapus]

# print(nama)

# hewan = ("kucing", "anjing", "burung", "ikan")
# # buah = ("apel", "jeruk", "mangga", "pisang")
# # kombinasi = hewan + buah
# # print(kombinasi)
# print(hewan) 

# list_hewan = list(hewan)
# list_hewan.append("kelinci")
# hewan = tuple(list_hewan)
# print(hewan)     

# chara = ("Yukari", "Yukino", "Odette", "Senku")
# (Persona, Oregairu, Genshin, DrStone) = chara
# print(Persona)
# print(Oregairu)

# bintang = ("*") 
# for i in range(5):
#     print(bintang * (i + 1))


# A = int(input("Masukkan nilai A : "))
# B = int(input("Masukkan nilai B : "))
# C = int(input("Masukkan nilai C : "))

# print("\n------------------------------")
# print("HASIL:")


# terbesar = max(A, B, C)
# print(f"Nilai Terbesar = {terbesar}")

# terkecil = min(A, B, C)
# print(f"Nilai Terkecil = {terkecil}")

# if A == B == C:
#     print("Keterangan     : A, B, dan C memiliki nilai yang sama")
# elif A == B:
#     print("Keterangan     : A dan B memiliki nilai yang sama")
# elif A == C:
#     print("Keterangan     : A dan C memiliki nilai yang sama")
# elif B == C:
#     print("Keterangan     : B dan C memiliki nilai yang sama")

# list_maba = ["Mingyu FT", "Wonwoo FT", "Seungkwan FKIP", "Jeonghan FH", "Hoshi FK", "Joshua FIB", "DK FISIP", "Jun FEB", "Minghao FEB"]
# mahasiswa = input("Masukkan nama mahasiswa yang ingin dicari: ")

# if mahasiswa in list_maba:
#     print(f"{mahasiswa} ditemukan dalam daftar mahasiswa.")
# else:
#     print(f"{mahasiswa} tidak ditemukan dalam daftar mahasiswa.")




# data_jurusan = {
#     "Informatika": [],
#     "Sipil": [],
#     "Elektro": []
# }

# print("=== INPUT DATA PENGELOMPOKAN MABA ===")


# for i in range(1, 5):
#     print(f"\n[ Data Maba Ke-{i} ]")
#     nama = input("Masukkan Nama Mahasiswa : ")
#     jurusan = input("Masukkan Jurusan (Informatika/Sipil/Elektro): ")
    

#     if jurusan in data_jurusan:
#         data_jurusan[jurusan].append(nama)
#         print(f" {nama} berhasil dimasukkan ke jurusan {jurusan}.")
#     else:
#         print(f" Jurusan '{jurusan}' tidak terdaftar! Data diabaikan.")

# print("\n" + "="*40)
# print("     HASIL PENGELOMPOKAN MAHASISWA     ")
# print("="*40)

# for jrs, daftar_nama in data_jurusan.items():
#     print(f"\n Jurusan {jrs} (Total: {len(daftar_nama)} orang):")
    
#     if len(daftar_nama) == 0:
#         print("   (Belum ada mahasiswa)")
#     else:
#         for nama in daftar_nama:
#             print(f"   - {nama}")


# list_maba = ["jeno NIM 88", "jaemin NIM 90","mark NIM 34"]
# print(list_maba)
# list_maba.append("jaehyun NIM 10")
# print(list_maba)


# kartu = {"merah", "merah", "biru", "hijau"}
# kartu.discard("kuning")
# kartu.remove("merah")
# print(kartu)

# aslab1 = {"fina", "shasha", "risma"}
# aslab2 = {"larry", "attar", "haekal"}
# gabung = aslab1.union(aslab2)
# print(gabung)

# Biodata = {
# "Nama" : "Siti Julpa",
# "NIM" : 25091060,
# "KRS" : ["Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Instagram" : "julpatarr"
# }

# print(f"Nama saya adalah {Biodata.get('Nama')}")
# print(Biodata.get("Nama"))
# print(Biodata.get("Alamat"))
# print(Biodata.get("Alamat", "Key untuk alamat tidak ada"))

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }
# for i in game:
#     print(i)
# for i in game.keys():
#     print(i)    

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }
# # for i in game.values():
# #     print(i)

# # for i, j in game.items():
# #     print(f"{i} adalah jenis game {j}")'

# game["resident evil"] = "horror"
#     print(game)

# aset = {
# "jenis" : "rumah",
# "harga" : 120000000,
# "alamat" : "Jl. Raya No. 1",
# "berpenghuni" : True,
# "luas" : "120m x 80m"
# }
# print(aset)
# cache = aset.pop("luas")
# print(aset)
# print(aset.get("luas"))
# print(cache)

# aset = {
# "jenis" : "rumah",
# "harga" : 120000000,
# "alamat" : "Jl. Raya No. 1",
# "berpenghuni" : True,
# "luas" : "120m x 80m"
# }

# aset_baru = aset.copy
# print(aset)
# print(aset_baru)

# key = "ayam geprek", "ayam goreng", "ayam bakar",
# value = 12000
# menu = dict.fromkeys(key, value)

# print(menu)

poli_umum = {"Andi", "Budi", "Citra", "Doni"}
poli_gigi = {"Citra", "Doni", "Eka", "Fani"}
gabungan_poli = poli_umum.union(poli_gigi)

print(gabungan_poli)


produk = { 
    "nama_produk1" : "tepung"
    "harga" : "10.000"
    "stok" : "7 karton"

    "nama_produk2" : ""

}