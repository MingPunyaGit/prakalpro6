#Input
def cari_bil_prima(n):

#Poses
    if n == 2 :
        return True
    elif n <= 0:
        return False
    else:
        for i in range(2, n):
            if n % i == 0 :
                return False
        return True
    
n = int(input('Masukan N: '))
if n > 2:
    for i in range(n - 1,1,-1):
        if cari_bil_prima(i):

#Output
            print('Maka prima Terdekat',n, 'adalah', i)
            break
else:
    'yo ga ada'