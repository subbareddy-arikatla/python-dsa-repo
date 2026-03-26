def koko(array,k):
    min_diff=float('inf')
    index=-1
    for i in range(len(array)):
        if(array[i]>k):
            diff=array[i]-k
            if diff < min_diff:
                min_diff=diff
                index=i
    return index
print(koko([5,10,3],4))
print(koko([5, 10, 15, 20],7))
