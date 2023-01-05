file = open("Tubes_2021_1301213029_HamdanAzani.txt","r")

x = len(file.readlines())

file.seek(0)

#Membuat dictionary
klasemen = {}

for i in range(x):
    a = file.readline()
    b = a.split()
    klasemen[b[0]] = [0, 0, 0, 0, 0, 0, 0, 0]

file.seek(0)

#total main
for i in range(x):
    a = file.readline()
    b = a.split()
    klasemen[b[0]][0] = 2

file.seek(0)

#total menang
for i in range(x):
    a = file.readline()
    b = a.split()
    if int(b[1]) > int(b[2]):
        klasemen[b[0]][1] = klasemen[b[0]][1] + 1
    elif int(b[1]) < int(b[2]):
        klasemen[b[3]][1] = klasemen[b[3]][1] + 1

file.seek(0)

#total draw
for i in range(x):
    a = file.readline()
    b = a.split()
    if int(b[1]) == int(b[2]):
        klasemen[b[0]][2] = klasemen[b[0]][2] + 1
        klasemen[b[3]][2] = klasemen[b[3]][2] + 1

file.seek(0)

#total kalah
for i in range(x):
    a = file.readline()
    b = a.split()
    if int(b[1]) > int(b[2]):
        klasemen[b[3]][3] = klasemen[b[3]][3] + 1
    elif int(b[1]) < int(b[2]):
        klasemen[b[0]][3] = klasemen[b[0]][3] + 1

file.seek(0)

# total gol memasukkan
for i in range(x):
    a = file.readline()
    b = a.split()
    klasemen[b[0]][4] = klasemen[b[0]][4] + int(b[1])
    klasemen[b[3]][4] = klasemen[b[3]][4] + int(b[2])

file.seek(0)

#total gol kemasukkan
for i in range(x):
    a = file.readline()
    b = a.split()
    klasemen[b[0]][5] = klasemen[b[0]][5] + int(b[2])
    klasemen[b[3]][5] = klasemen[b[3]][5] + int(b[1])

file.seek(0)

#selisih gol
for i in range(x):
    a = file.readline()
    b = a.split()
    klasemen[b[0]][6] = klasemen[b[0]][4] - klasemen[b[0]][5]

file.seek(0)

#total point
for i in range(x):
    a = file.readline()
    b = a.split()
    klasemen[b[0]][7] = klasemen[b[0]][1]*3 + klasemen[b[0]][2]

file.close()

#fungsi menampilkan tabel klasemen
def tabel_klasemen():
    print("Nama Klub\tTotal Main\tTotal Menang\tTotal Draw\tTotal Kalah\tTotal Gol Memasukkan\tTotal Gol Kemasukkan\tSelisih Gol\tTotal Point")
    for key in klasemen:
        if len(key) >=8:
            print(key, end="\t    ")
        else:
            print(key, end="\t\t    ")
        sementara = 0
        while sementara < 8:
            if sementara == 0: 
                print(klasemen[key][sementara], end="\t\t     ")
            elif sementara == 1: 
                print(klasemen[key][sementara], end="\t\t     ")
            elif sementara == 2: 
                print(klasemen[key][sementara], end="\t\t     ")
            elif sementara == 3: 
                print(klasemen[key][sementara], end="\t\t\t ")
            elif sementara == 4: 
                print(klasemen[key][sementara], end="\t\t\t ")
            elif sementara == 5: 
                if int(klasemen[key][sementara+1]) >= 0:
                    print(klasemen[key][sementara], end="\t\t      ")
                elif int(klasemen[key][sementara+1]) < 0:
                    print(klasemen[key][sementara], end="\t\t     ")
            elif sementara == 6: 
                print(klasemen[key][sementara], end="\t\t     ")
            elif sementara == 7:
                print(klasemen[key][sementara], end="\n")
            sementara += 1

def main():
    print("Hamdan Azani_1301213029".center(80,"-"))
    print("1. Tampilkan Dictionary")
    print("2. Tampilkan Klasemen")
    print("3. Stop")
    print("".center(80,"-"))
    input1 = input("Ketikkan Angka 1, 2 atau 3: ")
    if input1 == "1":
        print("".center(170,"="))
        print(klasemen)
        print("".center(170,"="))
        main()
    elif input1 == "2":
        print("".center(170,"="))
        tabel_klasemen()
        print("".center(170,"="))
        main()
    elif input1 == "3":
        print("Terima Kasih!")
    else:
        print("".center(170,"="))
        print("Masukkan Angka 1, 2 atau 3")
        print("".center(170,"="))
        main()

if __name__ == "__main__":
    main()
