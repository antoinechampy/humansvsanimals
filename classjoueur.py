import abc
from random import *
import jeu

class Joueur(abc.ABC):

	def __init__(self,pseudo,classe,vie,mana,force,vitesse,defense,poison=0):
		self.pseudo=pseudo
		self.classe=classe
		self.vie=vie
		self.mana=mana
		self.force=force
		self.vitesse=vitesse
		self.defense=defense
		self.poison=poison
		

	def baisserVie(self,dgt):
		self.vie-=dgt
	def monterVie(self,heal):
		self.vie+=heal
	
	def baisserMana(self,m):
		self.mana-=m
	def monterMana(self,m):
		self.mana+=m

	def baisserForce(self,f):
		self.force-=f 
	def monterForce(self,f):
		self.force+=f 

	def baisserVitesse(self,v):
		self.vitesse-=v 
	def monterVitesse(self,v):
		self.vitesse+=v

	def baisserDefense(self,d):
		self.defense-=d
	def monterDefense(self,d):
		self.defense+=d

	def monterPoison(self,p):
		self.poison+=p

	def estMort(self,vie):
		if vie == 0: return True
		else : return False


	def esquive(self,jatt):
		testattaquant=randint(0,jatt.vitesse)
		testattaque=randint(0,self.vitesse)
		if testattaquant>=testattaque:return True
		else: return False

class Mage(Joueur):

	def fireball(self,jatt):
		self.baisserMana(15)
		if jatt.esquive(self):
			dgt=abso(self,jatt)
			jatt.baisserVie(dgt)

	def freeze():
		pass

	def heal():
		pass

	def storm():
		pass

class Archer(Joueur):

		def arrow(self,jatt):
			self.baisserMana(10)
			if jatt.esquive(self):
				dgt=jeu.abso(self,jatt,40)
				jatt.baisserVie(dgt)


		def triarrow(self,jatt):
			self.baisserMana(50)
			if jatt.esquive(self):
				lst=[40,40,40,80,80,120]
				dgt=jeu.abso(self,jatt,choice(lst))
				jatt.baisserVie(dgt)

		def poisonarrow(self,jatt):
			self.baisserMana(30)
			if jatt.esquive(self):
				jatt.monterPoison(2)
				dgt=jeu.abso(self,jatt,20)
				jatt.baisserVie(dgt)


		def headshot(self,jatt):
			self.baisserMana(50)
			if jatt.esquive(self):
				if randint(0,100)<=10:
					jatt.vie=0
				else:
					dgt=jeu.abso(self,jatt,40)
					jatt.baisserVie(dgt)

class Guerrier(Joueur):

		

		def epee():
			pass

		def heurt():
			pass

		def concentration():
			pass

		def epbo():
			pass

class Paladin(Joueur):



		def marteau():
			pass

		def heal():
			pass

		def purification():
			pass

		def lumsac():
			pass

class Assassin(Joueur):

		def dague():
			pass

		def vanish():
			pass

		def evis():
			pass

		def scream():
			pass


class Ours(Joueur):

	def attaque1():
		pass

class Sanglier(Joueur):

	def attaque1():
		pass

class Aigle(Joueur):

	def attaque1():
		pass

class Serpent(Joueur):

	def attaque1():
		pass

class Lievre(Joueur):

	def attaque1():
		pass