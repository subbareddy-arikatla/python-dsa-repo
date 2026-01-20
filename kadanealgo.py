def maxsubarray(array):
    n=len(array)
    ans=array[0]
    curr_sum=0
    for i in array:
        curr_sum+=i
        if curr_sum>ans:
            ans=curr_sum  
        if curr_sum<0:
            curr_sum=0
    return ans

# contains duplicate -[leetcode 217]
# longest common prefix-[leetcode 14]
# valid anagram {leetcode 560}
# rotate image - leetcode 48
# maximum subarray-[leetcode 53]