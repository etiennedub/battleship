import turtle
import Tkinter
turtle.bgpic("grid.gif")


def main():
	turtle.Screen().onscreenclick(position)

def position(x,y): #Renvoie la case du board. Y et X position en px
    if abs(x) <= 25 or abs(x) >= 275 or y >= 100 or y <= -150:
        print("Out of range") # Determine si le joueur a cliquer sur une case
    elif x < 0:
        player = "enemy"
        collum = 13 + (int(x)-25)/25
        line = (abs(int(y)-100))/25+1
        print(player,collum,line)
    else:
        player = "you"
        collum = (int(x)-25)/25 + 1 #Position collone de 1 a 10
        line = (abs(int(y)-100))/25+1
        print(player,collum,line)

if __name__ == '__main__':
	main()
	turtle.mainloop()
