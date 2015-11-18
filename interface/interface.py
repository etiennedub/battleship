import turtle

def main(): pass

def setup(): #sert a init linterface
    turtle.ht() #hide the turtle
    turtle.penup() #stop drawing
    turtle.bgpic("interface.gif") #charge le background
    turtle.setup (width=600, height=400, startx=0, starty=0)#sert a juster la grandeur de la fenetre mais marche pas pour moi
    turtle.Screen().onscreenclick(click)
    turtle.Screen().onkey(help,'m')

def click(x,y):
    drawCircle(x,y,'red')

def help():
    print('-------Menu------')
    print('m pour afficher le menu')
    print('v pour....')

def position(x,y): #Renvoie la case du board Y et X position en px
    if abs(x) <= 25 or abs(x) >= 275 or y >= 100 or y <= -150:
        print("Out of range") # Determine si le joueur a cliquer sur une case
        turtle.done()
    elif x < 0:
        player = "enemy"
        collum = 13 + (int(x)-25)/25
        line = (abs(int(y)-100))/25+1
        return(collum,line,player)
    else:
        player = "you"
        collum = (int(x)-25)/25 + 1 #Position collone de 1 a 10
        line = (abs(int(y)-100))/25+1
        return(collum,line,player)

def drawCircle(x,y,color): #entrer collonne et line pour dessiner un cercle au centre
    collum,line,player = position(x,y)
    if player == "you":
        turtle.goto(13+collum*25,113-25*line)
        turtle.dot(20,color)
    if player == "enemy":
        turtle.goto(-287+(25*collum),113-25*line)
        turtle.dot(20,color)
if __name__ == '__main__':
    setup()
    main()
    turtle.listen()
    turtle.mainloop()

