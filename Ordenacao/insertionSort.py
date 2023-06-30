def insertionSort(array):
    # percorre o array
    # O laço começa do índice 1, pois o índice 0 é o início
    # do subconjunto ordenado
    for i in range(1, len(array)):
        # chave do subarray desordenado        
        key = array[i]
            
        # Move os elementos de array[0.. i-1] que são maiores
        # do que a chave, para uma posicao à frente de sua
        # posição atual

        j = i-1
        while j>=0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        
        array[j+1] = key

# i = 1
# key = 48
# j = 0
# array[j] = 25
# [(25, 48), 37, 12, 57]

# i = 2
# key = 37
# j = 1
# array[j] = 48
# [(25, 48), 37, 12, 57]
# j = 0
# array[j] = 25
# [(25, 37, 48), 12, 57]

# i = 3
# key = 12
# j = 2
# array[j] = 48
# [(25, 37, 48), 12, 57]
# j = 1
# array [j] = 37
# [(25, 37, 12, 48), 57]
# j = 0
# array[j] = 25 
# [(25, 12, 37, 48), 57]
# [(12, 25, 37, 48), 57]

# i = 4
# key = 57
# j = 3
# array[j] = 48
# [(12, 25, 37, 48), 57]
# [(12, 25, 37, 48, 57)]
