def gcd(a,b):
    if a == 0:
        return b
    return (b % a,a)
def gcd(array):
    res=array[0]
    for num in array[1:]:
        res=gcd(num,res)
        if res==1:
            return 1
    return res
array = [2, 4, 6, 8, 16]

print(gcd(array))

def getGcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return b if a == 0 else a

# Function to find GCD of an array
def GcdOfArray(arr):
    gcd = arr[0]
    for num in arr:
        gcd = getGcd(gcd, num)
    return gcd

def __gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a==b:
        return a
    if(a>b):
        return __gcd(a-b,b)
    return __gcd(a,b-a)
def coprime(a,b):
    if(__gcd(a,b)==1):
        print('co-prime')
    else:
        print("not co-prime")
a = 5; b = 6
coprime(a, b) 

a = 8; b = 16
coprime(a, b)

    
    
