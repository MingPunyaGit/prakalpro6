#input
t = int(input('Masukan Tinggi : '))
l = int(input('Masukan Tinggi : '))

#proses
for i in range(1, t*l+1):
    if i % l==0 :
        print(i,end='\n')
    else:
        print(i,end=' ') 