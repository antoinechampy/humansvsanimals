def choisirNom()->str:
	nom=""
	test=""
	while test=="":
		nom=input("Veuillez saisir votre pseudo: ")
		test=nom.strip()
	nom= nom.capitalize()
	return nom