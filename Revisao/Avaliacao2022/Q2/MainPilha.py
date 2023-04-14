import os
import time
from PilhaEncadeada import *
#from PilhaSequencial import *

def concatenaPilhas( pilha1:Pilha, pilha2:Pilha )->Pilha:
    '''Método que recebe duas pilhas e as concatena de maneira em que nenhuma delas perca qualquer dado. '''
    pilhaAuxiliar1=Pilha() #pilha que irá receber todos os elementos da primeira pilha, sem desempilhar.  
    pilhaAuxiliar2=Pilha() #pilha que irá receber todos os elementos da segunda pilha, sem desempilhar esta.
    pilhaAuxiliar3=Pilha() #pilha que irá empilhar todos os elementos das pilhas auxiliar.
    
    for cursor in range(len(pilha1)):
        '''Este laço é uma falsa representação de percorrimento de uma estrutura de dados. o cursor será responsável por indicar as posições das buscas pelos ELEMENTOS da pilha. '''
        
        NodeAtual= pilha1.elemento(cursor+1) #recebe o elemento cujo  valor está sendo apressentado no  cursor.
        pilhaAuxiliar1.empilha(NodeAtual)
        
    for cursor in range(len(pilha2)):
        NodeAtual= pilha2.elemento(cursor+1) #recebe o elemento cujo  valor está sendo apressentado no  cursor.
        pilhaAuxiliar2.empilha(NodeAtual)
    
    
        '''Nesta parte, a pilha que foi destinada receber a concatenação,"cls", irá empilhar os elementos das pilhas auxiliares.'''
    while not(pilhaAuxiliar2.estaVazia()):
        pilhaAuxiliar3.empilha(pilhaAuxiliar2.desempilha()) #Podemos utilizar o desempilha sem medo, pois foi gerado uma cópia dos dados, graças aos laços anteriores. 
    
    while not(pilhaAuxiliar1.estaVazia()):
        pilhaAuxiliar3.empilha(pilhaAuxiliar1.desempilha()) #Podemos utilizar o desempilha sem medo, pois foi gerado uma cópia dos dados, graças aos laços anteriores.
        
    return pilhaAuxiliar3


def checarPalindromo(frase:str):
    pilhaAuxiliar=Pilha()
    pass

def decToBin( numero:int):
    '''Método que transforma um número decimal em binário '''
    pass

def mostrarDicionario(dicionario:dict)->str:
    dicionarioChaves=list(dicionario.keys())
    s=''
    for i in dicionarioChaves:
        s+= f'{i :^5}=> {dicionario[i]:^5} \n'
    return s


def MostrarDicionario(dicionario:dict, chaveBusca:str = '0'):
    '''
    Este método recebe um dicionário e uma lista contendo suas chavesBusca, em seguida mostra-o na tela de maneira formatada 
    '''
    if dicionario.get(chaveBusca,False)==False:
        print(f'{"-":^5}=> {dicionario["-"]:^5} ')
        return
    print(f'{chaveBusca :^5}=> {dicionario[chaveBusca]:^5} ')
    MostrarDicionario(dicionario, str(int(chaveBusca) +1 ) )
        
opcoesPilha={
    'I':'Informações da Pilha',#0
    'E':'Empilhar Novo Nó',#1
    'D':'Desempilhar Nó',#2
    'V':'Verificar se está vazia',#3
    'M':'Modificar a carga de um Nó',#4
    'P':'Procurar Nó apartir da posição',#5
    'B':'Buscar a posição de Um Nó',#6
    'T':'Tamanho Pilha',#7
    'L':'Limpar a Pilha',#8
    'C': 'Inverter Ordem da Pilha',#9
    'N':'Escolher Outra Pilha',#10
    'Z':'Concatenar duas pilhas',
    'U':'Conversão dec/bin',
    'O':'Checar Frase Palindroma',
    'J':'Clonar a pilha',
    'F':'Finalizar o programa'#-
    
}

pilhasLista=[None for i in range(10)]# O programa será multipilhas.
posicaoPilhaAtual=0 #Posicao em que o usuario se encontra atualmente.
pilhaClonada=Pilha()
#-- -- Preenchendo a Lista de Pilhas:

for i in range(10):
    pilhasLista[i]=Pilha()
    #-- -- Preenchendo automaticamente a Pilha
    for j in range(i,i*6,3):
        pilhasLista[i].empilha((j*3)//2)

while True:
    try:
        pilhaAtual=pilhasLista[posicaoPilhaAtual]
        chaveBusca=0
        posicaoNode=0
        
        print("=="*30)
        print(f"Pilha selecionada: {posicaoPilhaAtual+1} de {len(pilhasLista) } Pilhas. ")
        print(pilhaAtual)
        print('Pilha clonada: ',pilhaClonada)
        print("=="*30)
 
        
        print('Escolha uma das seguintes opções: ')
        print(mostrarDicionario(opcoesPilha))
        escolha=str.upper(input('\n escolha: '))
        

        if escolha=='F':#== == == Encerra o programa
            break
          
        
        if escolha  in ['M','P']: #Escolhas que precisam de um informação
            posicaoNode=int(input('Digite qual a posição desejada para realizar tal operação: '))
        
        if escolha=='B' : #Escolhas que precisam de uma chaveBusca
            chaveBusca= int(input('Digite o valor que procuras do Nó: '))
        
        if escolha=='I':# Informações da Pilha
            print(pilhaAtual)
        
        elif escolha== 'E': # empilha um Novo nó
            Carga=int(input('Digite um valor inteiro a ser inserido: '))
            pilhaAtual.empilha(Carga)
        
        elif escolha=='D':#Desempilhar Nó
            print(pilhaAtual.desempilha())      
        
        elif escolha=='V': #Vê se a Pilha está vazia
            print(pilhaAtual.estaVazia())
        
        elif escolha=='M':#Modificar o Nó
            modificacao=int(input('Digite o valor que desja modificar no Node: '))
            pilhaAtual.modificar(posicaoNode,modificacao)
        
        elif escolha=='P':#Descobre o nó pela posição
            print(pilhaAtual.elemento(posicaoNode))
        
        elif escolha=='B': #Recebe uma chaveBusca, busca a posição de um nó
            print(pilhaAtual.busca(chaveBusca))
        
        
        elif escolha=='T':# Tamanho da Pilha
            print(len(pilhaAtual))

       
        elif escolha=='L': #Limpar a Pilha
            print(pilhaAtual.esvazia())
            
        elif escolha=='C': #Inverter Ordem da Pilha
            pilhaAtual.inverter()
            
        
        elif escolha=='N': #Escolher Outra Pilha
            posicaoPilhaAtual=int(input(f"[1 - {len(pilhasLista)}] Digite qual posição deseja acessar: "))-1
            if posicaoPilhaAtual> len(pilhasLista) or posicaoPilhaAtual<0: 
                posicaoPilhaAtual=0
                raise Exception("Posição de pilha inserida é inválida! ")
        
        elif escolha=='U':#Conversão dec/bin
            numeroDecimal= int(input('Digite o valor que desejas ser convertido para binário: '))
            
            print(decToBin(numeroDecimal))
            
        elif escolha=='Z': #Concatenar duas pilhas diferentes
            posicaoPilha1=int(input(f"[1 - {len(pilhasLista)}] 1ª Pilha\n Digite a pilha que deseja concatenar: "))-1
            posicaoPilha2=int(input(f"[1 - {len(pilhasLista)}] 2ª Pilha\n Digite a segunda pilha que deseja concatenar: "))-1
            destino=int(input(f"[1 - {len(pilhasLista)}] Pilha Destino\n Digite agora, qual a posição que será sobescrita: "))-1
             
            if (posicaoPilha1> len(pilhasLista) or posicaoPilha1<0) and \
                (posicaoPilha2> len(pilhasLista) or posicaoPilha2<0) and \
                (destino> len(pilhasLista) or destino<0): raise Exception('Posição inserida inválida')
            
            pilhasLista[destino]=concatenaPilhas(pilhasLista[posicaoPilha1],pilhasLista[posicaoPilha2])
        
        elif escolha=='O':
            frase=input('Digite a frase que desejas checar se é palindroma: \n')

            print(checarPalindromo(frase)) 
        
        elif escolha=='J':
            pilhaClonada= pilhaAtual.clone()
            print('Este é o novo clone da pilha: \n ',pilhaClonada)
        else:
            raise(Exception('CHOICE NOT FOUND'))
        
        if escolha not in ['E','M','N','F']:
            input()
        #os.system('clear')


    except PilhaException as PE:
        os.system('clear')
        print(PE)
        
        time.sleep(2)
    
    except TypeError as TE:
        os.system('clear')
        print(TE)
        
        time.sleep(2)
    
    except Exception as E:
        os.system('clear')
        print(E)
        
        time.sleep(2)
        