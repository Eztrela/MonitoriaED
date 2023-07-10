from Operacoes import *

escolhas="""
(d) Digitar texto
(e) Exibir palavras do texto Ascendente/Descendente
(c) Exibir frequência de ocorrência das palavras
(b) Mostrar o nível de desbalanceamento da árvore
(s) Sair
"""
operacao=Operacoes()

while True:
    print(escolhas)
    escolha=input("=>")
    
    if escolha=='d':
        texto=input(' ')
        operacao.adicionarPalavra(texto)