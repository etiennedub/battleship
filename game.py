#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle
from interface import ClassInterface


class ClassGame(ClassInterface):
    """Exécute toutes les focntions relier au jeu
    sans rien afficher directement

    :param pseudo: votre pseudonyme.
    :param adv: le pseudonyme de votre adversaire.
    """

    def __init__(self,pseudo,adv):
        super().__init__(pseudo,adv)
        self.phase = False
        self.ship = [2,3,3,4,5] #Liste de bateau à placer au début de la partie. int = longueur
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

    def attack(self):
        """
        Fonction appelé durant la phase d'attaque.
        Elle envoie la position d'attaque à l'adversaire
        et recoit celle de l'adversaire.
        """
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
        if self.BoardEnemy[self.coord1[0]][self.coord1[1]] == "X":
            print("Vous avez déjà attaqué cette case !")
            self.coord1 = None
            return None
        self.firstTime = True
        coordEnemy = None
        self.attaquer(cellule = (self.coord1[0],self.coord1[1]))
        self.drawCircle(self.coord1,'black')
        self.BoardEnemy[self.coord1[0]][self.coord1[1]] = "X"
        #self.phase = 'recevoir'
        while coordEnemy == None:#reste dans la boucle jusqua une position soit retourner par lautre joueur
            try:
                coordEnemy = self.attaquer() #return (i,j)
            except:
                print("L'adversaire à protester avec le message suivant: " + self.message)
                self.phase = "exit"
                return None
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
        if toucheEnemy in ('coulé','touché'):
            color = 'red'
            print(toucheEnemy)
        elif toucheEnemy == 'win':
            self.phase = 'win'
            return None
        else:
            print(toucheEnemy)
            color = 'blue'
        self.drawCircle(self.coord1,color)
        self.coord1 = None

    def placeShip(self):
        """ Fonction appelé durant la phase "placeShip"
        Fait un lien avec l'utilisateur et appel la fonction 
        shipX pour chaque bateau à placer
        """
        if self.firstTime == True:
            print("Placer le bateau de {} cases".format(self.ship[0]))
            self.firstTime = False
            self.shipX(self.ship[0])
        self.shipX(self.ship[0])

    def shipX(self,x):
        """
        place le bateau de la longeur indiqué en x.
        La fonction appel l'interface pour avoir 2 coordonée,
        puis elle teste les coordonée pour placer le bateau
        """
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
                    self.shipYou[len(self.ship)-1].append((i,self.coord1[1]))
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
                    self.shipYou[len(self.ship)-1].append((self.coord1[0],j))
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
            print('Cases invalides ou occupées')
            self.firstTime = True
            self.coord1,self.coord2 = None,None
            return None

    def checkShip(self,coord):
        """Recoie une liste de la coordoné d'attaque.
        Renvoie un str touché ou coulé
        """ 
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
        """"
        Vérifie si l'adversaire à gagné
        """
        for x in self.shipYou:
            if len(x) != 0:
                return None #Se passe rien
        return 'win' # L'adversaire à gagné
