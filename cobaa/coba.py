from datetime import datetime

# Inisialisasi daftar to-do list
daftar_tugas = []

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n=== Menu To-Do List ===")
    print("1. Tambah Tugas")
    print("2. Lihat Daftar Tugas")
    print("3. Hapus Tugas")
    print("4. Tandai Tugas Selesai")
    print("5. Keluar")

# Fungsi untuk menambah tugas dengan jadwal
def tambah_tugas():
    tugas = input("Masukkan tugas baru: ")
    waktu = input("Masukkan jadwal (format HH:MM): ")
    try:
        # Memvalidasi format waktu
        jadwal = datetime.strptime(waktu, "%H:%M")
        daftar_tugas.append({"tugas": tugas, "selesai": False, "jadwal": jadwal})
        print("Tugas berhasil ditambahkan!")
    except ValueError:
        print("Format waktu tidak valid. Gunakan format HH:MM.")

# Fungsi untuk melihat daftar tugas yang diurutkan sesuai jadwal
def lihat_tugas():
    if not daftar_tugas:
        print("Tidak ada tugas dalam daftar.")
    else:
        # Mengurutkan daftar tugas berdasarkan jadwal
        daftar_tugas_terurut = sorted(daftar_tugas, key=lambda x: x["jadwal"])
        print("\nDaftar Tugas (diurutkan berdasarkan jadwal):")
        for i, item in enumerate(daftar_tugas_terurut, start=1):
            status = "Selesai" if item["selesai"] else "Belum selesai"
            waktu_str = item["jadwal"].strftime("%H:%M")
            print(f"{i}. {item['tugas']} - {waktu_str} - {status}")

# Fungsi untuk menghapus tugas
def hapus_tugas():
    lihat_tugas()
    try:
        nomor_tugas = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if 1 <= nomor_tugas <= len(daftar_tugas):
            tugas_dihapus = daftar_tugas.pop(nomor_tugas - 1)
            print(f"Tugas '{tugas_dihapus['tugas']}' berhasil dihapus.")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input tidak valid, masukkan nomor tugas.")

# Fungsi untuk menandai tugas selesai
def tandai_tugas_selesai():
    lihat_tugas()
    try:
        nomor_tugas = int(input("Masukkan nomor tugas yang selesai: "))
        if 1 <= nomor_tugas <= len(daftar_tugas):
            daftar_tugas[nomor_tugas - 1]["selesai"] = True
            print("Tugas berhasil ditandai sebagai selesai.")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input tidak valid, masukkan nomor tugas.")

# Program utama
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah_tugas()
    elif pilihan == "2":
        lihat_tugas()
    elif pilihan == "3":
        hapus_tugas()
    elif pilihan == "4":
        tandai_tugas_selesai()
    elif pilihan == "5":
        print("Keluar dari program. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid, silakan pilih lagi.")