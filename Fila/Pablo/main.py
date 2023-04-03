from filasequencialcircular import *

F1=FilaSequencial()
#-- -- Preenchendo sozinho:
for i in range(1,17,3):
    F1.enfileira((i*3)//2)

print(F1)

for i in range(2):
    print(f'{i+1}ª Desinfileiração...')
    print(F1.desenfileira())


