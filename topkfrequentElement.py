# Given an array arr[] and a positive integer k, Find the top k elements which have the highest frequency in the array.

# Note: If more than one element has same frequency then priorities the larger element over the smaller one.

# Examples: 

# Input: arr[] = [3, 1, 4, 4, 5, 2, 6, 1], k = 2
# Output: [4, 1]
# Explanation: Frequency of 4 is 2 and frequency of 1 is 2, these two have the maximum frequency.

# Input: arr[] = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], k = 4
# Output: [5, 11, 7, 10]
# Explanation: Frequency of 5 is 3, frequency of 11 is 2, frequency of 7 is 2, and frequency of rest is 1  but 10 is largest .
from collections import Counter
#Driver Code Ends

def topKFreq(arr, k):
    n = len(arr)

    mp = Counter(arr)

    # Store the elements of 'mp' in the list 'freq'
    freq = list(mp.items())

    # Sort the list 'freq' on the basis of the
    # 'compare' function
    freq.sort(key=lambda x: (x[1], x[0]), reverse=True)
    
    res = []
    
    # Extract and store the top k frequent elements
    for i in range(k):
        res.append(freq[i][0])
        
    return res

#Driver Code Startsarr = [3, 1, 4, 4, 5, 2, 6, 1]
k = 2
arr = [3, 1, 4, 4, 5, 2, 6, 1]
res = topKFreq(arr, k)
    
for val in res:
    print(val, end=" ")


# Time Complexity: O(n +d*log d), where n is the size of the array and d is the count of distinct elements in the array.
# Auxiliary Space: O(d)

# [Expected Approach 1] Using Hash map and Min Heap
# The idea is to use a hashmap to store each element and its frequency. Then, use a priority queue (min-heap) to store pairs of frequency and element, so that the element with the smallest frequency is on top. Iterate through the hashmap and push each pair into the heap, and if the heap size exceeds k, remove the top element. After processing all elements, the heap will contain the k most frequent elements. Finally, extract these elements from the heap and store them in the result array.

import heapq
def topkfreq(array,k):
    mp={}
    for val in arr:
        mp[val]=mp.get(val,0)+1
    pq=[]
    for key,freq in mp.items():
        heapq.heappush(pq,[freq,key])
        if len(pq)>k:
                heapq.heappop(pq)
        res=[]
        temp=[0]*len(pq)
        index=len(pq)-1
        while pq:
            temp[index]=heapq.heappop(pq)[1]
            index-=1
        for val in temp:
            res.append(val)
arr = [3, 1, 4, 4, 5, 2, 6, 1]
k = 2
res = topKFreq(arr, k)
for val in res:
    print(val, end=" ")