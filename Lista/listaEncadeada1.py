
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

    
    def inserir(self, valor:any,posicaoDesejada:int=1):
        if posicaoDesejada < 1: raise ListaException("Posição inválida")
        
        NewNode=Node(valor) 
        
        if posicaoDesejada==1:
            NewNode.prox= self.__inicio
            self.__inicio= NewNode
        
        else:
            cursor=self.__inicio
            posicaoCursor=1
            
            while cursor!=None:
                if posicaoCursor + 1 == posicaoDesejada:
                    NewNode.prox= cursor.prox
                    cursor.prox= NewNode
                    break
                
                elif cursor.prox==None: # o cursor chegou no final da lista
                    cursor.prox=NewNode
                    break
                    #NewNode.ant=cursor
                
                cursor=cursor.prox
                posicaoCursor+=1
                
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