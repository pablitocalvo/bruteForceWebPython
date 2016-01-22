import itertools

for password in list(itertools.permutations("ABCDE",3)):
	print password	#stampa l'array nella sua forma
	print "".join(password) #stampa l'array trasformato in stringa (visto su stackoverflow.com)


#	Semplice no?
#	basta solo combinare i due programmi .....
#   e qualche altro controllo ..

