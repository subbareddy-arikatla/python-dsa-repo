def findMaxAverage(array,k):
    curr_sum=0
    n=len(array)
    for i in range(k):
        curr_sum+=array
    ans=curr_sum/k
    for i in range(k,n):
        curr_sum+=array[i]
        curr_sum-=array[i-k]
        ans=max(ans,curr_sum/k)
    return ans