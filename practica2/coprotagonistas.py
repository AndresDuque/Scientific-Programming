import utilidades
import shelve


def coprotagonistas(actor1,actor2):
	"""Devuelve la interseccion de peliculas en las que 
	han estado juntos"""
	
	d=shelve.open("movie_db.shelve")
	peliculas1=d[actor1]
	peliculas2=d[actor2]
	p1=[]
	for i in range(len(peliculas1)):
		for j in range(len(peliculas2)):
			if peliculas1[i][0]==peliculas2[j][0]:
				p1.append(peliculas1[i][0])
				
	d.close()
	return p1
				
		


if __name__=='__main__':
	actor1='Pitt, Brad'
	actor2='Jolie, Angelina'
	l=coprotagonistas(actor1,actor2)
	print ("Fueron coprotagonistas en: ", l)
	
	
