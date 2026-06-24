nama = input("nama: ")
pin = input("pin: ")

if nama == "rama" and pin == "rama123":
    print(f"SELAMA DATANG {nama}")
    print("1. cek saldo")
    print("2. tarik tunai")
    print("3. transfer")
    print("4. keluar")

    menu = input("Pilih menu: ")

if menu == "1":
    print("saldo anda Rp.500000")
elif menu == "2":
    tarik = int(input("Masukkan nominal:: "))
    if tarik > 500000:
        print("saldo anda tidak cukup")
    else:
        print(f"tarik tunai sebesar Rp.{tarik} berhasil")
        print(f"sisa saldo anda Rp.{500000 - tarik}")
elif menu == "3":
    tarik = int(input("Masukkan nominal:: "))
    if tarik > 500000:
        print("saldo anda tidak cukup")
    else:
        print(f"transfer sebesar Rp.{tarik} berhasil")
        print(f"sisa saldo anda Rp.{500000 - tarik}")
elif menu == "4":
    print("terima kasih telah menggunakan layanan kami")