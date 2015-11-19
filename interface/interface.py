import turtle

class interface():

    def __init__(self,x=600,y=400): #sert a init linterface || x = largeur de la fenetre et y la hauteur
        turtle.ht() #hide the turtle
        turtle.penup() #stop drawing
        turtle.bgpic("interface.gif") #charge le background
        turtle.setup (width=x, height=y, startx=0, starty=0)#sert a juster la grandeur de la fenetre mais marche pas pour moi
        turtle.Screen().onscreenclick(self.click)
        turtle.Screen().onkey(self.help,'m')

    def click(self,x,y):
        self.drawCircle(x,y,'red')

    def help(self):
        print('-------Menu------')
        print('m pour afficher le menu')
        print('v pour....')

    def drawLine(self,player,color,coord1,coord2): #coordX accepte un tuple (column,line) et dessine une ligne horizontal ou vertical de coor1 a coord2
        if player == "you":
            turtle.goto(13+coord1[0]*25,112-25*coord1[1])
        elif player == "enemy":
            turtle.goto(-287+(25*coord1[0]),112-25*coord1[1])
        else:
            print('wrong player')
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
        turtle.penup()
    def position(self,x,y): #Renvoie la case du board Y et X position en px
        if abs(x) <= 25 or abs(x) >= 275 or y >= 100 or y <= -150:
            print("Out of range") # Determine si le joueur a cliquer sur une case
            turtle.done()
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

def main():
    i.drawLine("enemy","red",(1,4),(4,8))

if __name__ == '__main__':
    i = interface()
    main()
    turtle.listen()
    turtle.mainloop()

