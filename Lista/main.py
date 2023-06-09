import os
import time
#from listaEncadeada import *
from listaSequencial import *


""" L1=Lista()

L1.inserir(1,1000)
print(L1)
L1.inserir(2,1)
print(L1)
L1.inserir(3,3)
print(L1)
L1.inserir(4,2)
print(L1)
L1.inserir(5,1)
print(L1)
L1.inserir(6,2)
print(L1)
L1.inserir(7,545)
print(L1)

print(L1)
print('=-'*30)

print(L1.remover(1))
print(L1.remover(3))
print(L1.remover(2))
print(L1.remover(1))
print(L1) """
""" 
def MostrarDicionario(dicionario:dict, Chave:str = '0'):

    if dicionario.get(Chave,False)==False:
        print(f'{"-":^5}=> {dicionario["-"]:^5} ')
        return
    print(f'{Chave :^5}=> {dicionario[Chave]:^5} ')
    MostrarDicionario(dicionario, str(int(Chave) +1 ) )
        
opcoesLista={
    '0':'Obter informações da Lista',
    '1':'Inserir Novo Nó',
    '2':'Remover Nó',
    '3':'Verificar se está vazia',
    '4':'Modificar a carga de um Nó',
    '5':'Descobrir a carga de um Nó apartir da posição',
    '6':'Buscar a posição de Um Nó',
    '7':'Obter a quantidade de Nós',
    '8':'Obter informações do Node Leader',
    '9': 'Esvaziar a Lista',
    '-':'Finalizar o programa'
}
opcoesListaChaves= list(opcoesLista.keys())

L1=Lista()
#-- -- Preenchendo sozinho:
for i in range(1,17,3):
    L1.inserir(i, (i*3)//2)
while True:
    try:
        print()
        Posicao=0
        Chave=0
        Carga=''
        print('Escolha uma das seguintes opções: ')
        MostrarDicionario(opcoesLista)
        escolha=input('\n escolha: ')
#== == == == == ==
        if escolha=='-':#== == == Encerra o programa
            break
        escolha=int(escolha)  
        
        if escolha<6 and escolha not in [0,3,4]: #Escolhas que precisam de um informação
            Posicao=int(input('Digite qual a posição desejada para realizar tal operação: '))
        
        if escolha==1 or escolha==4 or escolha==6 : #Escolhas que precisam de uma chave
            Chave= int(input('Digite o valor da chave do Nó: '))
        
        if escolha==0:# Informações da Lista
            print(L1)
        
        elif escolha== 1: # Inserir um Novo nó  
            Carga= int(input('Digite a Carga do nó: '))
            L1.inserir(Chave,Carga,Posicao)
        
        elif escolha==2:#Remove Nó
            print(L1.remover(Posicao))      
        
        elif escolha==3: #Vê se a lista está vazia
            print(L1.estaVazia())
        
        elif escolha==4:#Modificar o Nó
            modificacao=int(input('Digite o valor que desja inserir no Node: '))
            print(L1.modificarNode(Chave,modificacao)) 
        
        elif escolha==5:#Descobre o nó pela posição
            print(L1.elemento(Posicao))
        
        elif escolha==6: #Recebe uma chave, busca a posição de um nó
            print(L1.busca(Chave))
        
        
        elif escolha==7:# Informações da Lista
            print(L1.tamanho())

        elif escolha==8:# Informa o que tem no nó leader
            print(L1.NodeLeader)
       
        elif escolha==9:# Esvaziar a Lista
            print(L1.esvazia())
    
        else:
            raise(Exception('CHOICE NOT FOUND'))
        input()
        os.system('clear')


    except ListaException as LE:
        os.system('clear')
        print(LE)
        time.sleep(2)
    except Exception as E:
        os.system('clear')
        print(E)
        time.sleep(2) 
"""

lista1=Lista()

lista1.inserir(1,1)
lista1.inserir(1,2)
lista1.inserir(1,3)
lista1.inserir(1,4)

lista2=Lista()
lista2.inserir(1,1)
lista2.inserir(1,3)
lista2.inserir(1,5)
lista2.inserir(1,6)
lista2.inserir(1,9)

'''
#Lista1 [1,2,3,4]
#Lista2 [1,3,5,6,9]
#Interseção [1,3]
'''
print(Lista.intersecao(lista1,lista2))