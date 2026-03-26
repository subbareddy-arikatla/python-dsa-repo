def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)
print(factorial(5))
# time complex o(n)
# space complex o(n) becuase the recursion using stack function internal layering

def factorial(n):
    fact=1
    for i in range(n):
        fact=fact * i
    return fact
# time complex o(n)
#  space complex o(1)

def sumarray(arr):
    res=0
    for i in arr:
        res=res+i
    return res
# time complex o(n)
# space complex o(1)

def RecSum(arr,n):
    if n<=0:
        return 0
    return RecSum(arr,n-1)+arr[n-1]
def arraysum(arr):
    return RecSum(arr,len(arr))

arr = [1, 2, 3, 4, 5]
print(arraysum(arr))

# time complex o(n)
#  space complex o(n)

def reverse(str):
    return str[::-1]
# time complexity o(n)
# space complexity o(n) every new character new string is create in memeory that why it is o(n) space complexity

def reverse(str):
    s=list(str)
    start=0
    end=len(str)-1
    while start>=end:
        s[start],s[end]=s[end],s[start]
        start=start+1
        end=end-1
    return "".join(s)
# time complex o(n)
#  space complex o(n)

def reversedemo(str):
    for ch in reversed(str):
        print(ch,end='')

def reversedemo2(str):
    if len(str) == 0:
        return str
    return reversedemo2(str[1:])+str[0]
str = 'Geeks for Geeks'
print(reversedemo2(str))

def binary(n):
    binary=0
    while n > 0:
        value=n%2
        binary=binary*10+value
        n=n//2
    return binary
print(binary(7))


def recbinary(n):
    if n == 0:
        return
    recbinary(n // 2)
    print(n % 2, end="")

recbinary(7)
