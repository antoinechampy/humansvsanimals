import menuclasse
import nom
from genstat import *


def creaPerso()->list:
	lst=[]
	nm= nom.choisirNom()
	lst.append(nm)
	cl=menuclasse.choixClasse()
	lst.append(cl)
	stat=genStat(classe=cl)
	lst=lst+stat
	print("Pseudo: ",lst[0])
	print("Classe: ",lst[1])
	print("Points de vie: ",lst[2])
	print("Force: ",lst[3])
	print("Défence: ",lst[4])
	print("Vitesse: ",lst[5])
	return lst





