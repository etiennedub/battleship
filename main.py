import turtle
from game import classGame as game #Importer la class de l'interface

def main():
    if i.phase == "PlaceShip":
        i.placeShip()
    elif i.phase == "Attack": # Nom fictif
        i.attack()
    elif i.phase == "Recevoir": # Nom fictif
      pass
    else:
        print('out')
    turtle.ontimer(main,500)

if __name__ == '__main__':
    pseudo = input('Entrer votre pseudo: ')
    i = game(pseudo)
    print('Votre adversaire est: '+ str(i.adv))
    i.phase = "PlaceShip"
    main()
    turtle.listen()
    turtle.mainloop()
