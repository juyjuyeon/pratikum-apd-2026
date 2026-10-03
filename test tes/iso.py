# Data kelompok
identitas_kelompok = [
    "Nama: Wiliana Erianti",

nama_bindam = [
    "Bang Pernanda",
    "Bang Haqi"
]

nama_kelompok = [
    "Game Development"
]

while True:
    print("===== MENU UTAMA =====")
    print("1. Identitas Kelompok")
    print("2. Nama Bindam")
    print("3. Nama Kelompok")
    print("4. Program Berhenti")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        print("=== IDENTITAS KELOMPOK ===")
        
        print("=== NAMA BINDAM ===")
        print(nama_bindam[0])
        print(nama_bindam[1])

    elif pilihan == "3":
        print("=== NAMA KELOMPOK ===")
        print(nama_kelompok[0])

    elif pilihan == "4":
        print("Program berhenti.")
        break

    else:
        print("Pilihan tidak tersedia!")