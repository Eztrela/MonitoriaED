class pilhaException(Exception):
    def __init__(self, error_id, msg):
        super().__init__(f'{error_id} {msg}')


class pilhaSequencialMonitoria:

    def __init__(self):
        self.__dados = []

    def empilha(self, value: any) -> bool:
        self.__dados.append(value)

    def desempilha(self) -> any:
        return self.__dados.pop()

    def __len__(self) -> int:
        return len(self.__dados)

    def busca(self, value: any) -> int:
        for i in range(len(self.__dados)):
            if self.__dados[i] == value:
                return i
        return -1

    def elemento(self, index: int) -> any:
        if index > len(self) or index < 0:
            raise pilhaException(1, "Posição não existe")
        return self.__dados[index]

    def __str__(self) -> str:
        s = ''
        for num in self.__dados:
            s += f'{num} '
        return s
    
    def estaVazia(self) -> bool:
        return len(self) == 0

    def esvazia(self):
        '''
        Esvazia a Pilha
        '''
        while not self.estaVazia():
            self.desempilha()
    
    def modificar(self, index):
        