def printstr(palavra: str) -> int:
    if palavra is '':
        return ''
    printstr(palavra[1:])
    print(palavra[0], end=' ')


printstr('Jessye')

# 'Jessye'
# J
# 'essye'
# J e
# 'ssye'
# J e s
# 'sye'
# J e s s
# 'ye'
# J e s s y
# 'e'
# J e s s y e
