#from PilhaEncadeada import Pilha, PilhaException
from PilhaSequencial import Pilha, PilhaException
from Aluno import Aluno

p = Pilha()


for i in range (1,11):
    #p.empilha(i*10)
    p.empilha(Aluno(i*10,f"ipsl lorum{i}"))

try:
    key = p.elemento(10)
    print(type(key))
    print(key)
    key = Aluno(90,f"ipsl lorum9")
    print(p.busca(key))
    input("...")

    print(p)
    print(len(p))
    try:
        while(True):
            print('desempilha: ', p.desempilha())
    except PilhaException as pe:
        print(pe)
    print(p)
    print(len(p))
    print(p.elemento(1))
except PilhaException as pe:
    print(pe)