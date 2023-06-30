# Esta função atribui o primeiro elemento como pivô,
# coloca o pivô na sua posição correta no array
# ordenado, de forma que todos os elementos a esquerda
# do pivô são menores que ele, e os elementos à direita
# do pivô são maiores que ele

def quickSort(array):
    quickSortRun(array, 0, len(array)-1)


# Função que realiza todo o processo de posicionamento do pivô e
# particionamento das unidades do array. Retorna o índice correspondente
# ao posicionamento do pivô no array ordenado
#
# array[] --> Array a ser ordenado
# low  --> índice do primeiro elemento do array
# high  --> índice do último elemento do array
def partition(array, low, high):
    pivot = array[low]  # pivot

    # indice que sobe de forma crescente
    a = low + 1
    # indice que desce de forma decrescente
    b = high

    while (True):
        # Deslocando o indice para a direita
        while (a <= high and array[a] <= pivot):
            a += 1

        # Deslocando o indice do final para a esquerda
        while (array[b] > pivot):
            b -= 1

        # Se o indice "a" for menor que "b", realizamos a troca
        if (a < b):
            array[a], array[b] = array[b], array[a]
            a += 1
            b -= 1

        # se a cruzar com b, sai do laço
        if (a > b):
            break
    # Ja foi encontrado o lugar do pivo. Agora vamos troca-lo com o elemento
    # que se encontra no indice
    array[low] = array[b]
    array[b] = pivot

    return (b)

# função recursiva que aciona o particionamento e chamadas recursivas das
# subdivisões do array


def quickSortRun(array, low, high):
    if low < high:
        # pi é o índice de particionamento
        pi = partition(array, low, high)

        # Separadamente, os elementos antes e depois e antes da
        # partição são ordenados
        quickSortRun(array, low, pi-1)
        quickSortRun(array, pi+1, high)