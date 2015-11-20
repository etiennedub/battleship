import turtle
from interface import classInterface as interface

class classGame(interface):

    def __init__(self):
        super().__init__()
        self.phase = False
        self.ship = [2,3,3,4,5]
        self.firstTime = True
        self.BoardEnemy = [] #liste de l'enemie
        self.BoardYou = [] #votre liste
        liste = []
        firstTime = 0
        for x in range(10): liste.append(" ")
        for x in range(10):
            self.BoardYou.append(liste)
            self.BoardEnemy.append(liste)#Les deux liste ont 10 listes de 10 espaces (Ex.: liste[column][line])
                                        # " " est une espace vide (a l'eau), un chiffre (de 0 a 4) vaut un bateau
                                        #, un chiffre en string ("1") est un bateau touche et un "x" en string est un tir a l'eau
    def placeShip(self):
        if len(self.ship) >= 1:
            if self.firstTime == True:
                print("Placer le bateau de {} cases".format(self.ship[0]))
                self.firstTime = False
            self.shipX(self.ship[0])
        else:
            self.phase = False

    def shipX(self,x):
        if self.coord1 == None:
            turtle.Screen().onclick(self.setCoord1)
            return None
        if self.coord2 == None:
            turtle.Screen().onclick(self.setCoord2)
            return None
        if abs(self.coord2[0] - self.coord1[0]) == (x-1) or abs(self.coord2[1] - self.coord1[1]) == (x-1):#Si ligne est de la bonne dimension
            if self.coord1[0] == self.coord2[0]: #Vertical
                sens = "vertical"
            elif self.coord1[1] == self.coord2[1]: #Horizontal
                sens = "horizontal"
            else:
                print("Ligne non vertical ou horizontal")
                self.coord1,self.coord2 = None,None
                return None

            self.drawLine("gray",self.coord1,self.coord2)
            self.coord1,self.coord2 = None,None
            self.ship = self.ship[1:]#Enleve le bateau placer de la liste
            self.firstTime = True
        else:
            print("La dimension du bateau est de {} cases".format(x))
            self.coord1,self.coord2 = None,None
            return None
