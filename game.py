import turtle
from interface import classInterface as interface

class classGame(interface):

    def __init__(self,pseudo):
        super().__init__(pseudo)
        turtle.Screen().onkey(self.pleindre,'p')
        turtle.Screen().onkey(self.numNavire,'b')
        self.phase = False
        self.ship = [2,3,4,5]#original [2,3,3,4,5]
        self.shipYou = []
        self.firstTime = True
        self.BoardEnemy = [] #liste de l'enemie
        self.BoardYou = [] #votre liste
        firstTime = 0
        for x in range(len(self.ship)): self.shipYou.append([])
        for x in range(10):
            self.BoardYou.append(['.','.','.','.','.','.','.','.','.','.',])
            self.BoardEnemy.append(['.','.','.','.','.','.','.','.','.','.',])#Les deux liste ont 10 listes de 10 espaces (Ex.: liste[i][j])
                                        # " " est une espace vide (a l'eau), un chiffre (de 0 a 4) vaut un bateau
                                        #, un chiffre en string ("1") est un bateau touche et un "x" en string est un tir a l'eau
    def pleindre(self):
        dire = input('Vous pouvez protester \
              Entrez votre message: ')
        self.protester(dire)

    def numNavire(self):
        return 'Vous avez {} navire,' \
               'il vous en reste {}'.format(len(self.ship),len(self.shipYou))

    def attack(self):
        if self.firstTime == True:
          print('Clicker sur la case a attaquer')
          self.firstTime = False
        if self.coord1 == None:
            turtle.Screen().onclick(self.setCoord1)
            return None
        if self.coord1[2] != 'enemy':
          print('mauvais joueur!')
          self.coord1 = None
          return None
        self.firstTime = True
        coordEnemy = None
        self.attaquer(cellule = (self.coord1[0],self.coord1[1]))
        self.drawCircle(self.coord1,'gray')
        #self.phase = 'recevoir'
        while coordEnemy == None:#reste dans la boucle jusqua une position soit retourner par lautre joueur
            coordEnemy = self.attaquer() #return (i,j)
        toucheYou = self.checkShip(coordEnemy)
        if self.checkWin() == 'win':
          toucheYou = 'win'
        if toucheYou == 'coulé' or toucheYou == 'touché':
          color = 'red'
          self.rapporter(message = toucheYou)
        elif toucheYou == 'win':
          self.rapporter(message = 'win')
          self.phase = 'lose'
          return None
        else:
          self.rapporter(message = "A l'eau")
          color = 'blue'
        self.drawCircle((coordEnemy[0],coordEnemy[1],'you'),color)
        toucheEnemy = None
        while toucheEnemy == None:
          toucheEnemy = self.rapporter()
        print(toucheEnemy)
        if toucheEnemy in ('coulé','touché'):
          color = 'red'
        elif toucheEnemy == 'win':
          print('Vous avez gagne')
          self.phase = 'win'
          return None
        else:
          color = 'blue'
        self.drawCircle(self.coord1,color)
        self.coord1 = None

    def placeShip(self):
        if self.firstTime == True:
            print("Placer le bateau de {} cases".format(self.ship[0]))
            self.firstTime = False
            self.shipX(self.ship[0])
        self.shipX(self.ship[0])

    def shipX(self,x):
        if self.coord1 == None:
            turtle.Screen().onclick(self.setCoord1)
            return None
        if self.coord2 == None:
            turtle.Screen().onclick(self.setCoord2)
            return None
        if self.coord1[2] == 'enemy' or self.coord2[2] == 'enemy':
            print('Mauvais joueur')
            self.coord2,self.coord1 = None,None
            return None
        if abs(self.coord2[0] - self.coord1[0]) != (x-1) and abs(self.coord2[1] - self.coord1[1]) != (x-1):#Si ligne n'est pas de la bonne longueur
            self.coord2,self.coord1 = None,None
            print("La dimension du bateau est de {} cases".format(x))
            return None

# si aucun des if precedent n'est vrai, le code suivant s'execute
        backupBoard = self.BoardYou
        backupShip = self.shipYou

        if self.coord1[1] == self.coord2[1]: #Vertical
            for i in range(sorted((self.coord1[0],self.coord2[0]))[0],sorted((self.coord1[0],self.coord2[0]))[1]+1):# Sert a faire un range du plus petit nombre au plus grand
                if self.BoardYou[i][self.coord1[1]] == ".": #i = line, self.coord1[1] = j
                    (self.BoardYou[i][self.coord1[1]]) = len(self.ship)
                    self.shipYou[len(self.ship)-1].append((i,self.coord1[0]))
                    test = True
                else:
                    self.BoardYou = backupBoard
                    self.shipYou = backupShip
                    test = False
                    break

        elif self.coord1[0] == self.coord2[0]: #Horizontal
            for j in range(sorted((self.coord1[1],self.coord2[1]))[0],sorted((self.coord1[1],self.coord2[1]))[1]+1):
                if self.BoardYou[self.coord1[0]][j] == ".": # self.coord1[0] = line, j = column
                    self.BoardYou[self.coord1[0]][j] = len(self.ship)
                    self.shipYou[len(self.ship)-1].append((self.coord1[1],j))
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

    def checkShip(self,coord):
        coord = (coord[0],coord[1])#coord arrive en liste et je le tranforme en tuple
        for x in self.shipYou:
            if coord in x:
                x.remove(coord)
                if len(x)==0:
                    return 'coulé'
                else:
                    return 'touché'
        return None

    def checkWin(self):
        for x in self.shipYou:
            if len(x) != 0:
                return None
        return 'win'
