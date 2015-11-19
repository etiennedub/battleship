import turtle
from interface import classInterface as interface #Importer la class de l'interface
i = interface()

def main():

	i.drawLine("gray",(1,3,"you"),(1,8,"you"))
	turtle.fd(5)
	print("Bateau de 5 cases hori. ou vert.")
	turtle.Screen().onscreenclick(i.setCoord1)

if __name__ == '__main__':
   
    main()
    turtle.listen()
    turtle.mainloop()