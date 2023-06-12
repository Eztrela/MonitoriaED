class No:
    def __init__(self, carga:any):
        self.carga = carga
        self.esq = None
        self.dir = None
        
    def __str__(self):
        return f' carga: {str(self.carga)}'
    
    def __eq__(self, no:'No'):
        return self.carga == no.carga

#== == == ==Classe que contém todos os métodos a árvore binária
class ArvoreBusca:
    #== == == Método que cria a raiz               
    def __init__(self, carga_da_raiz=None):
        self.__raiz=No(carga_da_raiz) if carga_da_raiz  !=  None else carga_da_raiz#== == Caso não seja declarado um nó raiz, a árvore existirá, porém vazia.
        
        self.__tamanho= 0

    ''' 
    Exemplo de árvore binária com busca
                    20
                11        24
             5         21     49
          3    8          23
    '''
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
        
        if no.carga == cargaAdicionar:
            raise Exception('Esse objeto já existe!')
             
        if cargaAdicionar < no.carga :
            if no.esq is None:
                no.esq = No(cargaAdicionar)

            else:
                self.__adicionar(no.esq)
        
        elif cargaAdicionar > no.carga :
            
            if no.dir is None:
                no.dir = No(cargaAdicionar)
            
            else:
                self.__adicionar(no.dir)
                
    
    def preordem(self):
        self.__preordem(self.__raiz)

    def __preordem(self, no: No):
        
        if no is not None:
            print(f'{no.carga}', end=' ')
            
            self.__preordem(no.esq)
            
            self.__preordem(no.dir)

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
    

    def go(self, key)->any:
        if self.__raiz is None:
            return None
        else:
            return self.__go(key, self.__raiz)
        
    def __go(self, valorProcurado, nodeAtual:No)->'No':
    
        if nodeAtual is None: 
            return None

        elif nodeAtual.carga == valorProcurado:
            return nodeAtual
        
        else:
            
            nodeAchado=nodeAtual
            
            if valorProcurado < nodeAtual.carga: 
                nodeAchado=self.__go(valorProcurado, nodeAtual.esq)
                return nodeAchado
            
            elif valorProcurado > nodeAtual.carga:
                nodeAchado=self.__go(valorProcurado, nodeAtual.dir)
                return nodeAchado