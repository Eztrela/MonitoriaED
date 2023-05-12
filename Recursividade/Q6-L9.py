def ispalindrome(string:str)-> bool:
    
    if len(string) <= 1: # O nosso limite
        return True
    
    if string[0].lower() != string[-1].lower(): # checa se as letras são diferentes
        return False
    
    return ispalindrome(string[1:-1]) # caso ainda haja letras iguais.



print("arara é palindromo: "+ str(ispalindrome('arara')))
print("onibus é palindromo: "+ str(ispalindrome('onibus')))
print("osso é palindromo: "+ str(ispalindrome('osso')))

'''
Ela recebe Uma palavra e retorna True caso ela possa ser lida de trás para frente.

Arara   True

Onibus  False 

0      -1
O   ==  S :   False

if string[0] != string[-1]: return False #caso a primeira letra for diferente da ultíma letra 

A nd a

0      -1
A   ==  A :  True  

A  nd   A

nd

ispalindrome("nd")  ispalindrome(string[1 : -1])

n == d : False

A N A

primeira chamada
0   -1
A == A : True

ispalindrome("n")  ispalindrome(string[1 : -1])

segunda chamada
0   -1
n == n : True

if len(string)==1: return True #caso seja ímpar

osso

o == o 

ispalindrome("ss")  ispalindrome(string[1 : -1])

s == s : true

ispalindrome("")  ispalindrome(string[1 : -1])

if len(string)== 0: return True # caso Par


if len(string)==1 ou if len(string)==0

if len(string) =< 1: return True # caso só exista uma letra, ou nenhuma letra, a string é palíndroma
'''
