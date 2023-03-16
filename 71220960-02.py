#input 
def berurut(n):

#proses
    x = 1
    for i in range(1, n+1):
        x = x * i
    return x

n =int(input('Masukan N: '))

for i in range (n, 0, -1):
    for kj in range(i, 0, -1):
        if kj == i:
           
#Output          
            print(berurut(i),end=' ')
        print(kj,end=' ')
    print()