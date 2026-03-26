# def arraydemo(array,target):
#     for i in range(len(array)):
#         if array[i]==target:
#             return i
#         elif array[i]>target:
#             array.insert(i,target)
#             return i
#         elif(target>array[i]):
#             array.append(target)
#             return len(array)-1
        

def searchInsert(arr,k):
    for i in range(len(arr)):
        if arr[i]>=k:
            return i
    return len(arr)
arr = [1, 3, 5, 6]  
k = 5  
print(searchInsert(arr, k))