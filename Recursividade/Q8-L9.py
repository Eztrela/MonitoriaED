def menores_rec(lista: list, key: int) -> int:
    if len(lista) == 0:
        return 0
    if lista[0] == key:
        return 1 + menores_rec(lista[1:], key)
    return menores_rec(lista[1:], key)


print(menores_rec([1, 1, 1, 2, 3, 1, 2, 1], 1))
