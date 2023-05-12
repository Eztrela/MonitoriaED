def decToBin(num: int) -> int:
    if num // 2 == 0:
        print(num % 2, end='')
        return
    decToBin(num // 2)
    print(num % 2, end='')


decToBin(1)

'''

'''