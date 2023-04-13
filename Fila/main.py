from filasequencialcircular import *

F1=FilaSequencial()
#-- -- Preenchendo sozinho:
for i in range(1,21,3):
    F1.enfileira((i*3)//2)

print(F1)
print("=_"*30)

for i in range(2):
    print(f'{i+1}ª Desinfileiração...')
    print(F1.desenfileira())

print("=_"*30)
print(F1)
print()

print('Buscando um elemento')
print()
k=19
print('Valor Existente na fila....')
print(f'chave: {k}\n posicao: {F1.busca(k)}')

print()
print('Valor Inexistente....')
k='isso não é uma string'
print(f'chave: {k}\n posicao: {F1.busca(k)}')

print("=_"*30)
print(F1)
print()

print('Mostrando o valor em uma posição...')
print()
p=3
print('Valor Existente na fila....')
print(f"posicão {p} \n {F1.elemento(3)}")

try:
    print('Valor Inexistente....')
    p=0
    print(f"posicão {p} \n {F1.elemento(0)}")
except FilaException as FE:
    print(FE)
    
print("=_"*30)