from deroulementcreaperso import *
import menuclasse
import nom
from genstat import *
from laucher import *


def choixClasse()->str:
	classe=""
	tpRace= input("HUMAIN ou ANIMAL: ")
	choixRace=tpRace.upper()
	if choixRace=="HUMAIN" : classe=choixClasseHumain() 
	elif choixRace=="ANIMAL": classe=choixClasseAnimal()
	else: launch()
	return classe


def choixClasseHumain()->str:
	classe=""
	classeHumain=["Mage","Archer","Guerrier","Paladin","Assassin"]
	for i in range(len(classeHumain)):
		print(i+1,". ",classeHumain[i])
	tpClasse=input("Quelle classe choisissez vous ? : ")
	choixClasse=tpClasse.upper()
	if choixClasse=="MAGE": classe=classeHumain[0]
	elif choixClasse=="ARCHER":classe=classeHumain[1]
	elif choixClasse=="GUERRIER":classe=classeHumain[2]
	elif choixClasse=="PALADIN":classe=classeHumain[3]
	elif choixClasse=="ASSASSIN":classe=classeHumain[4]
	else:launch()
	return classe 

def choixClasseAnimal()->str:
	classe=""
	classeAnimal=["Ours","Sanglier","lievre","aigle","serpent"]
	for i in range(len(classeAnimal)):
		print(i+1,". ",classeAnimal[i])
	tpClasse=input("Quelle classe choisissez vous ? : ")
	choixClasse=tpClasse.upper()	
	if choixClasse=="OURS":classe=classeAnimal[0]
	elif choixClasse=="SANGLIER":classe=classeAnimal[1]
	elif choixClasse=="LIEVRE":classe=classeAnimal[2]
	elif choixClasse=="AIGLE":classe=classeAnimal[3]
	elif choixClasse=="SERPENT":classe=classeAnimal[4]
	else:launch()
	return classe

def creaPerso()->list:
	lst=[]
	nm= nom.choisirNom()
	lst.append(nm)
	cl=choixClasse()
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