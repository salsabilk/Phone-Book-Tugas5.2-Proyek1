#phoneBook.py 
# Nama  : Salsabil Khoirunisa
# Kelas : 1B
# NIM   : 221524058

dict_phoneBook = {}

def displayMenu():
    print("\n")
    print("===== Menu Phone Book =====")
    print("1. Menambah Data Kontak")
    print("2. Menghapus Data Kontak")
    print("3. Mencari Data Kontak")
    print("4. Update Data Kontak")
    print("5. Menampilkan Data Kontak")
    print("6. Keluar")
    print()

def tambahKontak():
    print("Tambahkan Nama dan Nomor Telepon")
    nama = input("Nama: ")
    nomor = input("Nomor Telepon: ")
    dict_phoneBook[nama] = nomor

    with open("phoneBook.txt", "a") as file:
        notes = ""
        for i in dict_phoneBook:
            notes = i + " " + dict_phoneBook[i] + "\n"
        file.write(notes)

    print("Data Kontak Berhasil Ditambahkan")
    print()

def hapusKontact():
    print("Hapus Nama dan Nomor Telepon")
    nama = input("Nama: ")
    with open("phoneBook.txt", "r") as file :
        lines = file.readlines()
        
    with open("phoneBook.txt", "w") as file :
        deleted = False
        for line in lines :
            if line.startswith(nama + " "):
                deleted = True
            else :
                file.write(line)
        
        if deleted:
            del dict_phoneBook[nama]
            print("Data", nama, "Berhasil Dihapus")
        else:
            print(nama, "Data Kontak Tidak Ditemukan")
            
    print()

def editKontak():
    print("Update Nama dan Nomor Telepon")
    nama = input("Nama: ")
    if nama in dict_phoneBook:
        nomor = input("Nomor Telepon: ")
        dict_phoneBook[nama] = nomor

        with open("phoneBook.txt", "w") as file:
            for i in dict_phoneBook:
                file.write(i + " " + dict_phoneBook[i] + "\n")

            print("Data", nama, "Berhasil Diedit")
            print()
    else:
            print(nama, "Data Kontak Tidak Ditemukan")
            print()

def cariKontak():
    print("Cari Nama dan Nomor Telepon")
    nama = input("Nama: ")
    if nama in dict_phoneBook:
        print("Nomor Telepon adalah", dict_phoneBook[nama])
        print()
    else :
        print("Data", nama, "Tidak Ditemukan")
        print()
        
def tampilKontak():
    print("Menampilkan Daftar Nama dan Nomor Telepon")
    try:
        with open("phoneBook.txt", "r") as file:
            file_contents = file.read()
        if len(file_contents) == 0:
            print("Daftar Kontak Masih Kosong")
        else:
            print(file_contents)
    except FileNotFoundError:
        print("Daftar Kontak Masih Kosong")
        
    print()
    displayMenu()

# Baca isi file phoneBook.txt dan simpan ke dictionary dict_phoneBook
with open("phoneBook.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            nama, nomor = line.split()
            dict_phoneBook[nama] = nomor

# Main Program
displayMenu()
choose= 0
while choose != "6":
    choose = str(input("Masukkan Pilihan antara 1 - 6 : "))
    if choose == "1":
        tambahKontak()

    elif choose == "2":
        hapusKontact()

    elif choose == "3":
        cariKontak()

    elif choose == "4":
        editKontak()

    elif choose == "5":
        tampilKontak()

    elif choose != "6":
        displayMenu()
