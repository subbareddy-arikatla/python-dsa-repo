# str='subba reddy'
# strdemo=str[::1]
# print(str)
# print(strdemo)


def gcd(a,b):
    result=min(a,b)
    while result>0:
        if a%result==0 and b%result==0:
            break
        result-=1
    return result
# print(gcd(20,28))

def gcd(a,b):
    print(a)
    print(b)

    if(a==0):
        return b
    if(b==0):
        return a
    if(a==b):
        return a
    if a>b:
        return gcd(a-b,b)
    return gcd(a,b-a)
print(gcd(20,28))

def gcd(a,b):
    if(a==0):
        return b
    if(b==0):
        return a
    if(a==b):
        return a
    if(a>b):
        if(a%b==0):
            return b
        return gcd(a-b,a)
    if(a<b):
        if(b%a==0):
            return a
        return gcd(a,b-a)

def gcd(a,b):
    return a if b==0 else gcd(a,b-a)