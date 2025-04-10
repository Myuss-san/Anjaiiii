class Siswa:
    def _init_(self, nama, usia, nilai):
        self.nama = nama
        self.usia = usia
        self.nilai = nilai

class ManajemenSiswa:
    def _init_(self):
        self.data_siswa = []  # Pastikan atribut ini ada untuk menghindari error

    def tampilkan_menu(self):
        print("\n=== Menu Manajemen Siswa ===")
        print("1. Tambah Siswa")
        print("2. Lihat Siswa")
        print("3. Edit Siswa")
        print("4. Hapus Siswa")
        print("5. Cari Siswa")
        print("6. Keluar")

    def tambah_siswa(self):
        nama = input("Masukkan Nama: ")
        usia = input("Masukkan Usia: ")
        nilai = input("Masukkan Nilai Rata-rata: ")
        self.data_siswa.append(Siswa(nama, usia, nilai))
        print(f"[Siswa {nama} berhasil ditambahkan!]")

    def lihat_siswa(self):
        if not self.data_siswa:
            print("Belum ada data siswa.")
        else:
            print("\n=== Daftar Siswa ===")
            for i, siswa in enumerate(self.data_siswa):
                print(f"{i + 1}. Nama: {siswa.nama}, Usia: {siswa.usia}, Nilai: {siswa.nilai}")

    def edit_siswa(self):
        self.lihat_siswa()
        if self.data_siswa:
            try:
                indeks = int(input("Masukkan nomor siswa yang ingin diedit: ")) - 1
                if 0 <= indeks < len(self.data_siswa):
                    self.data_siswa[indeks].nama = input("Masukkan Nama baru: ")
                    self.data_siswa[indeks].usia = input("Masukkan Usia baru: ")
                    self.data_siswa[indeks].nilai = input("Masukkan Nilai baru: ")
                    print("Data siswa berhasil diperbarui!")
                else:
                    print("Nomor siswa tidak valid.")
            except ValueError:
                print("Harap masukkan angka yang valid.")

    def hapus_siswa(self):
        self.lihat_siswa()
        if self.data_siswa:
            try:
                indeks = int(input("Masukkan nomor siswa yang ingin dihapus: ")) - 1
                if 0 <= indeks < len(self.data_siswa):
                    nama = self.data_siswa[indeks].nama
                    del self.data_siswa[indeks]
                    print(f"[Siswa {nama} berhasil dihapus!]")
                else:
                    print("Nomor siswa tidak valid.")
            except ValueError:
                print("Harap masukkan angka yang valid.")

    def cari_siswa(self):
        nama_cari = input("Masukkan nama siswa yang dicari: ").lower()
        hasil = [siswa for siswa in self.data_siswa if siswa.nama.lower() == nama_cari]
        
        if hasil:
            print("\n=== Hasil Pencarian ===")
            for siswa in hasil:
                print(f"Nama: {siswa.nama}, Usia: {siswa.usia}, Nilai: {siswa.nilai}")
        else:
            print("Siswa tidak ditemukan.")

# Program Utama
manajemen = ManajemenSiswa()

while True:
    manajemen.tampilkan_menu()
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        manajemen.tambah_siswa()
    elif pilihan == "2":
        manajemen.lihat_siswa()
    elif pilihan == "3":
        manajemen.edit_siswa()
    elif pilihan == "4":
        manajemen.hapus_siswa()
    elif pilihan == "5":
        manajemen.cari_siswa()
    elif pilihan == "6":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")