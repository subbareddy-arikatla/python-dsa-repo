def arraydemo(array):
    for i in range(len(array)):
        if array[i]>array[i+1]:
            return array[i+1]
    return array[1]

print(arraydemo([4,2,3]))