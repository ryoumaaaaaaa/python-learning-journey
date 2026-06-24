nama = input("nama: ")
nilai = int(input("nilai: "))

if nilai >= 90:
    print(f"{nama} Kamu lulus")
if nilai >= 80:
    print(f"{nama} Kamu Lulus")
if nilai >=70:
        print(f"{nama} Kamu Remidi")
if nilai >= 60:
    print(f"{nama} Kamu tidak naik kelas")
if nilai <= 50:
        print(f"{nama} Kamu turun kelas")