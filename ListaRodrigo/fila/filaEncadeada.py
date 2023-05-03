from  filaException import FilaException


class Node:
    
    def __init__(self,carga:any) -> None:
        self.carga= carga # elemento armazenado
        self.prox=None # para quem ele aponta na lista


class Fila:
    
    def __init__(self):
        self.__inicio=None
        self.__final=None
        self.__tamanho=0
    
        
    def estaVazia(self)->bool:
        return self.__inicio==None   
        
    def inserir(self, carga):
        novoNo= Node(carga)

        if self.__final==None: #Caso a fila esteja vazia
            self.__final=novoNo
            self.__inicio=novoNo
        
        else: #Já há algum elemento
            self.__final.prox=novoNo
            self.__final=novoNo
        
        self.__tamanho+=1
            
    
    def remover(self)->any:
        if self.estaVazia: raise FilaException("Fila Vazia!")
        
        cargaRemovida=self.__inicio.carga
        
        self.__inicio = self.__inicio.prox      
        
        self.__tamanho-=1
        
        return cargaRemovida
    
    
    def __str__(self) -> str:
        
        todaFila=''
        cursor=self.__inicio
        
        if self.estaVazia():
            return 'Vazia'
        
        while cursor != None:
            todaFila+= str(cursor.carga)
            cursor= cursor.prox
            
        return todaFila
        
    def imprimir(self)-> str:
        
        todaFila=''
        cursor=self.__inicio
        
        if self.estaVazia():
            return 'Vazia'
        
        while cursor != None:
            todaFila+= str(cursor.carga)
            
            cursor= cursor.prox
    
            
        return todaFila