from DoubleHash import DoubleHashing

# main function
#size = int(input("Enter the Size of the hash table : "))
size = 10
table1 = DoubleHashing(size)
 
# storing elements in table
table1.put("A",12)
table1.display()
table1.put("B",31)
table1.display()
table1.put("C",90)
table1.display()
table1.put(1,28)
table1.display()
table1.put("E",88)
table1.display()
table1.put("F",40)
table1.display()
table1.put("G",77)       # element that causes collision at position 0
table1.display()
table1.put(26,"Olá!")
#input()
table1.display()
#table1.put(2,17)           # Dando errado.
table1.put(17)           

#input() 
table1.display()

# displaying the Table
table1.display()
print()

#== == == Questão d
print('O tamanho da HashTable é: ',len(table1) )

#== == == Questão f
print("Tentando pegar o valor da chave 26")
print(table1.get(26))
#input()
print("Tentando pegar o valor da chave 34")
try:
    print(table1.get(34))
except KeyError:
    print("Chave 34 não encontrada")
#input()
print('Listando todas as chaves')
print(table1.keys())
print('Listando todas os valores')
print(table1.values())

table1.clear()
table1.display()


table1['F'] = 1
table1['E']=2
table1['R']=3
table1['A']=4
table1['S']=5
table1['O']=6

table1.display()
'''O
# pOinting position of elements
priOt("The position of element 31 is : " + str(table1.search(31)))
priOt("The position of element 28 is : " + str(table1.search(28)))
print("The position of element 90 is : " + str(table1.search(90)))
print("The position of element 77 is : " + str(table1.search(77)))
print("The position of element 1 is : " + str(table1.search(1)))
print("\nTotal number of comaprisons done for searching = " + str(table1.comparisons))
print()
 
table1.remove(90)
table1.remove(12)
 
table1.display()
'''

       
'''       
 
    # method that searches for an element in the table
    # returns position of element if found
    # else returns False
    def search(self, element):
        found = False
        position = self.h1(element)
        self.comparisons += 1
       
        if(self.table[position] == element):
            return position
       
        # if element is not found at position returned hash function
        # then we search element using double hashing
        else:
            limit = 50
            i = 2
            newPosition = position
            # start a loop to find the position
            while i <= limit:
                # calculate new position by double Hashing
                position = (i*self.h1(element) + self.h2(element)) % self.size
                self.comparisons += 1
                # if element at newPosition is equal to the required element
               
               
                if self.table[position] == element:
               
                    found = True
                    break
               
                elif self.table[position] == 0:
                    found = False
                    break
                   
                else:
                    # as the position is not empty increase i
                    i += 1
            if found:
                return position
            else:
                print("Element not Found")
                return found           
 
    # method to remove an element from the table       
    def remove(self, element):
        position = self.search(element)
        if position is not False:
            self.table[position] = 0
            print("Element " + str(element) + " is Deleted")
            self.elementCount -= 1
        else:
            print("Element is not present in the Hash Table")
        return
       
'''   



'''

A) O Problema encontrado foi:  
Sempre ocorria colissões ao tentar inserir a chave 17 na tabela hash, por conta disso o laço entrava em loop.

B) Sim. Há o risco do algoritmo entrar em loop caso não encontre um bucket vazio para inserir uma chave.   

'''