nama = input("nama: ")
pin = input("pin: ")

if nama == "admin" and pin == "admin123":
    print(f"selamat datang {nama}")
    print("1. profil")
    print("2. pengaturan")
    print("3. keluar")
else:
    print("lau siape mpruy")

    percobaan = 3

    while percobaan > 0:
        pin = input("pin: ")

        if pin == "admin123":
            print("login berhasil")
            break

        percobaan -= 1
        print(f"pin salah, sisa percobaan: {percobaan}")

        if percobaan == 0:
            print("anda telah kehabisan percobaan, akun anda akan terkunci")