class No:
    def __init__(self, carga:any):
        self.carga = carga
        self.esq = None
        self.dir = None
        
    def __str__(self):
        return f' carga: {str(self.carga)}'

#== == == ==Classe que contém todos os métodos a árvore binária
class ArvoreBusca:
    #== == == Método que cria a raiz               
    def __init__(self, carga_da_raiz=None):
        self.__raiz=No(carga_da_raiz) if carga_da_raiz  !=  None else carga_da_raiz#== == Caso não seja declarado um nó raiz, a árvore existirá, porém vazia.
        self.__tamanho= 0
        
    @property
    def raiz(self):
        return self.__raiz
    
    #== == == Método que confere se a raiz está vazia            
    def estaVazia(self)->bool:
        if self.__raiz==None: return True
        else: return False

    def criarRaiz(self, valor_raiz:any)->any:
        if self.__raiz is not None:
            raise Exception('Já há raiz')
        self.__raiz=No(valor_raiz)
    
    
    def adicionar(self, carga:any)->None:
        if self.__raiz is None:
            self.criarRaiz(carga)
            return
        
        self.__adicionar(carga, self.__raiz)
        
    
    def __adicionar(self, cargaAdicionar:any, no:'No'):
        '''
        Alfabeticamente, caracteres maiúsculos são menores do que caracteres minúsculos. Por exemplo, ao ordenar de forma ascendente os nomes Denilson, alex e Diogo , o resultado será Denilson, Diogo e Alex
        '''
        '''
        Dessa forma, para adicionar um elemento será necessário comparar as letras em tamanhos iguais. Ou seja: 
        
        comparar AleXaNdre com alEx...    ALEXANDRE == ALEX ou alexandre == alex    
        '''
        
        
        """ 
        if cargaAdicionar.upper() < no.carga.upper() :
            if no.esq is None:
                no.esq = No(cargaAdicionar)

            else:
                self.__adicionar(no.esq)
        
        elif cargaAdicionar.upper() > no.carga.upper() :
            
            if no.dir is None:
                no.dir = No(cargaAdicionar)
            
            else:
                self.__adicionar(no.dir) """
                
                
    def emordem(self):
        self.__emordem(self.__raiz)

    def __emordem(self, no):
        if no is not None:
            self.__emordem(no.esq)
            print(f'{no.carga}', end=' ')
            self.__emordem(no.dir)

    def posordem(self):
        self.__posordem(self.__raiz)

    def __posordem(self, no):
        if no is None:
            return
        
        self.__posordem(no.esq)
        self.__posordem(no.dir)
        print(f'{no.carga}', end=' ')
    
    
    def busca(self, key)->bool:
        if self.__raiz is None:
            return False
        else:
            return self.__busca(key, self.__raiz)
        
    
    def __busca(self, valorProcurado, nodeAtual:No)->bool:
        
        if nodeAtual is None: 
            return False

        elif nodeAtual.carga==valorProcurado:
            return True
        
        else:
            if valorProcurado < nodeAtual.carga: 
                return self.__busca(valorProcurado, nodeAtual.esq)
            
            elif valorProcurado > nodeAtual.carga:
                return self.__busca(valorProcurado, nodeAtual.dir)
    
    
    def textoOrdenadoAscDesc(self)->tuple[list[str],list[str]]:
        """
        Como pedido, este método deverá retornar todas as palavras na ABB de maneira ascendente e descendente 
        
        possível retorno:
        ([Alegria, Baunilha, Caderno, Dogma], [Dogma, Caderno, Baunilha, Alegria] )
        """
        
        """
        recomendo criar duas funções para percorrer a ABB de forma ascendente e descendente 
        """
        
        return (self.__exibirAscendente(),self.__exibirDescendente())
    
    def __exibirAscendente()->list[str]:
        '''
        percore e armazena as palavra da ABB em um array. Começando da palavra de ordem menor, até a maior.
        
        Dica: Existe um método de exibição que já faz isso ;)
        '''     
   
    def __exibirDescendente():
        '''
        percore e armazena as palavra da ABB em um array. Começando da palavra de ordem maior, até a menor.
        
        Dica: Existe um método de exibição que já faz isso ;)
        '''
        
    
    def frequenciaPalavras(palavra:str)->int:
        '''
        percorre toda a ABB procurando as ocorrências de uma palavra na árvore. Assim como em adicionar, palavras contendo letras de tamanhos diferentes são consideradas do mesmo nível.
        
        Ou seja:
        
        AlEx == aleX    &&              AleXanDre !=  alex
        
        Dica: Recomendo implementar o método de busca da ABB. 
        '''
     
    def checarBalanceamento(self)->int:
        '''
        Este método fára algo parecido com o que ocorre em uma árvore AVL. Ele deverá percorrer a árvore, coletando o nível dos nós a esquerda e a direita da raiz {especulação minha}.
                
        Especulação: checar apenas o nível da raiz já baste:
        
        0            Banana
        1    Abacaxi         Cajá
        2                        Damasco     
        
        O nível de balanceamento desta árvore é:  
            direita_raiz - esquerda_Raiz
                2        -       1
                         =       0                      
        '''