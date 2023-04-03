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
        
        cont = self.__inicio
        """Proca a posição de um elemento na fila."""
        
        for i in range(self.__tamanho_fila):  #0      4
            
            #         cF  I
            #[ 3, 4 , 5, 6 ]    #valor  7
            #  0,  1, 2, 3
            # return -1
            
            if(self.__dados[cont] == valor):
                return cont + 1
            
            cont = (cont + 1) % self.__tamanho_array 
            
            #cont= (3  + 1) %  4 = 0  
            
            # if cont == self.__tamanho_array:
            #     cont = 0
            
        return -1

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
            self.__final = (self.__final + 1) % self.__tamanho_array
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
            inicio = self.__dados[self.__inicio]
            # move o inicio para a proxima posição da fila
            self.__inicio = (self.__inicio + 1) % self.__tamanho_array
            #diminui o tamanho da fila em um
            self.__tamanho_fila -= 1
            #retorna o valor anteriormente salvo que estava no inicio
            return inicio
        except AssertionError:
            raise FilaException(f'A fila já está Vazia')