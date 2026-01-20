def arraydemo(array,target):
    if not target in array:
        array.append(target)
        return array
    for i in range(len(array)):
        if array[i]==target:
            return i
        elif array[i]>target:
            array.insert(i,target)
            return i
        elif(target>array[i]):
            array.append(target)
            return len(array)-1