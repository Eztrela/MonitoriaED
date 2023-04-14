from Pilha.Pablo.pilhaencadeada import pilha
class FilaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class noCabeca:
    def __init__(self):

        self.inicio = None
        self.fim = None
        self.tamanho = 0


class no:
    def __init__(self, carga: any):
        self.prox = None
        self.carga = carga

    def __str__(self):
        return str(self.carga)


class filaEncadeadaNoCabeca:
    def __init__(self):
        self.__head = noCabeca()

    def estaVazia(self):
        return self.__head.tamanho == 0

    def tamanho(self) -> int:
        return self.__head.tamanho

    def __len__(self) -> int:
        return self.__head.tamanho

    def frente(self) -> object:
        return self.__head.inicio

    def final(self) -> object:
        return self.__head.fim

    def elemento(self, posicao: int) -> any:
        try:
            assert posicao > 0 and posicao <= self.__head.tamanho
            cont = 1
            cursor = self.__head.inicio
            while(cont < posicao):
                cursor = cursor.prox
                cont += 1
            return cursor.carga

        except AssertionError:
            raise FilaException(
                f'Posicao inválida para a pilha atual com {self.__head.tamanho} elementos')

    def busca(self, valor: any) -> int:
        cont = 1
        cursor = self.__head.inicio
        while (cursor != None):
            if (cursor.carga == valor):
                return cont
            cursor = cursor.prox
            cont += 1
        raise FilaException(f'Valor {valor} não está na pilha')

    def modificar(self, posicao: int, valor: any):
        try:
            assert posicao > 0 and posicao <= self.__head.tamanho
            cont = 1
            cursor = self.__head.inicio
            while(cont < posicao):
                cursor = cursor.prox
                cont += 1
            cursor.carga = valor

        except AssertionError:
            raise FilaException(
                f'Posicao inválida para a pilha atual com {self.__head.tamanho} elementos')

    def enfileira(self, valor: any):
        novo = no(valor)
        if(self.estaVazia()):
            self.__head.inicio = novo
            self.__head.fim = novo
        else:
            self.__head.fim.prox = novo
            self.__head.fim = novo

        self.__head.tamanho += 1

    def desenfileira(self) -> any:
        try:
            assert not self.estaVazia()
            inicial = self.__head.inicio
            self.__head.inicio = inicial.prox
            self.__head.tamanho -= 1
            return inicial.carga

        except AssertionError:
            raise FilaException(f'A pilha está Vazia impossivel desempilhar')

    def __str__(self):
        s = ''
        cursor = self.__head.inicio
        while(cursor != None):
            s += f'{cursor} '
            cursor = cursor.prox
        return s

    def inverte(self):
        try:
            assert not self.estaVazia()
            pilhaAuxiliar = pilha()

            while(not self.estaVazia()):
                pilhaAuxiliar.empilha(self.desenfileira())
            while(not pilhaAuxiliar.estaVazia()):
                self.enfileira(pilhaAuxiliar.desempilha())
        except AssertionError:
            raise FilaException(f'A pilha está Vazia')

    def esvazia(self):
        while(not self.estaVazia()):
            self.desenfileira()

    def concatenar(self, fila: object):
        while not fila.estaVazia():
            self.enfileira(fila.desenfileira())

    @classmethod
    def combina(cls, f_res, f1, f2):
        while(not f1.estaVazia() or not f2.estaVazia()):
            if(not f1.estaVazia()):
                f_res.empilha(f1.desempilha())
            if(not f2.estaVazia()):
                f_res.empilha(f2.desempilha())
        return f_res

    # @classmethod
    # def doubleconcatenar(cls, pilha1: object, pilha2: object):
    #     out = filaEncadeada()
    #     t = filaEncadeada()

    #     while not pilha1.estaVazia():
    #         t.empilha(pilha1.desempilha())
    #     while not t.estaVazia():
    #         out.empilha(t.desempilha())

    #     while not pilha2.estaVazia():
    #         t.empilha(pilha2.desempilha())
    #     while not t.estaVazia():
    #         out.empilha(t.desempilha())

    #     return out
    
    def remover(self, posicao:int):
        '''Remove o nó da Fila, '''
        if self.estaVazia():
            raise FilaException('Fila vazia')
        
        if posicao<=0 or posicao> len(self):
            raise FilaException('Posicão inválida')
        
        for posicaoCursor in range (len(self) ): #Percorrerá toda a fila
            
            nodeRemovido= self.desenfileira() # removi o elemento
            
            if posicaoCursor + 1 != posicao: # Checamos se a 
                self.enfileira(nodeRemovido)
    
    '''
    2ª solucação
    '''
    def remover2(self, posicao):
        
        if self.estaVazia():
            raise FilaException('Fila vazia')
        
        if posicao<=0 or posicao> len(self):
            raise FilaException('Posicão inválida')
        
        for posicaoCursor in range (len(self) ): #Percorrerá toda a fila
            
            if posicaoCursor + 1 != posicao: # Checamos se a 
                self.enfileira(self.desenfileira())
            
            else:
                self.desenfileira()
    
    def inverte(self) ->None:
        fila_aux = filaEncadeadaNoCabeca()
    
        for i in range(self.tamanho(), 0, -1): # este laço irá iniciar no final da fila
            '''Responsável por criar a fila com os elementos inversamente'''
            fila_aux.enfileira(self.elemento(i)) # a fila auxiliar irá adicionar os elementos de trás para frente da fila.
    
        for i in range(fila_aux.tamanho()): #Este laço será responsável por inserir
            '''Responsável por remover os elementos da fila atual e inserir os elementos inversos'''
            self.desenfileira() # Remove o primeiro elemento da fila original.
            self.enfileira(fila_aux.desenfileira()) #adiciona no final o elemento da ordem inversa.