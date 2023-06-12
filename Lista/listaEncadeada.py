#== == == == lista Exception
class ListaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        
#== == == == No é o elemento que será adiciona na estrutura de dados encadeada.
class Node:
    
    def __init__(self,carga:any) -> None:
        self.carga= carga # elemento armazenado
        self.prox=None # para quem ele aponta na lista

#== == == == A estrutura de dado lista, ou LIFO.
class Lista:
    def __init__(self):
        self.__inicio=None
        self.__quantidadeNode=0
    
    def estaVazia(self):
        return self.__inicio==None

    def inserir(self,valor:any,posicao:int=1):
        
        if posicao<1 : raise ListaException("Posição Inválida") # a posição não pode ser menor que 1 ou maior que a quantidade de nós
        NewNode=Node(valor) #criamos o nó
    
        if posicao==1 or self.estaVazia(): #checamos se a posição inserida pelo usuário foi "1" e a lista está vazia, no caso, a primeira
            NewNode.prox=self.__inicio
            self.__inicio=NewNode  
               
        else: #caso a posicao tenha sido qualquer outra
            #posicao-=1 #Decrementamos 1, para que quando entrar no laço, o cursor pare uma posição antes
            cursor=self.__inicio
            cursorPosicao=1
            
            while cursor!=None:

                if cursorPosicao + 1 ==posicao: #checamos se o cursor parou uma casa antes da posição
                    NewNode.prox=cursor.prox # o Novo nó aponta para o que o nó apontado pelo cursor aponta
                    cursor.prox=NewNode # agora, o apontado pelo cursor aponta ao novo nó.
                    break # encerramos o o laço
                
                elif cursor.prox==None: #inserir na condição de que a quantidade foi superior ao tamanho da Lista
                    cursor.prox=NewNode
                    break
                
                cursor=cursor.prox 
                cursorPosicao+=1
                    
        self.__quantidadeNode+=1
        
    def remover(self,posicao:int):
        if self.__quantidadeNode< posicao or posicao <1: raise ListaException("Posição Inválida")
        #elif self.estaVazia(): raise ListaException("Lista está vazia")
        
        NodeRemovido=None
        if posicao==1: #caso seja a primeira posição a ser removida
            NodeRemovido=self.__inicio
            self.__inicio=self.__inicio.prox
        
        else:
            cursor=self.__inicio
            cursorPosicao=1
            while cursor!=None:

                if cursorPosicao+1 ==posicao: #checamos se o cursor parou uma casa antes da posição
                    NodeRemovido=cursor.prox
                    cursor.prox = NodeRemovido.prox
                    break # encerramos o o laço
                cursor=cursor.prox 
                cursorPosicao+=1
        
        self.__quantidadeNode-=1
        return NodeRemovido.carga
        
    def __str__(self)-> str:
        
        todaLista=''
        cursor=self.__inicio
        
        if self.estaVazia():
            return 'Vazia'
        
        while cursor != None:
            todaLista+= f' ==|{str(cursor.carga)}|== '
            
            cursor= cursor.prox
    
        return todaLista