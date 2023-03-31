class PilhaException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)
        


class Pilha:
    """A classe Pilha implementa a estrutura de dados "Pilha" utilizando a técnica encadeada.
       A classe foi desenvolvida de modo a permitir que qualquer tipo de dado seja armazenado como carga
       de um nó.

     Attributes:
        topo (No): referência para o nó que se encontra no topo da lista
        quantidade (int): número de elementos existentes na pilha
    """
    def __init__(self):
        """ Construtor padrão da classe Pilha sem argumentos. Ao instanciar
            um objeto do tipo Pilha, esta iniciará vazia. 
        """
        self.__colecao = []

        
    def estaVazia(self)->bool:
        """ Método que verifica se a pilha está vazia .

        Returns:
            boolean: True se a pilha estiver vazia, False caso contrário.

        Examples:
            p = Pilha()
            ...   # considere que temos internamente na pilha [10,20,30,40]<- topo
            if(p.estaVazia()): 
               # instrucoes quando a pilha estiver vazia
        """
        return len(self.__colecao)==0

    def __len__(self):
        return len(self.__colecao)

    def tamanho(self)->int:
        """ Método que retorna a quantidade de elementos existentes na pilha

        Returns:
            int: um número inteiro que determina o número de elementos existentes na pilha

        Examples:
            p = Pilha()
            ...   # considere que temos internamente a pilha [10,20,30,40]<- p
            print (p.tamanho()) # exibe 4
        """ 
        return len(self.__colecao)

    def elemento(self, posicao:int)->any:
        """ Método que recupera a carga armazenada em um determinado elemento da pilha

        Args:
            posicao (int): um número correpondente à ordem do elemento existente.
                           Sentido: da base em direção ao topo
        
        Returns:
            Any: a carga armazenada no elemento correspondente à posição indicada.

        Raises:
            PilhaException: Exceção lançada quando uma posição inválida é
                  fornecida pelo usuário. São inválidas posições que se referem a:
                  (a) números negativos
                  (b) zero
                  (c) número natural correspondente a uma posição  que excede a
                      quantidade de elementos da lista.                      
        Examples:
            p = Pilha()
            ...   # considere que temos internamente a pilha [10,20,30,40]<-topo
            posicao = 5
            print (p.elemento(3)) # exibe 30
        """
        if posicao <= 0 or posicao > self.tamanho():
            raise PilhaException(f"Posicao invalida. A pilha so tem {len(self.__colecao)} elementos.")
        
        return self.__colecao[posicao-1]
        
                
    def busca(self, key:any)->int:
        """ Método que retorna a posicao ordenada, dentro da pilha, em que se
            encontra uma chave passado como argumento. No caso de haver mais de uma
            ocorrência do valor, a primeira ocorrência será retornada.
            O ordenamento que determina a posição é da base para o topo.

        Args:
            key (any): um item de dado que deseja procurar na pilha
        
        Returns:
            int: um número inteiro representando a posição, na pilha, em que foi
                 encontrada a chave.

        Raises:
            PilhaException: Exceção lançada quando o argumento "key"
                  não está presente na pilha.

        Examples:
            p = Pilha()
            ...   # considere que temos internamente a lista [10,20,30,40]<-topo
            print (p.elemento(40)) # exibe 4
        """
        for i in range(len(self.__colecao)):
            if key == self.__colecao[i]:
                return i+1
        raise PilhaException(f"A chave {key} não está na pilha.")

    def topo(self)->any:
        """ Método que devolve o elemento localizado no topo, sem desempilhá-lo.
    
        Returns:
            any: o conteúdo armazenado no elemento do topo

        Raises:
            PilhaException: Exceção lançada quando se tenta consultar o topo de uma
                   uma pilha vazia
                    
        Examples:
            p = Pilha()
            ...   # considere que temos internamente a lista [10,20,30,40]
            dado = p.topo()
            print(dado) # exibe 40
        """
        if self.estaVazia():
            raise PilhaException("Pilha Vazia")
        return self.__colecao[-1]

    def empilha(self, carga:any):
        """ Método que adiciona um novo elemento ao topo da pilha

        Args:
            carga (any): a carga que será armazenada no novo elemento do topo da pilha.

        Examples:
            p = Pilha()
            ...   # considere que temos internamente a lista [10,20,30,40]
            p.empilha(50)
            print(p)  # exibe [10,20,30,40,50]
        """
        self.__colecao.append(carga)


    def desempilha(self)->any:
        """ Método que remove um elemento do topo da pilha e retorna
            sua carga correspondente.
    
        Returns:
           any: a carga armazenada no elemento removido

        Raises:
            PilhaException: Exceção lançada quando se tenta remover algo de uma pilha vazia
                    
        Examples:
            p = Pilha()
            ...   # considere que temos internamente a lista [10,20,30,40]
            dado = p.desemplha()
            print(p) # exibe [10,20,30]
            print(dado) # exibe 40
        """
        if self.estaVazia():
            raise PilhaException('Não há elementos para remoção. Pilha Vazia')
        
        return self.__colecao.pop()
   
    def imprime(self):
        """ Método que exibe na tela a sequência ordenada dos elementos da pilha

        Examples:
            p = Pilha()
            ...   # considere que temos internamente a pilha [10,20,30,40]<-topo
            p.imprimir()) # exibe Lista: [10,20,30,40] <- topo
        """  
        print(self.__str__())
        
    def __str__(self)->str:
        """ Método que retorna a ordenação atual dos elementos da pilha, do
            topo em direção à base

        Returns:
           str: a carga dos elementos da pilha, do topo até a base
        """  
        s="["
        for i in range(len(self.__colecao)):
            s += f'{self.__colecao[i]}, '
        return s[:-2] + ' ] <-topo'

 

