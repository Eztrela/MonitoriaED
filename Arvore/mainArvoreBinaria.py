from arvoreBinaria import ArvoreBinaria

arv = ArvoreBinaria()
arv.criaRaiz(40)
arv.addEsq(32)
arv.addDir(27)
arv.descerEsquerda()
print('Cursor: ', arv.getCursor())
arv.addDir(16)
arv.descerDireita()
print('Cursor: ', arv.getCursor())
arv.addEsq(10)
arv.addDir(20)
arv.resetCursor()
arv.descerDireita()
print('Cursor: ', arv.getCursor())
arv.addDir(55)
arv.descerDireita()
print('Cursor: ', arv.getCursor())
arv.addEsq(8)

""" print('Busca:', arv.busca(578))

arv.preordem()
print()
arv.emordem()
print()
arv.posordem()
#print(arv.__dict__)
print()
print(arv.go(116))
arv.preordem()
print('Cursor: ', arv.getCursor())
print(arv.removeEsq())
arv.preordem() """

print(arv.go(8))



'================= Lista 10.1 ==================='

#Q2
arvore1 = ArvoreBinaria(1)

arvore1.addEsq(2)
arvore1.addDir(3)
arvore1.descerEsquerda()
arvore1.addDir(4)
arvore1.resetCursor()
arvore1.descerDireita()
arvore1.addEsq(5)
arvore1.addDir(6)
arvore1.emordem()

#Q3
print()
arvore1.preordem()
print()
print(arvore1.getLevel(5))

#print(arvore1.getCursor())

arvore1.libera(1)

arvore1.preordem()
