#== == == == Pilha Exception
class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        
#== == == == No é o elemento que será adiciona na estrutura de dados encadeada.

#== == == == A estrutura de dado Pilha, ou LIFO.
class Pilha:
    def __init__(self):
        self.__pilha=[] # A pilha inicia vazia.

#== == == == Método para examinar se a pilha está vazia
    def estaVazia(self)->bool:
        return len(self.__pilha) == 0
    
#== == == == Método para checar o tamanho da Pilha
    def tamanho(self):
        return len(self.__pilha)

#== == == == Método que retornára o contéudo de um nó dependendo da possição exigida.
    def elemento(self, posicao:int)->any:
        try:
            #== == Só funciona se: a pilha NÃO estiver vazia e a posição inserida não exceda o tamanho da lista.
            assert not self.estaVazia() ,'A lista está vazia!'
            assert self.tamanho()>=posicao and posicao>0, f'A posição inserida é inválida, pois o tamanho da pilha é de {self.tamanho()} nó(s)!'
            
            return self.__pilha[posicao-1]
        
        except AssertionError as AE:
            raise PilhaException(AE)
        except Exception as E:
            raise PilhaException(E)
        else:
            return valorNo

#== == == == Método que retornára a posição de um Nó através do valor no qual foi inserido.
    def busca(self, conteudo:any)->int:
        try:
            #== == O método só não funciona quando a lista estiver vazia
            assert not self.estaVazia() ,'A lista está vazia!'
            
            for i in range(len(self.__pilha)):
                if self.__pilha[i]==conteudo:
                    return i
                              
            raise PilhaException('Contéudo inserido não foi encontrado!') # o contéudo não foi Achado.
    
        except AssertionError as AE:
            raise PilhaException(AE)
        except Exception as E:
            raise PilhaException(E)
                
##== == == == Método que Modificará o contéudo de um nó a partir da possição exigida.
    def modificar(self, posicao:int, conteudo: any):
        try:
            #== == Só funciona se: a pilha NÃO estiver vazia e a posição inserida não exceda o tamanho da lista.
            assert not self.estaVazia() ,'A lista está vazia!'
            assert self.tamanho()>=posicao and posicao>0, f'A posição inserida é inválida, pois o tamanho da pilha é de {self.tamanho()} nó(s)!'
        
            self.__pilha[posicao-1]= conteudo
 
        except AssertionError as AE:
            raise PilhaException(AE)
        
        except Exception as E:
            raise PilhaException(E)
        
    #== == Adiciona um novo Nó na Pilha.
    def empilha(self, conteudo:any):
        self.__pilha.append(conteudo) # O final da lista é considerado o topo.
        
    #== == Remove o Ùltimo Nó adicionado na Pilha.
    def desempilha(self)->any:
        try:
            assert not self.estaVazia() ,'A lista está vazia!'
            return self.__pilha.pop() # Remove no final da lista, o topo.
            
        except AssertionError as AE:
            raise PilhaException(AE)
        
        except Exception as E:
            raise PilhaException(E)

    #== == Desempilha a pilha até ela possuir Zero Nós.
    def esvazia(self):
        try:
            return self.__pilha.clear()
        except:
            pass
        
    
    #== == Mètodo extra 1... Concatenador de Pilhas.
    
    def concatenar(self,outraPilha):
        pilhaAuxiliar=Pilha()
        while not outraPilha.estaVazia():
            pilhaAuxiliar.empilha(outraPilha.desempilha())
        
        while not pilhaAuxiliar.estaVazia():
            self.empilha(pilhaAuxiliar.desempilha())
            
    
    #== == Mètodo extra 2... Inversor de Pilhas.
    
    def inverter(self):
        pilhaAuxiliar=Pilha()
        while not self.estaVazia():
            pilhaAuxiliar.empilha(self.desempilha())
        
        self.__pilha=pilhaAuxiliar.__pilha
        

    def __str__(self)->str:
        if self.tamanho()==0:
            return 'Empty'
        s = ''
        for i in range(len(self.__pilha)):
            s+= f'=|Nó {i+1}: {self.__pilha[i]} |= '
        return s + f'\n tamanho: {len(self.__pilha)}'