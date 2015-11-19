import turtle
from game import classGame as game

class classInterface(game):

    def __init__(self,x=600,y=400): #sert a init linterface || x = largeur de la fenetre et y la hauteur
        super().__init__()
        self.coord1 = None
        self.coord2 = None
        turtle.ht() #hide the turtle
        turtle.penup() #stop drawing
        turtle.bgpic("interface.gif") #charge le background
        turtle.setup (width=x, height=y, startx=0, starty=0)#sert a juster la grandeur de la fenetre mais marche pas pour moi
        turtle.Screen().onkey(self.help,'m')

    def click(self,x,y):
        self.drawCircle(x,y,'red')

    def help(self):
        print('-------Menu------')
        print('m pour afficher le menu')
        print('v pour....')

    def drawLine(self,color,coord1,coord2): #coordX accepte un tuple (column,line,"player") et dessine une ligne horizontal ou vertical de coor1 a coord2
        if coord1[2] == coord2[2] and coord2[2] == "you":
            turtle.goto(13+coord1[0]*25,112-25*coord1[1])
        elif coord1[2] == coord2[2] and coord2[2] == "enemy":
            turtle.goto(-287+(25*coord1[0]),112-25*coord1[1])
        else:
            print('wrong player')
            return 0
        turtle.pensize(20)
        turtle.pencolor(color)
        if coord1[0] == coord2[0]: #Vertical
            turtle.pendown()
            turtle.setheading(270)
            turtle.fd((coord2[1]-coord1[1])*25)
        elif coord1[1] == coord2[1]: #horizontal
            turtle.pendown()
            turtle.setheading(0)
            turtle.fd((coord2[0]-coord1[0])*25)
        else:
            print('Ligne non Hori ou Vert')
            return 0
        turtle.penup()
        return 1
    def setCoord1(self,x,y): #set coord1 (colum,line,"player")
        turtle.Screen().onscreenclick(None)
        column,line,player = self.position(x,y)
        if column != player:
            self.coord1 == (column,line,player)
            turtle.Screen().onscreenclick(self.setCoord2)
        else:
            print("Mauvaise coordone")
            turtle.Screen().onscreenclick(self.setCoord1)
        
    def setCoord2(self,x,y):
        turtle.Screen().onscreenclick(None)
        column,line,player = self.position(x,y)
        if column != player:
            self.coord2 == (column,line,player)
            #self.setCoord = 1
            print(self.coord2,self.coord1)
            #self.drawLine("gray",self.coord1,self.coord2)
            self.placeShips5()
        else:
            print("Mauvaise coordone")
            turtle.Screen().onscreenclick(self.setCoord2)

    def position(self,x,y): #Renvoie la case du board Y et X position en px
        if abs(x) <= 25 or abs(x) >= 275 or y >= 100 or y <= -150:
            print("Out of range") # Determine si le joueur a cliquer sur une case
            return(0,0,0)
        elif x < 0:
            player = "enemy"
            column = 13 + (int(x)-25)/25
            line = (abs(int(y)-100))/25+1
            return(column,line,player)
        else:
            player = "you"
            column = (int(x)-25)/25 + 1 #Position collone de 1 a 10
            line = (abs(int(y)-100))/25+1
            return(column,line,player)

    def drawCircle(self,x,y,color): #entrer collonne et line pour dessiner un cercle au centre
        column,line,player = self.position(x,y)
        if player == "you":
            turtle.goto(13+column*25,113-25*line)
            turtle.dot(20,color)
        if player == "enemy":
            turtle.goto(-287+(25*column),113-25*line)
            turtle.dot(20,color)


