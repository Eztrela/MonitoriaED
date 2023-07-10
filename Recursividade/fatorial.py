def calcularFatorial(n:int)->int:
    print('n vale: ',n)
    if n <= 1:
        return 1
    
    fatorial= n * calcularFatorial( n - 1)
    print(f'fatorial de {n} vale: ',fatorial)
    
    return fatorial


print('fatorial de 4: ',calcularFatorial(4))
print('fatorial de 5: ',calcularFatorial(5))
print('fatorial de 1: ',calcularFatorial(1))
print('fatorial de 0: ',calcularFatorial(0))


'''
    4!
    4*3!
    4*3*2!
    4*3*2*1!
    4*3*2*1
    5!
    n=5
    n2=4
    5*4*3*2*1
'''