import turtle
from interface import classInterface as interface

class classGame(interface):

    def __init__(self):
        super().__init__()
        self.phase = False
        self.ship = [2,3,3,4,5]
        self.firstTime = True
        self.BoardEnemy = [] #liste de l'enemie
        self.BoardYou = [['.','.','.','.','.','.','.','.','.','.',],['.','.','.','.','.','.','.','.','.','.',],['.','.','.','.','.','.','.','.','.','.',],['.','.','.','.','.','.','.','.','.','.',],['.','.','.','.','.','.','.','.','.','.',],['.','.','.','.','.','.','.','.','.','.',],['.','.','.','.','.','.','.','.','.','.',],['.','.','.','.','.','.','.','.','.','.',],['.','.','.','.','.','.','.','.','.','.',],['.','.','.','.','.','.','.','.','.','.',]] #votre liste
        liste = []
        firstTime = 0
        for x in range(10): liste.append(".")
        for x in range(10):
            #self.BoardYou.append(liste) #Ne fonctionne pas et surement la meme choses pour BoardEnemy !!!
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
            pass

    def shipX(self,x):
        if self.coord1 == None:
            turtle.Screen().onclick(self.setCoord1)
            return None
        if self.coord2 == None:
            turtle.Screen().onclick(self.setCoord2)
            return None
        if abs(self.coord2[0] - self.coord1[0]) != (x-1) and abs(self.coord2[1] - self.coord1[1]) != (x-1):#Si ligne n'est pas de la bonne longueur
            self.coord2,self.coord1 = None,None
            print("La dimension du bateau est de {} cases".format(x))
            return None

# si aucun des if precedent n'est vrai, le code suivant s'execute
        backupBoard = self.BoardYou

        if self.coord1[0] == self.coord2[0]: #Vertical
            for i in range(sorted((self.coord1[1],self.coord2[1]))[0],sorted((self.coord1[1],self.coord2[1]))[1]+1):# Sert a faire un range du plus petit nombre au plus grand
                if self.BoardYou[self.coord1[0]][i] == ".":
                    (self.BoardYou[self.coord1[0]])[i] = len(self.ship)
                    test = True
                else:
                    self.BoardYou = backupBoard
                    test = False
                    break

        elif self.coord1[1] == self.coord2[1]: #Horizontal
            for i in range(sorted((self.coord1[0],self.coord2[0]))[0],sorted((self.coord1[0],self.coord2[0]))[1]+1):
                if self.BoardYou[i][self.coord1[1]] == ".":
                    self.BoardYou[i][self.coord1[1]] = len(self.ship)
                    test = True
                else:
                    self.BoardYou = backupBoard
                    test = False
                    break
        else:
            print("Ligne non vertical ou horizontal")
            self.coord1,self.coord2 = None,None
            return None
        if test == True:
            self.drawLine("gray",self.coord1,self.coord2)
            self.coord1,self.coord2 = None,None
            self.ship = self.ship[1:]#Enleve le bateau placer de la liste
            if len(self.ship) == 0:
                self.phase = "Attack" #Prochaine phase
            self.firstTime = True
        else:
            print('case invalide ou occupe')
            self.firstTime = True
            self.coord1,self.coord2 = None,None
            return None

    def check_u(self, coord):#retourne "toucher", "couler", "à l'eau", "Game Over", "Grats"