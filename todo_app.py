
import json
import os
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

FILE_NAME = 'tasks.json'

def load_tasks():
    """Memuat tugas dari file JSON."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    """Menyimpan daftar tugas ke file JSON."""
    with open(FILE_NAME, 'w') as f:
        json.dump(tasks, f, indent=4)

def view_tasks(tasks):
    """Menampilkan semua tugas."""
    print("\n--- DAFTAR TUGAS ---")
    if not tasks:
        print("Tidak ada tugas. Saatnya bersantai!")
    else:
        for i, task in enumerate(tasks):
            status = "Selesai" if task['completed'] else "Belum Selesai"
            task_text = task['description']
            if task['completed']:
                print(Fore.GREEN + f"{i + 1}. [X] {task_text} - {status}")
            else:
                print(f"{i + 1}. [ ] {task_text} - {status}")
    print("--------------------")

def add_task(tasks):
    """Menambahkan tugas baru."""
    description = input("Masukkan deskripsi tugas baru: ")
    tasks.append({'description': description, 'completed': False})
    save_tasks(tasks)
    print(Fore.CYAN + f"Tugas '{description}' telah ditambahkan.")

def mark_task_complete(tasks):
    """Menandai tugas sebagai selesai."""
    view_tasks(tasks)
    try:
        num = int(input("Masukkan nomor tugas yang ingin ditandai selesai: "))
        if 0 < num <= len(tasks):
            tasks[num - 1]['completed'] = True
            save_tasks(tasks)
            print(Fore.GREEN + "Tugas berhasil ditandai selesai!")
        else:
            print(Fore.RED + "Nomor tugas tidak valid.")
    except ValueError:
        print(Fore.RED + "Input tidak valid. Harap masukkan angka.")

def delete_task(tasks):
    """Menghapus tugas."""
    view_tasks(tasks)
    try:
        num = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if 0 < num <= len(tasks):
            removed_task = tasks.pop(num - 1)
            save_tasks(tasks)
            print(Fore.YELLOW + f"Tugas '{removed_task['description']}' telah dihapus.")
        else:
            print(Fore.RED + "Nomor tugas tidak valid.")
    except ValueError:
        print(Fore.RED + "Input tidak valid. Harap masukkan angka.")

def main():
    """Fungsi utama untuk menjalankan aplikasi."""
    tasks = load_tasks()
    while True:
        print("\n--- MENU APLIKASI TO-DO ---")
        print("1. Lihat Semua Tugas")
        print("2. Tambah Tugas Baru")
        print("3. Tandai Tugas Selesai")
        print("4. Hapus Tugas")
        print("5. Keluar")
        
        choice = input("Pilih opsi (1-5): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Terima kasih telah menggunakan aplikasi. Sampai jumpa!")
            break
        else:
            print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
