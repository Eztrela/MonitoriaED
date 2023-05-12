def somaRecursiva(numero:int )->int:
    
    if numero==0: # a nossa condição de parada
        return 0
    
    return numero + somaRecursiva(numero - 1) 


print(somaRecursiva(3))

'''O que essa função faz

Ela vai receber um número, e vai somar começando do 0 até esse número.

somaRecursiva(3)

3 + 2 + 1 + 0

3 + somaRecursiva(3 - 1)  #numero + somaRecursiva(numero - 1) 

2 + somaRecursiva(2 - 1)

1 + somaRecursiva( 1 - 1 )

0

somaRecursiva(2 - 1) return 1 + 0 =  1

somaRecursiva(3 - 1) return 2 + 1 + 0 = 3

somaRecursiva(3) return 3 + 2 + 1 + 0 = 6
'''