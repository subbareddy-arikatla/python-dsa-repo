print("hello")

def twoSum(array,k):
    for i in range(len(array)):
        for j in range(i,len(array)):
            if array[i]+array[j]==k:
                return [i,j]
    return -1
print(twoSum([2,7,11,15],9))

# def twoSum(array,k):
#     n=len(array)
#     right=array[0]
#     left=array[n-1]
#     while right<left:

def twosum(array,k):
    mapdemo={}
    for i in range(len(array)):
        complement=k-array[i]
        if i in complement:
            return [mapdemo.get(complement),i]
        mapdemo.update(array[i],i)
    return []
