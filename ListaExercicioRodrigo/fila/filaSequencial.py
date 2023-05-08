from  filaException import FilaException


class Fila:
    
    def __init__(self, quantidade=10):
        self.__dados=[None for i in range(quantidade)]
        self.__inicio=0
        self.__final=-1
        self.__tamanhoFila=0
        self.__tamanhoLimite=quantidade
    
    
    def estaVazia(self)->bool:
        return self.__tamanhoFila==0
    
    def inserir(self, carga:any):
        ''''
              F   I                   inserir 4
        fila=[4 , 1, 2, 3] 
        '''
        if self.__tamanhoFila == self.__tamanhoLimite: raise FilaException("Fila cheia!")
        
        novoFinal= self.__final + 1 % self.__tamanhoLimite
        self.__dados[novoFinal]= carga
        self.__tamanhoFila+=1
        self.__final= novoFinal
        
    
    def remover(self)->any:
        
        ''''
              F   I                     remover
        fila=[4 , 1, 2, 3] 
        '''
        
        if self.estaVazia: raise FilaException("Fila Vazia!")
        
        elementoRemovido=self.__dados[self.__inicio]
        
        self.__inicio= (self.__incio + 1) % self.__tamanhoLimite
        
        self.__tamanhoFila -= 1
        
        return elementoRemovido
    
    
    def imprimir(self)-> str:
        ''''
              F   I                     remover
        fila=[4 , 1, 2, 3] 
              c                           
        '''
        
        todaFila=''
        
        if self.estaVazia():
            return 'Vazia'
        
        elemento=self.__inicio
        cont= self.__tamanhoFila
        
        while cont>0:
            
            todaFila+= ' '+str(self.__dados[elemento])
            
            elemento= (elemento + 1) % self.__tamanhoLimite
            
            cont-= 1 
            
            
        return todaFila

        
                