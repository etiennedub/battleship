import turtle

class classGame():
	def __init__(self):
		
		self.BoardEnemy = [] #liste de l'enemie
		self.BoardYou = [] #votre liste
		liste = []
		for x in range(10): liste.append(" ")
		for x in range(10):
			self.BoardYou.append(liste)
			self.BoardEnemy.append(liste)
	def placeShips5(self):
		#if abs(self.coord2[1]-self.coord1[1]) == 5 or abs(self.coord2[0]-self.coord1[0]) == 5:
		print("lol")
		print(self.coord1,self.coord2)
		self.drawLine("gray",self.coord1,self.coord2)
		print(lol)
		return None

