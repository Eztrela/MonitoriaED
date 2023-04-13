class FilaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class FilaSequencial:
    def __init__(self):
        
        self.__tamanho_array = 10
        self.__dados = [None for i in range(self.__tamanho_array)]
        
        self.__inicio = 0
        self.__final = -1
        
        self.__tamanho_fila = 0

    def estaVazia(self)->bool:
        '''Verifica se a fila está vazia'''
        return self.__tamanho_fila == 0

    def busca(self, valor: any) -> int:
        '''recebe uma chave, percorre todo a fila em busca da posição dela'''
        #4 elementos
        #[0, 1, 2, None]
        # 0  1  2, 3
        
         #posicao: 3
        #  3 % 4  =  3

              #I    #F
        #[None,0, 1, 2 ]
        # 0,   1, 2, 3 , 4
        
        #posicao: 4
        #  posicao  % 4  =  0
        posicaoArray= self.__inicio
        """Procura a posição de um elemento na fila."""
        
        for posicaoFila in range(self.__tamanho_fila):  #0      4
            #         cF  I
            #[ 3, 4 , 5, 6 ]    #valor  7
            #  0,  1, 2, 3
            # return -1
            
            if(self.__dados[posicaoArray] == valor):
                return posicaoFila + 1
            
            posicaoArray = (posicaoArray + 1) % self.__tamanho_array 

            #cont= (3  + 1) %  4 = 0  
            
            # if cont == self.__tamanho_array:
            #     cont = 0
            
        return -1
    
    def elemento(self, posicao:int):
        '''
        Este método retornar o valor de um elemento dentro da fila circular em questão da fila e não do tamanho limite 
        '''
        '''
        Na fila circular não se é possível saber a posicao certa de um elemento, pois este pode ocupar uma posição aleatória dentro do array.
        Devido a isto, devemos percorrer, com um posicaoArray, a nossa fila começando pela posição inicial, até que o posicaoArray atinja a posição desejada.
        '''
        if posicao >self.__tamanho_fila or posicao<=0:
            raise FilaException('Posição Inválida! ')       
        
        posicaoArray= self.__inicio #o posicaoArray irá começar no primeiro nó da fila.
        posicaoFila=1
        
        while posicaoFila<=self.__tamanho_fila:
            if posicaoFila ==posicao:
                return self.__dados[posicaoArray]
            
            posicaoArray=  (posicaoArray + 1) % self.__tamanho_array # utilizamos a fórmula para deslocar o posicaoArray
            posicaoFila+=1
            
        
        
    def enfileira(self, valor: any):
        """Insere um nó no final da fila
        
        Adicionando elemento 50.
        
        Exemplo comum:
        
        Inicio               Final  
        [10     20     30     40 null ]
                  Inicio                Final
        Resultado [10    20   30   40    50]
        
        Exemplo Atipico:
        
                  Inicio              Final  
        [null      10     20     30     40  ]
        
                  Final   Inicio                
        Resultado [ 50    10    20   30   40]
        
        """
        try:
            # verifica se há espaços disponíveis na fila para enfileirar
            assert self.__tamanho_fila < self.__tamanho_array
    
            # move o final para uma posição disponível do array
            
            self.__final = (self.__final + 1 ) % self.__tamanho_array
                       
            # insere na posição disponível o novo valor
            self.__dados[self.__final] = valor #!! !! !! !! ERRO, Não foi iniciado a lista de dados
            # aumenta o tamanho da fila em um
            self.__tamanho_fila += 1
        except AssertionError:
            raise FilaException(f'A fila está cheia')

    def desenfileira(self) -> any:
        '''
        Remove e retorna o primeiro elemento da Fila sequencial.
        
        2 3 4 5 10
        final                                        inicio    
        [10 None None None None None None None 5      4]

                         final  inicio       
        [124   45    1     10     3   4   5   565 120 568]
        '''
        try:
            #Verifica se a fila não está Vazia
            assert not self.estaVazia()
            #salva o valor que está no inicio            
            valorInicial = self.__dados[self.__inicio]
            # move o inicio para a proxima posição da fila
            self.__inicio = (self.__inicio + 1) % self.__tamanho_array
            #diminui o tamanho da fila em um
            self.__tamanho_fila -= 1
            #retorna o valor anteriormente salvo que estava no inicio
            return valorInicial
        except AssertionError:
            raise FilaException(f'A fila já está Vazia')
        
    def __str__(self) -> str:
        s=''
        posicaoArray=self.__inicio
        posicaoFila=1
        
        while posicaoFila<= self.__tamanho_fila:
            s+= f'|{posicaoFila}: {self.__dados[posicaoArray]:^2} |' 
            posicaoFila+=1
            posicaoArray= (posicaoArray + 1)% self.__tamanho_array
        
        s+= f'\n fila tamanho: {self.__tamanho_fila}, tamanho limite: {self.__tamanho_array}'
        
        return s