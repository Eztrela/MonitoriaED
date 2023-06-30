class TabelaHash:
    def __init__(self, max):
        self.__table = [None for i in range(max)]
        self.__capacidade = max
        self.__ocupados = 0
    
    def __len__(self):
        return self.__ocupados

    def put(self, key:any, value:any):
        if self.__ocupados < self.__capacidade:
            slot = self.__hash(key)
            if (self.__table[slot] is None):
                self.__table[slot] = value                
            else:  # tratar colisao aqui
                nextSlot = self.__rh(slot)
                while(self.__table[nextSlot] is not None):
                    nextSlot = self.__rh(nextSlot)
                self.__table[nextSlot] = value
            self.__ocupados += 1

    def get(self, key:any)->any:
        pass

    def __hash(self, key:any):
        return hash(key) % self.__capacidade

    def __rh(self, slot):
        return (slot + 1) % self.__capacidade

    def __str__(self):
        s = ''
        for i in range(self.__capacidade):
            s += f'{self.__table[i]} '
        return s

# teste
ht = TabelaHash(10)
print(ht)
print(len(ht))
ht.put(205,"ABC")
ht.put(423,"KLM")
ht.put(500,"BTC")
ht.put(777,"UVW")
ht.put(401,"TYZ")
ht.put(402,"CNN")
print(ht)
ht.put(400,"GBR")
ht.put(600,"RTG")
ht.put(700,"ZZZ")
ht.put(900,"ASW")
ht.put(358,"ERR")


print(ht)
print(len(ht))


#sondagem Quadratica

12 31 90 28 77 26

[90,26,28,77,None,31,None,None,None,None,None,None,12]

#12
h(k) = 12 % 13 = 12

#31
h(31) = 31 % 13 = 5

#90
h(90) = 90 % 13 = 12
rh(90) = (12 + 1²) % 13 = 0

#28
h(28) = 28 % 13 = 2

#77
h(77) = 77 % 13 = 12
rh(77) = (12 + 1²) % 13 = 0
rh(77) = (12 + 2²) % 13 = 3

#26
h(26) = 26 % 13 = 0
rh(26) = (0 + 1²) % 13 = 1

espalhamento duplo
h1(k) = k % m
h2(k) = Num_primo - (k % Num_primo)
rh(k) = (h1(k) + i * h2(k)) % m
m: tamanho da tabela de disperção
k: chave
Num_primo: numero primo menor que m
i: numero de colisão

12 31 90
[90,None,None,None,None,31,None,None,None,None,None,None,12]

Num_primo = 7

#12
h1(12) = 12 % 13 = 12

#31
h1(31) = 31 % 31 = 5

#90
h1(90) = 90 % 13 = 12
h2(90) = 7 - (90 % 7) = 1
rh(90) = (12 + (1 * 1)) % 13 = 0