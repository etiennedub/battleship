import turtle
from game import classGame as game #Importer la class de l'interface

def main():
    if i.placeShip == 1:
        i.placeShips5()
    else:
        print('out')
    turtle.ontimer(main,500)

if __name__ == '__main__':
    i = game()
    i.placeShip = 1
    main()
    turtle.listen()
    turtle.mainloop()
