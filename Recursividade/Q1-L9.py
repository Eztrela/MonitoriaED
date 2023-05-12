def recursiveLength(string:str)->int:
    if string is '':
        return 0
    return 1 + recursiveLength(string[:-1])

print(recursiveLength('Jessye'))

