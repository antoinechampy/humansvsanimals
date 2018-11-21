from random import *
from attaques import *
import os
from classjoueur import *

def creaPerso()->Joueur:
	nm= choisirNom()
	classe=choixClasse()
	stat=genStat(classe)
	att=donnerAttaque(classe)
	j=define(classe,nm,stat)
	return j

def choisirNom()->str:
	nom=""
	test=""
	while test=="":
		nom=input("Veuillez saisir votre pseudo: ")
		test=nom.strip()
	nom= nom.capitalize()
	return nom

def genStat(classe:str)->list:
	lst = []
	listeClasse=["Mage","Archer","Guerrier","Paladin","Assassin","Ours","Sanglier","lievre","aigle","serpent"]
	if classe.upper()== listeClasse[0].upper():
		lst.append(50)
		lst.append(100)
		lst.append(randint(20,40))
		lst.append(randint(60,90))
		lst.append(randint(50,80))
	elif classe.upper()== listeClasse[1].upper():
		lst.append(50)
		lst.append(60)
		lst.append(randint(40,60))
		lst.append(randint(30,60))
		lst.append(randint(60,80))
	elif classe.upper()== listeClasse[2].upper():
		lst.append(100)
		lst.append(20)
		lst.append(randint(70,100))
		lst.append(randint(50,80))
		lst.append(randint(20,40))
	elif classe.upper()== listeClasse[3].upper():
		lst.append(75)
		lst.append(75)
		lst.append(randint(50,80))
		lst.append(randint(70,100))
		lst.append(randint(30,50))
	elif classe.upper()== listeClasse[4].upper():
		lst.append(50)
		lst.append(50)
		lst.append(randint(20,60))
		lst.append(randint(0,30))
		lst.append(randint(80,10))
	elif classe.upper()== listeClasse[5].upper():
		lst.append(75)
		lst.append(35)
		lst.append(randint(70,90))
		lst.append(randint(50,80))
		lst.append(randint(30,50))
	elif classe.upper()== listeClasse[6].upper():
		lst.append(65)
		lst.append(80)
		lst.append(randint(60,80))
		lst.append(randint(60,90))
		lst.append(randint(70,90))
	elif classe.upper()== listeClasse[7].upper():
		lst.append(40)
		lst.append(150)
		lst.append(randint(70,100))
		lst.append(randint(60,80))
		lst.append(randint(80,100))
	elif classe.upper()== listeClasse[8].upper():
		lst.append(50)
		lst.append(75)
		lst.append(randint(20,50))
		lst.append(randint(30,50))
		lst.append(randint(80,100))
	elif classe.upper()== listeClasse[9].upper():
		lst.append(40)
		lst.append(80)
		lst.append(randint(70,100))
		lst.append(randint(20,50))
		lst.append(randint(60,90))
	else: lst=[0,0,0,0]
	lst.append(0)
	return lst

def choixClasse()->str:
	classe=""
	choixRace=""
	while not(choixRace=="HUMAIN" or choixRace=="H" or choixRace=="ANIMAL" or choixRace=="A")  :
		tpRace= input("HUMAIN ou ANIMAL: ")
		choixRace=tpRace.upper()
	
	if choixRace=="HUMAIN" or choixRace=="H": classe=choixClasseHumain() 
	elif choixRace=="ANIMAL" or choixRace=="A": classe=choixClasseAnimal()
	
	return classe

def choixClasseHumain()->str:
	classe=""
	classeHumain=["Mage","Archer","Guerrier","Paladin","Assassin"]
	for i in range(len(classeHumain)):
		print(i+1,". ",classeHumain[i])
	choixClasse=""
	while not(choixClasse=="MAGE" or choixClasse=="1" or choixClasse=="ARCHER" or choixClasse=="2" or choixClasse=="GUERRIER" or choixClasse=="3" or choixClasse=="PALADIN" or choixClasse=="4" or choixClasse=="ASSASSIN" or choixClasse=="5"):
		tpClasse=input("Quelle classe choisissez vous ? : ")
		choixClasse=tpClasse.upper()
	if choixClasse=="MAGE" or choixClasse=="1": classe=classeHumain[0]
	elif choixClasse=="ARCHER" or choixClasse=="2":classe=classeHumain[1]
	elif choixClasse=="GUERRIER" or choixClasse=="3":classe=classeHumain[2]
	elif choixClasse=="PALADIN" or choixClasse=="4":classe=classeHumain[3]
	elif choixClasse=="ASSASSIN" or choixClasse=="5":classe=classeHumain[4]
	return classe 

def choixClasseAnimal()->str:
	classe=""
	classeAnimal=["Ours","Sanglier","lievre","aigle","serpent"]
	for i in range(len(classeAnimal)):
		print(i+1,". ",classeAnimal[i])
	choixClasse=""
	while not(choixClasse=="OURS" or choixClasse=="1" or choixClasse=="SANGLIER" or choixClasse=="2" or choixClasse=="LIEVRE" or choixClasse=="3" or choixClasse=="AIGLE" or choixClasse=="4" or choixClasse=="SERPENT" or choixClasse=="5" ):
		tpClasse=input("Quelle classe choisissez vous ? : ")
		choixClasse=tpClasse.upper()	
	if choixClasse=="OURS" or choixClasse=="1" :classe=classeAnimal[0]
	elif choixClasse=="SANGLIER" or choixClasse=="2":classe=classeAnimal[1]
	elif choixClasse=="LIEVRE" or choixClasse=="3" :classe=classeAnimal[2]
	elif choixClasse=="AIGLE" or choixClasse=="4" :classe=classeAnimal[3]
	elif choixClasse=="SERPENT" or choixClasse=="5" :classe=classeAnimal[4]
	return classe

def launch()->None:
	os.system('cls')
	j1=creaPerso()
	j2=creaPerso()
	return None

def donnerAttaque(classe):
	if classe.upper()=="MAGE":return ["fireball","freeze","heal","storm"]
	if classe.upper()=="ARCHER":return ["arrow","triarrow","poisonarrow","headshot"]
	if classe.upper()=="GUERRIER":return ["coupepee","heurtbouclier","concentration","bouclierepee"]
	if classe.upper()=="PALADIN": return ["coupmarteau","heal","purification","boost"]
	if classe.upper()=="ASSASSIN":return ["coupdague","vanish","evis","scream"]
	if classe.upper()=="OURS": return ["coupgriffe","eventre","dodo","miel"]
	if classe.upper()=="SANGLIER": return ["charge","peaudure","provoc","corne"]
	if classe.upper()=="AIGLE": return ["vue","pic","voltige","tornade"]
	if classe.upper()=="SERPENT": return ["ligoter","ramper","venin","morsure"]
	if classe.upper()=="LIEVRE": return ["charge","course","ecoute","rage"]

def abso(jatq,jattaque,dgts):
	dgt=int(dgts*(jattaque.force*0.01))
	abso=(randint(0,jattaque.defense)*0.01)
	abso=abso*dgt
	dgt=int(dgt-abso)
	return dgt

def define(classe,nm,stat):
	j=""
	if classe.upper()=="MAGE": j=Mage(nm,classe,stat[0],stat[1],stat[2],stat[3],stat[4])
	if classe.upper()=="ARCHER": j=Archer(nm,classe,stat[0],stat[1],stat[2],stat[3],stat[4])
	if classe.upper()=="GUERRIER": j=Guerrier(nm,classe,stat[0],stat[1],stat[2],stat[3],stat[4])
	if classe.upper()=="PALADIN": j=Paladin(nm,classe,stat[0],stat[1],stat[2],stat[3],stat[4])
	if classe.upper()=="ASSASSIN": j=Assassin(nm,classe,stat[0],stat[1],stat[2],stat[3],stat[4])
	if classe.upper()=="OURS": j=Ours(nm,classe,stat[0],stat[1],stat[2],stat[3],stat[4])
	if classe.upper()=="SANGLIER": j=Sanglier(nm,classe,stat[0],stat[1],stat[2],stat[3],stat[4])
	if classe.upper()=="AIGLE": j=Aigle(nm,classe,stat[0],stat[1],stat[2],stat[3],stat[4])
	if classe.upper()=="SERPENT": j=Serpent(nm,classe,stat[0],stat[1],stat[2],stat[3],stat[4])
	if classe.upper()=="LIEVRE": j=Lievre(nm,classe,stat[0],stat[1],stat[2],stat[3],stat[4])
	return j

def testatt():
	os.system("cls")
	j1=Mage("Matthieu","Admin",60,1000,60,60,80)
	j2=Archer("Matthieu","Admin",1000,1000,60,60,80)
	j1.afficherVie()