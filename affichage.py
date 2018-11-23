import os
import sys
from random import *
#for line in sys.stdin:
VieJ1 = randint(20,60)
VieJ2 = randint(20,60)
ManaJ1 = randint(20,60)
ManaJ2 = randint(20,60)
DefJ1 = randint(20,60)
DefJ2 = randint(20,60)
ForceJ1 = randint(20,60)
ForceJ2 = randint(20,60)
VitJ1 = randint(20,60)
VitJ2 = randint(20,60)

os.system("clear")

val=input()
while True:
	
	os.system("clear")
	if "a" == val:
		print("Joueur 1 :")
		print("Vie :  ", "💖"*VieJ1)
		print("Mana : ", "🌀"*ManaJ1)
		print("Def :  ", "🛡 "*DefJ1)
		print("Force :", "⚔️ "*ForceJ1)
		print("Speed :", "💨"*VitJ1)
		val=input()

	else:
		print("Joueur 2 :")
		print("Vie :  ", "💖"*VieJ2)
		print("Mana : ", "🌀"*ManaJ2)
		print("Def :  ", "🛡️ "*DefJ2)
		print("Force :", "⚔️ "*ForceJ2)
		print("Speed :", "💨"*VitJ2)
		val=input()