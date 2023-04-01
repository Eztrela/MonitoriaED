class FilaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class FilaSequencial:
    def __init__(self):
        self.__tamanho_array = 10
        self.__dados = []
        self.__inicio = 0
        self.__final = -1
        self.__tamanho_fila = 0

    def estaVazia(self):
        return self.__tamanho_fila == 0

    def busca(self, valor: any) -> int:
        cont = self.__inicio
        for i in range(self.__tamanho_fila):
            if(self.__dados[cont] == valor):
                return cont + 1
            cont = (cont + 1) % self.__tamanho_array
            # if cont == self.__tamanho_array:
            #     cont = 0
        raise FilaException(f'O valor {valor} não está na fila')

    def enfileira(self, valor: any):
        try:
            # verifica se há espaços disponíveis na fila para enfileirar
            assert self.__tamanho_fila < self.__tamanho_array
            # move o final para uma posição disponível do array
            self.__final = (self.__final + 1) % self.__tamanho_array
            # insere na posição disponível o novo valor
            self.__dados[self.__final] = valor
            # aumenta o tamanho da fila em um
            self.__tamanho_fila += 1
        except AssertionError:
            raise FilaException(f'A fila está cheia')

    def desenfileira(self) -> any:
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
        '''
        2 3 4 5 10
        final                                        inicio    
        [10 None None None None None None None 5      4]

                         final  inicio       
        [124   45    1     10     3   4   5   565 120 568]
        '''
