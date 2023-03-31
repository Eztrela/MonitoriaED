class PilhaException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)
        

class No:
    def __init__(self, carga:any):
        self.__carga = carga
        self.__prox = None
    
    def getCarga(self):
        '''Retorna a Carga do nó'''
        return self.__carga

    def getProximo(self)->'No':
        '''Retorna qual o próximo nó da lista'''
        return self.__prox
    
    def setCarga(self,valor):
        self.__carga=valor
    
    def setProximo(self, novoProx:'No'):
        '''Informa para ao Nó para qual outro deverá apontar. '''
        self.__prox = novoProx

    def temProximo(self)->bool:
        '''Afirma que o nó está apontando para o vazio '''
        return self.__prox == None

    def __str__(self):
        
        return f'{self.__carga}'


class Pilha:

    def __init__(self):

        self.__topo = None 
        self.__tam = 0
    

    def __len__(self):
        '''Retorna o tamanho da lista'''
        return self.__tam

    def estaVazia(self)->bool:
        '''Informa se a lista está vazia, a partir da afirmação: O topo está apontando para None'''
        return self.__tam==0

    def tamanho(self)->int:
        '''Retorna o tamanho da lista'''
        return self.__tam

    def elemento(self, posicaoDesejada:int)->any:
        """ Método que recupera a carga armazenada em um determinado elemento da pilha"""
        if self.estaVazia():raise PilhaException('A pilha está vazia')
        
        if posicaoDesejada<=0 or posicaoDesejada> self.__tam: raise PilhaException(f'Posição inserida: {posicaoDesejada} ')       
        
        cursor=self.__topo
        cursorPosicao=self.__tam
        
        while cursor != None:
            
            if cursorPosicao== posicaoDesejada:
                return cursor.getCarga()
            
            cursor=cursor.getProximo()
            cursorPosicao-=1
        

                
    def busca(self, key:any)->int:
        """ Método que retorna a posicao ordenada, dentro da pilha, em que se encontra uma chave passado como argumento."""
        
        if self.estaVazia(): raise PilhaException('Pilha vazia.')
        
        cursor=self.__topo
        posicaoKey=self.__tam
        
        while cursor!=None:
                        
            if key== cursor.getCarga(): #Verificamos se a carga do nó é igual a chave que procuramos.
                '''Lembrando, a pilha foi considerada como: o topo é o último nó. 
                Logo os passos precisam ser contados na ordem inversa ao tamanho:
                
                Topo-> [1 , 2 , 3 , 4, 5, 6]  Tamanho=6
                
                keyProcurada= 3
                
                o laço será execultado três vezes.
                
                passos=2 quando o  "if" for True 
                
                será retornado 6 (tamanho da pilha ) - 2 (vezes que o laço foi execultado. )
                
                A chave se encontra na posição 4 da pilha.
        
                '''
                return posicaoKey
            cursor=cursor.getProximo()
            posicaoKey-=1
        return -1
        

    def topo(self)->any:
        """ Método que devolve o elemento localizado no topo, sem desempilhá-lo. """
        return self.__topo

    def empilha(self, carga:any):
        '''Lembrando, a pilha foi considerada como: o topo é o último nó. 
        O nó é inserido no topo da pilha:
        
        Topo-> [1 , 2 , 3 , 4, 5, 6]  Tamanho=6
        
        Inserir Node 0
        
        O No contendo 0 é criado, e ele aponta para None
        
        fazemos o Node 0 para apontar o Atual Topo (1)
        
        Consideramos o Node 0 como o novo Topo da pilha.
        
        Incrementamos o tamanho da pilha 
        
        
        Topo-> [0, 1 , 2 , 3 , 4, 5, 6]  Tamanho=7
        '''
        
        novoNo=No(carga)
        novoNo.setProximo(self.__topo)
        self.__topo=novoNo
        self.__tam+=1       

    def desempilha(self)->any:
        """ Método que remove um elemento do topo da pilha e retorna sua carga correspondente. """
        if self.estaVazia():
            raise PilhaException('A pilha está vazia!')
        
        NodeCarga=self.__topo.getCarga()
        self.__topo= self.__topo.getProximo()
        self.__tam-=1
        return NodeCarga
    
    def modificar(self,posicaoDesejada:int, novoValor:any)->bool:
        '''Modifica um Nó a partir de uma posição.'''
        if self.estaVazia():return False
        if posicaoDesejada<=0 or posicaoDesejada> self.__tam: return False      
        
        
        cursor=self.__topo
        cursorPosicao=self.__tam
        while cursor!=None:
            if cursorPosicao==posicaoDesejada:
                try:
                    cursor.setCarga(novoValor)
                    return True
                except:
                    return False
            cursor=cursor.getProximo()
            cursorPosicao-=1
   
    def imprime(self):
        if self.__tam==0:
            return 'Empty'
        s = ''
        cont=0
        cursor=self.__topo
        while cont< self.__tam:
            
            if cont==0: s+=f'|TOPO: {cursor}| '
            
            else:s+=f'|Nó {self.__tam-cont}: {cursor}| '
            
            cont+=1
            cursor=cursor.getProximo()
        return s + f'tamanho: {self.__tam}'
        
    def __str__(self)->str:
        """ Método que retorna a ordenação atual dos elementos da pilha, do
            topo em direção à base

        Returns:
           str: a carga dos elementos da pilha, do topo até a base
        """
          
        s = 'topo->[ '
        cursor = self.__topo
        while(cursor != None):
            s += f'{cursor.getCarga()} '
            if cursor.getProximo() is not None:
                s+= ', '
            cursor = cursor.getProximo()
        # s = 
        # s += ' ]'
        # return s[:-2] + ' ]'
        return s + f"] tamanho:{self.__tam}"
    
    def inverte( self ):
        '''
        Retorna True se foi possível inverter a pilha ou False caso contrário
        '''
    
    
    def concatena( self, pilha2:'Pilha'):
        '''
            Recebe uma segunda pilha p2, e transfira todos os elementos da pilha p2 para o topo da pilha responsável pela invocação da operação.
        '''
        
        pass
