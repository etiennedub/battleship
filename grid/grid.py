import turtle
import Tkinter


def main():
    turtle.Screen().onscreenclick(position)

def position(x,y): #Renvoie la case du board. Y et X position en px
    if abs(x) <= 25 or abs(x) >= 275 or y >= 100 or y <= -150:
        print("Out of range") # Determine si le joueur a cliquer sur une case
        turtle.done()
    elif x < 0:
        player = "enemy"
        collum = 13 + (int(x)-25)/25
        line = (abs(int(y)-100))/25+1
        return(player,collum,line)
    else:
        player = "you"
        collum = (int(x)-25)/25 + 1 #Position collone de 1 a 10
        line = (abs(int(y)-100))/25+1
        return(player,collum,line)

def drawCircle(collum,line,player): #entrer collonne et line pour dessiner un cercle au centre
    if player == "you":
        turtle.goto(12.5+line*25,100-25*collum)
        turtle.circle(12)
    if player == "enemy":
        turtle.goto(-287.5+(25*line),100-25*collum)
        turtle.circle(12)
if __name__ == '__main__':
        turtle.bgpic("grid.gif")
        turtle.setup (width=600, height=400, startx=0, starty=0)
	main()
	turtle.mainloop()
