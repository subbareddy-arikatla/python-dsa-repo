arraydemo=[]
a=[1,2,3,4,5,5]
b=["apple","banana","cherry"]
c=[1,2,"hello",3.14,True]
print(a)
print(b)
print(c)
a.append(8)
a.append(9)
print(a)
print(a[0])
print(a[-1])
print(a[1:4])
a.insert(0,6)
print(a)
a.extend([14,20,30])
print(a)
a.clear()
print(a)

a=[10,20,30,40,50]
a.remove(30)
print(a)
popped_val=a.pop(1)
print(popped_val)
print(a)
del a[0]
print("after del a[0]",a)

a=[1,2,3,44,5]
for item in a:
    print(item," ")
squares=[x**2 for x in range(1,6)]
print(squares)

def buyandsell(array):
    min_price=array[0]
    ans=0
    for i in range(1,len(array)):
        current_price=array[i]-min_price
        ans=max(current_price,ans)
        min_price=min(min_price,array[i])
    return ans

def isAlpha(s,i):
    x=ord(s[i])
    if  97<=x<=122 or 48<=x<=52:
        return True
    else:
        return False
    
def ispalindrome(s):
    s=s.lower()
    n=len(s)
    i,j=0,n-1
    while i<j:
        if not isAlpha(s,i):
            i+=1
            continue
        if not isAlpha(s,j):
            j-=1
            continue
        if s[i]==s[j]:
            i+=1
            j-=1
        else:
            return False
    return True
