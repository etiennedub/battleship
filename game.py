import turtle
from interface import classInterface as interface

class classGame(interface):

  def __init__(self):
    super().__init__()
    self.placeShip = 0
    self.BoardEnemy = [] #liste de l'enemie
    self.BoardYou = [] #votre liste
    liste = []
    firstTime = 0
    for x in range(10): liste.append(" ")
    for x in range(10):
      self.BoardYou.append(liste)
      self.BoardEnemy.append(liste)

  def placeShips5(self):
    if self.coord1 == (0,0,'0'):
      turtle.Screen().onclick(self.setCoord1)
      print("lol")
      return None
    else:
      if self.coord2 == None:
        turtle.Screen().onclick(self.setCoord2)
      else:
        self.drawLine("gray",self.coord1,self.coord2)
        self.placeShip = 0

    return None

