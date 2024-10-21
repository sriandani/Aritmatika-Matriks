# menginput jumlah baris dan kolom matriks A nilai yang dimasukkan akan disimpan di setiap variabel
baris_A=int(input("masukkan ukuran baris matriks A = "))
kolom_A=int(input("masukkan ukuran kolom matriks A = "))
# menginput jumlah baris dan kolom matriks B nilai yang dimasukkan akan disimpan di setiap variabel
baris_B=int(input("Masukkan ukuran baris matriks B = "))
kolom_B=int(input("Masukkan ukuran kolom matriks B = "))
#memeriksa apakah jumlah kolom matriks A sama dengan matriks B
# jika tidak perkalian matriks tidak dapat dilakukan
if (kolom_A !=baris_B):

    print ("Matriks Tidak Dapat Dikalikan!")
#jika iya input sesuai perintah berikut
#Matriks A diinisialisasi sebagai list kosong. Kemudian, menggunakan dua loop bersarang,
#masukkan elemen matriks A
else:
    print("masukkan element Matriks A : ")
    A=[]
    for i in range (baris_A):
        baris=[]
        for j in range (kolom_A):
            value = int(input("Masukkan elemen Matriks A: "))
            baris.append(value)
        A.append(baris)
#masukkan elemen2 matriks b
    print ("Masukkan elemen Matriks B : ")
    B=[]
    for i in range (baris_B):
        baris=[]
        for j in range (kolom_B):
            value = int(input("Masukkan elemen Matriks B: "))
            baris.append(value)
        B.append(baris)
#Mencetak matriks A dan B untuk menunjukkan isi dari kedua matriks yang telah dimasukkan
print ("Matriks A : ", A)
print ("Matriks B : ", B)

# Perkalian Matriks A dengan Matriks B
# inisialisasi hasil perkalianß

hasil_kali = [[0 for _ in range(kolom_B)]for _ in range(baris_A)]
#melakukan perkalian matriks dengan 3 loop bersarang
for i in range(baris_A):
    for j in range(kolom_B):
        for k in range(kolom_A):
            hasil_kali[i][j]+=A[i][k]*B[k][j]
#mencetak hasil perkalian matriks
print ("Hasil Perkalian Matriks A dengan Matriks B adalah, ", hasil_kali)
