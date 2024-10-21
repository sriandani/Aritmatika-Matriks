baris_A=int(input("Masukkan ukuran baris matriks A= "))
kolom_A=int(input("Masukkan ukuran kolom matriks A= "))

baris_B=int(input("Masukkan ukuran baris matriks B= "))
kolom_B=int(input("Masukkan ukuran kolom matriks B= "))

if (kolom_A!=baris_B):
    print ("Matriks Tidak Dapat Dikalikan!")
else:
    print ("Masukkan element matriks A : ")
    A=[]
    for i in range (baris_A):
        baris=[]
        for j in range (kolom_A):
            value=int(input("Masukkan element: "))
            baris.append(value)
        A.append(baris)
    print("Masukkan element matriks B")
    B=[]
    for i in range (baris_B):
        baris=[]
        for j in range (kolom_A):
            value=int(input("Masukkan element: "))
            baris.append(value)
        B.append(baris)
        
print ("Matriks A : ", A)
print ("Matriks B: ", B)
