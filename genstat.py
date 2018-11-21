from menuclasse import*
from random import *
from deroulementcreaperso import *

def genStat(classe:str)->list:
	lst = []
	listeClasse=["Mage","Archer","Guerrier","Paladin","Assassin","Ours","Sanglier","lievre","aigle","serpent"]
	if classe.upper()== listeClasse[0].upper():
		lst.append(10)
		lst.append(randint(2,4))
		lst.append(randint(5,8))
		lst.append(randint(6,9))
	elif classe.upper()== listeClasse[1].upper():
		lst.append(10)
		lst.append(randint(4,6))
		lst.append(randint(3,6))
		lst.append(randint(6,8))
	elif classe.upper()== listeClasse[2].upper():
		lst.append(20)
		lst.append(randint(7,10))
		lst.append(randint(5,8))
		lst.append(randint(2,4))
	elif classe.upper()== listeClasse[3].upper():
		lst.append(15)
		lst.append(randint(5,8))
		lst.append(randint(7,10))
		lst.append(randint(3,5))
	elif classe.upper()== listeClasse[4].upper():
		lst.append(10)
		lst.append(randint(2,6))
		lst.append(randint(0,3))
		lst.append(randint(8,10))
	elif classe.upper()== listeClasse[5].upper():
		lst.append(16)
		lst.append(randint(7,9))
		lst.append(randint(5,8))
		lst.append(randint(3,5))
	elif classe.upper()== listeClasse[6].upper():
		lst.append(14)
		lst.append(randint(6,8))
		lst.append(randint(6,9))
		lst.append(randint(7,9))
	elif classe.upper()== listeClasse[7].upper():
		lst.append(8)
		lst.append(randint(7,10))
		lst.append(randint(6,8))
		lst.append(randint(8,10))
	elif classe.upper()== listeClasse[8].upper():
		lst.append(10)
		lst.append(randint(2,5))
		lst.append(randint(3,5))
		lst.append(randint(8,10))
	elif classe.upper()== listeClasse[9].upper():
		lst.append(8)
		lst.append(randint(7,10))
		lst.append(randint(2,5))
		lst.append(randint(6,9))
	else: lst=[0,0,0,0]
	return lst

