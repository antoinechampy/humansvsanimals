class Joueur():

	def __init__(self,pseudo,classe,vie,mana,force,vitesse,defense):
		self.pseudo=pseudo
		self.classe=classe
		self.vie=vie
		self.mana=mana
		self.force=force
		self.vitesse=vitesse
		self.defense=defense
		

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
			dgt=abso(self,jatt,50)
			jatt.baisserVie(dgt)


	def freeze(self,jatt):
		self.baisserMana(20)
		if jatt.esquive(self):
			jatt.baisserVitesse(15)
			jatt.baisserForce(5)


	def heal(self):
		self.baisserMana(20)
		lst=[10,10,10,20,20,20,20,20,30]
		self.monterVie(choice(lst))
			

	def storm(self,jatt):
		self.baisserMana(50)
		if jatt.esquive(self):
			dgt=abso(self,jatt,75)
			jatt.baisserVie(dgt)


class Archer(Joueur):


		def arrow():
			pass

		def triarrow(self,jatt):
			self.baisserMana(30)
			if jatt.esquive(self):
				dgt=abso(self,jatt)
				jatt.baisserVie(dgt)

		def poisonarrow():
			pass

		def headshot():
			pass


class Guerrier(Joueur):


		def epee(self,jatt):
			if jatt.esquive(self):
				dgt=abso(self,jatt,30)
				jatt.baisserVie(dgt)

		def heurt(self,jatt):
			self.baisserMana(10)
			if jatt.esquive(self):
				dgt=abso(self,jatt,20)
				jatt.baisserVie(dgt)
				self.baisserDefense(3)

		def concentration(self):
			self.baisserMana(20)
			self.monterDefense(4)
			self.monterForce(4)
			self.monterVitesse(4)

		def epbo(self,jatt):#######le guerrier doit jouer en 1er quelque soit sa
			self.baisserMana(50)#######vitesse. Il ne doit en plus ne prendre aucun
			if jatt.esquive(self):#####dégat durant le même tour.
				dgt=abso(self,jatt,60)
				jatt.baisserVie(dgt)



class Paladin(Joueur):


		def marteau(self,jatt):
			if jatt.esquive(self):
				dgt=abso(self,jatt,30)
				jatt.baisserVie(dgt)

		def heal(self):
			self.baisserMana(20)
			lst=[10,20,20,20,20,20,30,30,30]
			self.monterVie(choice(lst))

		def purification(self):
			self.baisserMana(30)
			if jatt.esquive(self):
				self.monterForce(3)
				self.monterVitesse(3)
				self.monterDefense(3)
				jatt.baisserForce(3)
				jatt.baisserVitesse(3)
				jatt.baisserDefense(3)

		def lumsac():
			self.baisserMana(50)
			self.monterForce(6)
			self.monterVitesse(7)
			self.monterDefense(6)
			if jatt.esquive(self):
				dgt=abso(self,jatt,60)
				jatt.baisserVie(dgt)
				
			
class Assassin(Joueur):


		def dague(self,jatt):
			if jatt.esquive(self):
				dgt=abso(self,jatt,30)
				jatt.baisserVie(dgt)

		def vanish(self):
			#####a completer######
			pass

		def evis(self,jatt):
			self.baisserMana(40)
			if jatt.esquive(self):
				dgt=abso(self,jatt,60)
				jatt.baisserVie(dgt)

		def scream(self,jatt):
			self.baisserMana(50)
			###passe au premier tour, tape obligatoirement
			###invincible durant le tour
			


class Ours(Joueur):


class Sanglier(Joueur):


class Aigle(Joueur):


class Serpent(Joueur):


class Lievre(Joueur):