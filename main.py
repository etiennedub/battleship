import turtle
from game import classGame as game #Importer la class de l'interface
import argparse



def main():

    if i.phase == "PlaceShip":
        i.placeShip()
    elif i.phase == "Attack": # Nom fictif
        i.attack()
    elif i.phase == "win":
        turtle.goto(0,0)
        turtle.pencolor('black')
        turtle.write('Vous avez gagné!',align="center",font=("Arial",70, "normal"))
        i.phase = "exit"
    elif i.phase == "lose":
        turtle.goto(0,0)
        turtle.pencolor('black')
        turtle.write('Vous avez perdu!',align="center",font=("Arial",70, "normal"))
        i.phase = "exit"
    elif i.phase == "exit":
        turtle.exitonclick()
        return None
    else:
        print('out')


    turtle.ontimer(main,500)

if __name__ == '__main__':
    #utilisation de argparse
    parser = argparse.ArgumentParser(description="Interface de jeu")
    parser.add_argument("nom",help = "votre nom"+ \
    " pour jouer", type=str)
    parser.add_argument("-a", "--adversaire", help="le pseudonyme de l'adversaire", type = str,default = None)
    parser.add_argument("-m", "--menu", help="Appuyer sur 'm' pour afficher le menu")
    parser.add_argument("-n", "--nom", help="Votre nom du jeu")
    parser.add_argument("-p", "--protester", help="Appuyer sur 'p' "
                        "pour entrer votre message de protestation")
    parser.add_argument("-b", "--bateaux", help="Appuyer sur b pour voir le nombre de bateau")
    parser.add_argument("-r","--regle", help="---Bataile Navale---\n"
                                             "Regle de jeu: \n1) Placer vos bateaux en " \
       "appuyant sur deux points sur votre carte" \
         "à l'aide de la souris, en respectant leur taille. \n2) " \
         "Utiliser la souris pour attaquer sur la carte de l'ennemie \n  BON JEU!")
    args = parser.parse_args()

    i = game(args.nom,args.adversaire)
    print('Votre adversaire est: '+ str(i.adv))
    i.phase = "PlaceShip"

    main()
    turtle.listen()
    turtle.mainloop()
