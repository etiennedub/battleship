import turtle
from game import classGame as game #Importer la class de l'interface

def main():
    if i.phase == "PlaceShip":
        i.placeShip()
    else:
        print('out')
    turtle.ontimer(main,500)

if __name__ == '__main__':
    i = game()
    i.phase = "PlaceShip"
    main()
    turtle.listen()
    turtle.mainloop()
