class Node:
    def __init__(self,id:int,key:any, carga:any):
        self.__key=key
        self.id=id
        self.carga = carga
        self.esq = None
        self.dir = None
        
    @property    
    def key(self):
        return self.__key
    
    def __str__(self):
        return f'key:{self.__key}| carga: {str(self.carga)}'
    
    def __eq__(self, __value: object) -> bool:
        return self.__key ==self.__key
#== == == ==Classe que contém todos os métodos aárvore binária
class ArvoreBusca:
    #== == == Método que cria a raiz               
    def __init__(self, carga_da_raiz=None):
        self.__raiz=Node(carga_da_raiz) if carga_da_raiz  !=  None else carga_da_raiz#== == Caso não seja declarado um nó raiz, a árvore existirá, porém vazia.

    ''' Exemplo de árvore binária co busca
                    20
                11        24
             5         21     49
          3    8          23
    '''
    @property
    def raiz(self):
        return self.__raiz
    
    #== == == Método que confere se a raiz está vazia            
    def estaVazia(self)->bool:
        if self.__raiz==None: return True
        else: return False
    
    #== == == Retorna o Nó raiz, caso ele exista            
    def getRaiz(self)->any:
        try:
            assert self.__raiz  !=  None 
            return self.__raiz
        except AssertionError:
            raise SearchArborException(1,'NO ROOT!')