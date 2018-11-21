from random import *

def heal(jattanquant):
	jattanquant.baisserMana(20)
	lst=[10,10,10,10,20,20,20,20,30]
	jattanquant.monterVie(choice(lst))

"""
Ancienne version

def speedRate(jattaque:list,jattanquant:list)->bool:
	test=False
	testattaquant=randint(0,jattanquant[5])
	testattaque=randint(0,jattaque[5])
	if testattaquant >= testattaque:test= True
	return test

def abso(jattaque:list,jattanquant:list,dgts:int)->int:
	dgt=int(dgts*(jattanquant[4]*0.01))
	abso=(randint(0,jattaque[6])*0.01)
	abso=abso*dgt
	dgt=int(dgt-abso)
	print(dgt)
	return dgt

def heal(jattanquant:list)->None:
	lst=[10,10,10,10,10,20,20,20,30]
	pv=choice(lst)
	jattanquant[2]+=pv
	return None

def freeze(jattaque:list,jattanquant:list)->None:
	jattanquant[3]-=30
	if speedRate(jattaque,jattanquant):
		lst=[1,10,10,10,10,20,20,20,30,30]
		low=choice(lst)
		jattaque[5]-=low
		print(jattaque[5])
	else: print("fail")
	return None

def fireBall(jattaque:list,jattanquant:list)->None:
	jattanquant[3]-=15
	if speedRate(jattaque,jattanquant):
		dgt=abso(jattaque,jattanquant,50)
		jattaque[2]-=dgt
		print(jattaque[2])
	else: print("fail")
	return None

def poisonArrow(jattaque:list,jattanquant:list)->None:
	jattanquant[3]-= 20
	if speedRate(jattaque,jattanquant):
		dgt=abso()
	return None
"""