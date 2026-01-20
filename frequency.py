# list1=[2,3,4,1,2,3,4,5,4,3,2]
# freq={}
# for i in list1:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# for i in freq:
#     print(f"{i} is present {freq[i]} times")
# leetcode 217  contains Duplicate

# given an interger array nums,return true if an value appear at twice at least twice in the array and return false if every elememt is distinct
# nums=[1,3,2,5,4] false
# array=[1,2,3,4,5,5]true

def duplicate(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]==array[j]:
                return True
    return False
         
array=[1,2,3,4,5,5]  
print(duplicate(array))

def duplicate(array):
    array=sorted(array)
    # print(array)
    for i in range(0,len(array)-1):
        if array[i]==array[i+1]:
            return True
    return False

nums=[1,3,2,5,4,4]
print(duplicate(nums))

def duplicate(array):
    freq={}
    for i in array:
        if i in freq:
            return True
        else:
            freq[i]=1
    return False
nums=[1,3,2,5,4,4]
print(duplicate(nums))
