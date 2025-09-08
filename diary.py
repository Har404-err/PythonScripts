def tambah_catatan():
    """Menambahkan catatan baru ke dalam file."""
    catatan = input("Masukkan catatan Kamu: ")
    with open('catatan.txt', 'a') as file:
        file.write(catatan + '\n')
    print("Catatan berhasil ditambahkan!")

def lihat_catatan():
    try:
        with open('catatan.txt', 'r') as file:
            isi_catatan = file.read()
            if isi_catatan:
                print("\n=== Catatan Harian Kamu ===")
                print(isi_catatan)
                print("===========================")
            else:
                print("Belum ada catatan.")
    except FileNotFoundError:
        print("File catatan belum ada. Silakan tambahkan catatan.")

def hapus_catatan():
    try:
        with open('catatan.txt', 'w') as file:
            file.truncate(0) 
    except FileNotFoundError:
        print("File catatan belum ada.")


while True:
    print("\n--- Menu Pencatat Harian ---")
    print("1. Tambah catatan")
    print("2. Lihat catatan")
    print("3. Hapus catatan") 
    print("4. Keluar") 

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == '1':
        tambah_catatan()
    elif pilihan == '2':
        lihat_catatan()
    elif pilihan == '3':
        hapus_catatan()
    elif pilihan == '4':
        print("Terima kasih, sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
