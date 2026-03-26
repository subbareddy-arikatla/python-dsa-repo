# Find first non-repeating element in a given Array of integers
# Last Updated : 11 Jul, 2025
# Given an array of integers of size N, the task is to find the first non-repeating element in this array. 

# Examples:

# Input: {-1, 2, -1, 3, 0}
# Output: 2
# Explanation: The first number that does not repeat is : 2
# Input: {9, 4, 9, 6, 7, 4}
# Output: 6
def nonrepeat(array):
    n=len(array)
    for i in range(len(array)):
        j=0
        while(j<n):
            if(i!=j and array[i]==array[j]):
                break
            j=j+1
        if j==n:
            return array[i]
    return -1
print(nonrepeat([9, 4, 9, 6, 7, 4]))  
from collections import defaultdict

def nonrepeat(array):
    n=len(array)
    mp=defaultdict(lambda:0)
    for i in range(n):
        mp[array[i]]+=1
    for i in range(n):
        if mp[array[i]]==1:
            return array[i]
print(nonrepeat([9, 4, 9, 6, 7, 4]))



