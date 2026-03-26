def next_greater(arr):
    n=len(arr)
    ans=[-1]*n
    stack=[]
    for i in range(n-1,-1,-1):
        while stack and stack[-1]<=arr[i]:
            stack.pop()
        if stack:
            ans[i]=stack[-1]
        stack.append(arr[i])
    return ans
print(next_greater([2, 1, 2, 4, 3]))

def next
