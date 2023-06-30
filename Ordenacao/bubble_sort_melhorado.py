def bolha(array):
    flag = False
    for i in range(len(array)-1,0,-1):
        for j in range(0,i):
            if (array[j] > array[j+1] ):
                array[j],array[j+1] = array[j+1],array[j]
                flag = True
        if(not flag):
            return
        
[60, 35, 48, 12, 31, 20]
A = [60]
B = [35, 48, 12, 31, 20]

A = [35,60]
B = [48,12,31,20]

A = [35,48,60]
B = [12,31,20]

A = [12,35,48,60]
B = [31,20]

A = [12,31,35,48,60]
B = [20]

A = [12,20,31,35,48,60]
B = []