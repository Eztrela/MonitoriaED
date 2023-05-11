def invertString(palavra: str) -> str:
    if palavra is '':
        return ''
    #modo 1
    # return palavra[-1] + invertString(palavra[:-1])
    
    #modo 2
    return invertString(palavra[1:]) + palavra[0]

print(invertString('Jessye'))
# modo 1:
# 'Jessye' retorna 'e' + invertString('Jessy')
# 'Jessy' retorna 'y' + invertString('Jess')
# 'Jess' retorna 's' + invertString('Jes')
# 'Jes' retorna 's' + invertString('Je')
# 'Je' retorna 'e' + invertString('J')
# 'J' retorna 'J' + invertString('')
# '' retorna '' + invertString('')

# modo 2:
# 'Jessye' retorna invertString('essye') + 'J'
# 'essye' retorna invertString('ssye')  + 'e'
# 'ssye' retorna invertString('sye') + 's'
# 'sye' retorna invertString('ye') + 's'
# 'ye' retorna invertString('e') + 'y'
# 'e' retorna invertString('') + 'e'
# ''  retorna invertString('') + ''
