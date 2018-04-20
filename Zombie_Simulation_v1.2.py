"""
***
Philip Irving
Jorge Alejandre
Rodrigo Lapenne
Curtis Lee

4/18/18
v1.2
***
"""

import random
import numpy as np # can now be used as "np.- whatever function call"
import matplotlib.pyplot as plt # can now be used as "plt.- whatever function call"

island_Size = 50                    # island is a square
peps = int(input("How many Peps: "))  # peps is Person Objs
zams = int(input("How many Zams: "))  # zams is Zombie Objs
sick = int(input("How many Sick: "))  # Sick is Infected Objs
personList = []                     # to contain peps objs
zombieList = []                     # to contain zams objs
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
            
# Function for printing peps
for i in range(peps):
    """loops thro person Objs in personList"""
    personList.append(Person(i,0,0))
    
bFlag = True   #boolean flag
time = 0       # time var 
while bFlag:
    for p in personList:
        """loop 4 peps walking"""
        p.walk()
        
    print("t = {}, walks complete".format(time))
    time +=1
    
    if time == 100:
        bFlag = False 
print("")

for p in personList:
    print(p.__str__(), ", x =", p.get_x(), ", y =", p.get_y())

for p2 in personList:
    if peps[p2].get_x() == zams[p2].get_x() and peps[p2].get_y() == zams[p2].get_y():
        sickList.append(__init__(self.__str__(),self.get_x(),self.get_y()))
    
class Zombie(Person):
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Zam {}".format(self.ID)
     
# Function for printing Zombies    
for i in range(zams):
    """loops thro Zombie Objs in zombieList"""
    zombieList.append(Zombie(i,random.randint(0,50),random.randint(0,50)))
    
bFlag = True   # boolean flag
time = 0       # time var 
while bFlag:
    for z in zombieList:
        """loop 4 zams walking"""
        z.walk()
        
    print("t = {}, walks complete".format(time))
    time +=1
    
    if time == 100:
        bFlag = False 
print("")
for z in zombieList:
    print(z.__str__(), ", x =", z.get_x(), ", y =", z.get_y())

           
class Infected(Person):
    def __str__(self):
        """creates string repersentation of the obj"""
        return "Sick {}".format(self.ID)
    
    
# Funtion for printing Infected
for i in range(sick):
    """loops thro person Objs in personList"""
    sickList.append(Infected(i,0,0))
    
bFlag = True   #boolean flag
time = 0       # time var 

while bFlag:
    for s in sickList:
        """loop 4 peps walking"""
        s.walk()
        
    print("t = {}, walks complete".format(time))
    time +=1
    
    if time == 100:
        bFlag = False 

print("")
for s in sickList:
    print(s.__str__(), ", x =", s.get_x(), ", y =", s.get_y())
