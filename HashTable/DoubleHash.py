 
class DoubleHashing:
    # initialize hash Table
    PRIME = 7
    def __init__(self, size:int=10):
        self.size = 10 if size < 10 else size
        # initialize table with all elements None
        self.table = list(None for i in range(self.size))
        self.usedSlots = 0
      
    # method that checks if the hash table is full or not
    def isFull(self)->bool:
        return self.usedSlots == self.size
      
    # method that returns the bucket for a given element
    # (modular hashing algorithm)
    def h1(self, key)->int:
        return hash(key) % self.size
       
    # method that returns the index by a second spread function  for a given element
    # The key is the argument have already transformed to an int value
    def __h2(self, key)->int:
        return self.__class__.PRIME - (key % self.__class__.PRIME)

    # method that computes rehashing for a givel element.
    # ih1: means "index computed by h1() method"
    # ih2: menas "index computed by h2() method"
    # i: means the i value of current iteration
    def __rh(self, ih1:int, ih2: int, i:int)->int:        
        return (ih1 + i * ih2) % self.size
           
   
    # method to insert a new pair of key/value using doublehashing technic
    def put(self, key):
        # testing if the hash table is full
        if( self.isFull() ):
            return

        # primary index (modular hashing)
        i1 = self.h1(key)

        # Testing if collision occurs 
        if (self.table[i1] != None): # Yes, we have a collision
            # get index2 from second hash 
            i2 = self.__h2(key)
           
            i = 1 # "i" is an attempt to insert a new key
            while(True): 
                # get rerash index
                irh = self.__rh( i1, i2,i)
  
                # if no collision occurs, store the key 
                if (self.table[irh] == None):
                    self.table[irh] = key
                    break 
                i += 1 
  
        else: #  No collision occurs 
            self.table[i1] = key
            irh = i1

        self.usedSlots += 1
        print(f'Key {key} stored at bucket {irh}')
         

    # method to display the hash table
    def display(self):
        print('  ',end='')
        for i in range(self.size):
            print(f' {i:2}    ',end='')
        print("\n[ ",end='')
        firstTime = True
        for i in range(self.size):
            if firstTime:
                firstTime = False
                if self.table[i] is None:
                    print(f'{self.table[i]} ',end= "")    
                else:
                    print(f'{self.table[i]:4d} ',end= "")    
            else:
                if self.table[i] is None:
                    print(f'| {self.table[i]} ',end= "") 
                else:  
                    print(f'| {self.table[i]:4d} ',end= "")  
            #print(f'{None if self.table[i] is None else self.table[i]:3d}',end= " | ")
        print("]")
        print("The number of element in the is: " + str(self.usedSlots),end='\n\n')
       
           
