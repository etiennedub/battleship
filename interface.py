# -*- coding: utf-8 -*-

import turtle
from reseau import ClientReseau


class ClassInterface(ClientReseau):
    """
    Pour tout ce qui est relié a l'interface visuel

    :param pseudo: votre pseudonyme.
    :param adv: le pseudonyme de votre adversaire.
    :param x: largeur de la fenetre en px
    :param y:  hauteur de la fenêtre en px
    """
    def __init__(self,pseudo,adv,*,x=600,y=400):
        super().__init__(pseudo,adversaire = adv)
        turtle.Screen().onkey(self.pleindre,'p')
        turtle.Screen().onkey(self.rule,'j')
        self.coord1 = None
        self.coord2 = None
        turtle.ht() 
        turtle.penup() 
        turtle.bgpic("interface.gif") #charge le fond d'écran
        turtle.setup (width=x, height=y, startx=0, starty=0)
        turtle.Screen().onkey(self.help,'m')
        turtle.goto(-170,115)
        turtle.write(self.adv,align="center",font=("Arial",25, "normal"))
        turtle.goto(140,115)
        turtle.write(pseudo,align="center", font=("Arial",25, "normal"))

    def pleindre(self):
        """Appelé pour protester"""
        print('Vous pouvez protester')
        dire = input('Entrez votre message: ')
        try:
            self.protester(dire)
        except:
            print("Vous quitter la partie suite à votre protestation")
            turtle.bye()

    def help(self):
        """Affiche un menu d'aide"""
        print("-------Menu------'\nAppuiyer sur 'b' pour afficher le nombre de\
        bateau. \nAppuyer \sur 'p' pour protester. \nAppuyer sur 'j' pour afficher les regles du jeu")
    
    def rule(self):
        """"
        Affiche les règle du jeu
        """
        print("---Bataile Navale---\n"
        "Regle de jeu: \n1) Placer vos bateaux en " \
        "appuyant sur deux points sur votre carte " \
        "à l'aide de la souris, en respectant leur taille. \n2) " \
        "Utiliser la souris pour attaquer sur la carte de l'ennemie \n")
    def drawLine(self,color,coord1,coord2): 
        """
        dessine une ligne entre deux coordonné sur la grille

        :param color: La couleur de la ligne
        :param coord1: La première coordonné en tuple (i,j,"joueur")
        :param coord2: La deuxième coordonné en tuple (i,j,"joueur")
        """
        if coord1[2] == coord2[2] and coord2[2] == "you":
            turtle.goto(38+coord1[1]*25,87-25*coord1[0])
        elif coord1[2] == coord2[2] and coord2[2] == "enemy":
            turtle.goto(-262+(25*coord1[1]),87-25*coord1[0])
        else:
            print('wrong player')
            return 0
        turtle.pensize(20)
        turtle.pencolor(color)
        if coord1[1] == coord2[1]: #Vertical
            turtle.pendown()
            turtle.setheading(270)
            turtle.fd((coord2[0]-coord1[0])*25)
        elif coord1[0] == coord2[0]: #horizontal
            turtle.pendown()
            turtle.setheading(0)
            turtle.fd((coord2[1]-coord1[1])*25)
        else:
            print('Ligne non Hori ou Vert')
            return 0
        turtle.penup()
        return 1

    def setCoord1(self,x,y):
        """
        Sélectionner la première coordonnée.

        :param x: position sur l'axe des x en px
        :param y: position sur l'axe des y en px
        """
        turtle.Screen().onscreenclick(None)
        i,j,player = self.position(x,y)
        if j != player:
            self.coord1 = (i,j,player)
            return self
        else:
            print("Mauvaise coordone")
            turtle.Screen().onscreenclick(self.setCoord1)

    def setCoord2(self,x,y):
        """
        Sélectionner la deuxième coordonnée.

        :param x: position sur l'axe des x en px
        :param y: position sur l'axe des y en px
        """
        turtle.Screen().onscreenclick(None)
        i,j,player = self.position(x,y)
        if j != player:
            self.coord2 = (i,j,player)
        else:
            print("Mauvaise coordone")
            turtle.Screen().onscreenclick(self.setCoord2)

    def position(self,x,y):
        """
        Renvoie la position i,j de la grille du joueur sous la forme d'un tuple (i,j,"joueur")
        Ne renvoie rien si x,y sont à l'extérieur des grilles

        :param x: position x souris en px
        :param y: position y souris en px
        """
        if abs(x) <= 25 or abs(x) >= 275 or y >= 100 or y <= -150:
            return(0,0,0) #À l'extérieur des grilles
        elif x < 0:
            player = "enemy"
            j = 12 + int((int(x)-50)/25)
            i = int((abs(int(y)-100))/25)
            return(i,j,player)
        else:
            player = "you"
            j = int((int(x)-25)/25)  #Position collone de 0 a 9
            i = int((abs(int(y)-100))/25)
            return(i,j,player)

    def drawCircle(self,position,color):
        """
        Dessine un cercle de la couleur et à la position choisie

        :param position: position de la grille en (i,j,"joueur")
        :param color: couleur du cercle en str ou code hex RGB
        """ 
        i,j,player = position
        if player == "you":
            turtle.goto(38+j*25,88-25*i)
            turtle.dot(20,color)
        if player == "enemy":
            turtle.goto(-262+(25*j),88-25*i)
            turtle.dot(20,color)
