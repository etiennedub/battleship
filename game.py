import turtle
from interface import classInterface as interface

class classGame(interface):

    def __init__(self):
        super().__init__()
        self.phase = False
        self.ship = [2,3,3,4,5]
        self.shipYou = []
        self.firstTime = True
        self.BoardEnemy = [] #liste de l'enemie
        self.BoardYou = [] #votre liste
        firstTime = 0
        for x in range(len(self.ship)): self.shipYou.append([])# chaque liste va contenir des tuples qui sont la positions des bateaux en (column,line)
        for x in range(10):
            self.BoardYou.append(['.','.','.','.','.','.','.','.','.','.',])
            self.BoardEnemy.append(['.','.','.','.','.','.','.','.','.','.',])#Les deux liste ont 10 listes de 10 espaces (Ex.: liste[line][column])
                                        # " " est une espace vide (a l'eau), un chiffre (de 0 a 4) vaut un bateau
                                        #, un chiffre en string ("1") est un bateau touche et un "x" en string est un tir a l'eau
                                        # c'est la place qu'on utilise (line,column) tout les autre endroit cest (column,line) aka (x,y)
    def placeShip(self):
        if self.firstTime == True:
            print("Placer le bateau de {} cases".format(self.ship[0]))
            self.firstTime = False
        self.shipX(self.ship[0])

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
        backupShip = self.shipYou

        if self.coord1[0] == self.coord2[0]: #Vertical
            for i in range(sorted((self.coord1[1],self.coord2[1]))[0],sorted((self.coord1[1],self.coord2[1]))[1]+1):# Sert a faire un range du plus petit nombre au plus grand
                if self.BoardYou[i][self.coord1[0]] == ".": #i = line, self.coord1[0] = column
                    (self.BoardYou[i][self.coord1[0]]) = len(self.ship)
                    self.shipYou[len(self.ship)-1].append((self.coord1[0],i))
                    test = True
                else:
                    self.BoardYou = backupBoard
                    self.shipYou = backupShip
                    test = False
                    break

        elif self.coord1[1] == self.coord2[1]: #Horizontal
            for i in range(sorted((self.coord1[0],self.coord2[0]))[0],sorted((self.coord1[0],self.coord2[0]))[1]+1):
                if self.BoardYou[self.coord1[1]][i] == ".": # self.coord1[1][i] = line, i = column
                    self.BoardYou[self.coord1[1]][i] = len(self.ship)
                    self.shipYou[len(self.ship)-1].append((i,self.coord1[1]))
                    test = True
                else:
                    self.BoardYou = backupBoard
                    self.shipYou = backupShip
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

    def check_u(self, coord):#retourne "toucher", "couler", "� l'eau", "Game Over", "Grats"
      pass
