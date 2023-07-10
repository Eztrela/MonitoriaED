def calcular_mdc(a, b):
    if b == 0:
        return a
    else:
        return calcular_mdc(b, a % b)
    

print('CalculandoMDC de 5,4 ',calcular_mdc(5,4))
print('CalculandoMDC de 30,60 ',calcular_mdc(30,60))
print('CalculandoMDC de 9,10 ',calcular_mdc(10,9))