class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class no:
    def __init__(self, carga: any) -> None:
        self.__carga = carga
        self.__prox = None

    def __str__(self) -> str:
        return str(self.carga)

    @property
    def prox(self) -> 'no':
        return self.prox

    @property
    def carga(self) -> any:
        return self.carga


class pilha():

    def __init__(self):
        self.__topo = None
        self.__tamanho = 0

    def estaVazia(self) -> bool:
        return self.__topo == None

    def tamanho(self) -> int:
        return self.__tamanho

    def __len__(self) -> int:
        return self.__tamanho

    def empilha(self, valor: any):
        novo = no(valor)
        novo.prox = self.__topo
        self.topo = novo
        self.__tamanho += 1

    def desempilha(self) -> any:
        try:
            # garanta que a pilha não está vazia
            assert not self.estaVazia()
            topo = self.__topo.carga
            self.__topo = self.__topo.prox
            self.__tamanho -= 1
            return self.topo
        except AssertionError:
            raise PilhaException(f'A está vazia impossível desempilhar')

    def elemento(self, posicao: int) -> any:
        try:
            # garanta que a posição vai estar entre 1 e o tamanho
            assert posicao > 0 and posicao <= self.tamanho
            cont = self.__tamanho
            cursor = self.__topo
            while(cont > posicao):
                self.cursor = self.cursor.prox
                cont -= 1
            return cursor.carga
        except AssertionError:
            raise PilhaException(
                f'Posicao inválida para apilha atual com {self.tamanho} elementos')

    def busca(self, valor: any) -> int:
        cont = self.__tamanho
        cursor = self.__topo
        while (cursor != None):
            if (cursor.carga == valor):
                return cont
            self.cursor = self.cursor.prox
            cont -= 1
        raise PilhaException(f'Valor {valor} não está na pilha')

    def topo(self) -> any:
        try:
            # garanta que a pilha não está vazia
            assert not self.estaVazia()
            return self.__topo.carga
        except AssertionError:
            raise PilhaException(f'A pilha esta Vazia')

    def inverter(self) -> bool:
        try:
            assert not self.estaVazia()
            pilhaAuxiliar = pilha()
            while(not self.estaVazia()):
                pilhaAuxiliar.empilha(self.desempilha())
            self.__topo = pilhaAuxiliar.__topo
            self.__tamanho = pilhaAuxiliar.__tamanho
        except AssertionError:
            raise PilhaException(f'A pilha so possui um elemento')

    def concatena(self, pilha2: object):
        aux = pilha()
        while(not pilha2.estaVazia()):
            aux.empilha(pilha2.desempilha())
        while(not aux.estaVazia()):
            self.empilha(aux.desempilha())

    def esvazia(self):
        while(self.__tamanho > 0):
            self.desempilha()

    @classmethod
    def doubleconcatena(cls, pilha1: object, pilha2: object) -> object:

        out = pilha()
        pilhaAuxiliar = pilha()

        while(not pilha1.estaVazia()):
            pilhaAuxiliar.empilha(pilha1.desempilha())
        while(not pilhaAuxiliar.estaVazia()):
            out.empilha(pilhaAuxiliar.desempilha())

        while(not pilha2.estaVazia()):
            pilhaAuxiliar.empilha(pilha2.desempilha())
        while(not pilhaAuxiliar.estaVazia()):
            out.empilha(pilhaAuxiliar.desempilha())

        return out

    @classmethod
    def binario(cls, valor: int) -> str:
        bin = pilha()
        count = valor

        while (count//2) != 0:
            bin.empilha(count % 2)
            count = count // 2

        out = ''

        while not bin.estaVazia():
            out += f'{bin.desempilha()}'

        return out


'''
queremos carga do elemento na posição 3

        cont = 3

        [5] prox -> [4] <- topo (ultimo elemnto a ser inserido)
        [4] prox -> [3] 
cursor  [3] 
        [2]
        [1] prox -> None <- base (primeiro elemento a ser inserido)
'''
