from  pilhaException import PilhaException


class pilha:
    
    def __init__(self):
        self.__dados=[]
    
    
    def estaVazia(self)->bool:
        return len(self.__dados) == 0
    
    def inserir(self, carga):
        self.__dados.append(carga)
    
    
    def remover(self):
        '''
        1 3º topo
        2 2º
        3 1º
        '''
        if self.estaVazia(): raise PilhaException('Esta vazia')
    
        return self.__dados.pop()
        