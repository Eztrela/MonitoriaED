from arvoreBinaria import ArvoreBinaria
'''
        
          raiz
           5  
    2          4   
  1    3     6
                  
    
'''


arvore=ArvoreBinaria()
arvore.criaRaiz(5)

arvore.addEsq(2)
arvore.addDir(4)
arvore.descerEsquerda()
arvore.addDir(3)
arvore.addEsq(1)
arvore.resetCursor()

print('preordem')
arvore.preordem()
''' 5  2  1  3  4 '''
print()
print('emordem')
arvore.emordem()
'''1  2  3   5  4  '''
print()

print('posordem')
arvore.posordem()
''' 1 3 2  4  5'''
print()

arvore.descerDireita()

arvore.addEsq(6)

arvore.emordem()
'''1  2  3 5 6 4 '''

print('buscando o 3 ',arvore.busca(3))
print('buscando 10',arvore.busca(10))