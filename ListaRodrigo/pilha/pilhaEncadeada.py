from  pilhaException import PilhaException


class Node:
    
    def __init__(self,carga:any) -> None:
        self.carga= carga # elemento armazenado
        self.prox=None # para quem ele aponta na lista


class pilha:
    
    def __init__(self):
        
        self.topo=None
        self.__tamanho=0
    
        
    def estaVazia(self)->bool:
        return self.__inicio==None   
        
    def inserir(self, carga:any):
        
        novoNo=Node(carga)
        
        novoNo.prox=self.topo
        
        self.__tamanho+=1
        
        
    def remover(self):
        '''
        1 3º topo
        2 2º
        3 1º
        '''
        if self.estaVazia(): raise PilhaException('Esta vazia')
        
        cargaRemovida= self.topo.carga
        
        self.topo= self.topo.prox
        
        self.__tamanho-=1
        
        return cargaRemovida
    
    def esvaziar(self):
        
        while not (self.estaVazia()):
            
            self.topo= self.topo.prox
        
            self.__tamanho-=1
    
    
    
    def busca(self,chave:int):
        '''Retorna uma posição a partir de uma chave'''
        pass
    
    def elemento(self,index:int)->any:
        '''Retorna um elemento a partir de uma posição'''
        
        '''
                    elemento na posição 1
        1 3º topo   
        2 2º   
        3 1º   cursor   1  
        '''
        
        if self.estaVazia(): raise PilhaException('Esta vazia')
        
        if index> self.__tamanho :  raise PilhaException('ìndice inválido.')
        
        cursor= self.topo
        cursorPosicao= self.__tamanho
        
        while cursor== None:
            
            if cursorPosicao== index:
                return cursor.carga
            
            cursor= cursor.prox
            cursorPosicao -= 1
            
    
    
    def concatenar(self, outraPilha:'pilha'):
        pilhaAuxiliar=pilha()
        
        while not(outraPilha.estaVazia()):
            pilhaAuxiliar.inserir(outraPilha.remover())
        
        while not( pilhaAuxiliar.estaVazia()):
            self.inserir(pilhaAuxiliar.remover()) 
        