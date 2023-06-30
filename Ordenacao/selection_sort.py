def selectionSort(array):
    for i in range(len(array)-1):
        min = i
        for j in range(i+1,len(array)):
            if(array[j] < array[min]):
                min = j
        array[min], array[i] = array[i], array[min]


# i = 0 j = (1,5)
# [40, 30, 20, 10, 0]