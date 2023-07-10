from av2 import *
 
class Operacoes:
   arvore= ArvoreBusca()
      
   def adicionarPalavra(self, frase:str):
      '''Adiciona uma nova palavra na àrvore'''
      
      palavras=frase.split(' ')
      for p in palavras:
         self.arvore.adicionar(p.lower())     
      
      
   def exibirAscendente(self)->list[str]:
      self.arvore.preordem()

   def exibirDescendente(self)->list[str]:
      self.arvore.posordem()
   
   def exibirFrequencia(self,palavraChecar:str)->int:
      palavraRaiz= self.arvore.raiz
      if palavraRaiz is None:
         return 0
      else:
         return self.__exibirFrequencia(palavraChecar.lower(), palavraRaiz)
      
      
   def __exibirFrequencia(self, palavraBuscada:str, nodeAtual:No)->int:
      
      quantidadeEncontrada=0
      
      if nodeAtual is None: 
         return quantidadeEncontrada

      elif nodeAtual.carga==palavraBuscada:
         quantidadeEncontrada+=1
         
      if palavraBuscada < nodeAtual.carga: 
         return quantidadeEncontrada + self.__exibirFrequencia(palavraBuscada, nodeAtual.esq)

      elif palavraBuscada > nodeAtual.carga:
         return quantidadeEncontrada + self.__exibirFrequencia(palavraBuscada, nodeAtual.dir)

   
   
   def exibirDesbalanceamento(self)->int:
      palavraRaiz=self.arvore.raiz
      if palavraRaiz is None:
         return 0
   
      return self.__exibirDesbalanceamento(palavraRaiz) - 1
      
   
   def __exibirDesbalanceamento(self,node:No)->int:
      '''
         D
      C     F
   A      
      '''
      if node is None:
         return 0
      
      balanceamentoEsquerda=1
      balanceamentoDireita=1
         
      balanceamentoEsquerda += self.__exibirDesbalanceamento(node.esq)
      balanceamentoDireita += self.__exibirDesbalanceamento(node.dir)
      return max(balanceamentoEsquerda,balanceamentoDireita)