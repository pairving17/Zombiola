"""
***
Philip Irving
Jorge Alejandre
Rodrigo Lapenne
Curtis Lee

4/20/18
v1.2
***
"""

import random
island_Size = 50                    # island is a square
peps = int(input("How many Peps"))  # peps is Person Objs
zams = int(input("How many Zams"))  # zams is Zombie Objs
sick = int(input("How many Sick"))  # Sick is Infected Objs
personList = []                     # to contain peps objs
zambieList = []                     # to contain zams objs
sickList = []                       # to contain zams objs


class Person :
    #creates the X Y and ID 
    def __init__(self, ID, x, y):
        self.ID = ID
        self.x = x
        self.y = y
        
    
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Pep {}".format(self.ID)
    
    # returns X    
    def get_x(self):
        return self.x
    
    #returns Y
    def get_y(self):
        return self.y
    
    # returns indent
    def get_ID(self):
        return self.ID
    
    # the walk func that moves the X & Y forward, backward, sideways, nowhere
    def walk(self):
        """
        the walk func moves X & Y
        forward, backward, sideways, no where
        """
        # X Coonditionals
        if self.x == 0:
            """condit 4 if pep at 0"""
            self.x += random.randint(0,1)
            
        elif self.x < island_Size:
            """condit 4 if pep in the middle of island"""
            self.x += random.randint(-1,1)
            
        else:
            """condit 4 if pep at MAX island val"""
            self.x += random.randint(-1,0)
            
        # Y Coonditionals    
        if self.y == 0:
            """condit 4 if pep at 0"""
            self.y += random.randint(0,1)
            
        elif self.y < island_Size:
            """condit 4 if pep in the middle of island"""
            self.y += random.randint(-1,1)
            
        else:
            """condit 4 if pep at MAX island val"""
            self.y += random.randint(-1,0)
            
class Zombie(Person):
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Zam {}".format(self.ID)
     
class Infected(Person):
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Sick {}".format(self.ID)
    
ID_giver=0
# Function creates People objs
for i in range(peps):
    """loops thro person Objs in personList"""
    personList.append(Person(ID_giver,random.randint(0,50),random.randint(0,50)))
    ID_giver+=1
# Function creates Zombies objs    
for i in range(zams):
    """loops thro Zombie Objs in zambieList"""
    zambieList.append(Zombie(ID_giver,random.randint(0,50),random.randint(0,50)))
    ID_giver+=1

# Funtion creates Infected objs
for i in range(sick):
    """loops thro person Objs in personList"""
    sickList.append(Infected(ID_giver,random.randint(0,50),random.randint(0,50)))
    ID_giver+=1

# Main Function
Flag = True
time = 0
while Flag:
    print("time =", time)
    for p in personList:
        """loop 4 peps walking"""
        p.walk()
        for z2 in zambieList:
            if p.get_x() == z2.get_x() and p.get_y() == z2.get_y():
                sickList.append(Infected(p.get_ID(), p.get_x(), p.get_y()))                    
                print('PEP',p.get_ID(),"BIT BY ZAMBIE",z2.get_ID(),"!!!")
                for s2 in sickList:
                    if p.get_x() == s.get_x() and p.get_y() == s.get_y():
                        
                
            
    for s in sickList:
        """loop 4 peps walking"""
        s.walk()
        
    for z in zambieList:
        """loop 4 zams walking"""
        z.walk()

    if time == 100:
        Flag= False
    time+=1
