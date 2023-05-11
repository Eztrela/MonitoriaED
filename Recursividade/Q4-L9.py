def printInverse(palavra:str):
    if palavra is '':
        return ''
    print(palavra[-1],end='')
    printInverse(palavra[:-1])

printInverse('Jessye')