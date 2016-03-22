import shelve
import utilidades

def store_actor_movie_record(actor, date, title, role) :
    global actor_db

    movie_record = (title, date, role)    
    actor_db[actor] = actor_db.setdefault( actor, [] ) + [movie_record]
    print actor,"en", title, date, "actuo  como", role


def populate_database(imdb_file) :
    try :
		utilidades.process_file(imdb_file, store_actor_movie_record)
    except IndexError, e:
        print "error index" % ( e, imdb_file )



def peliculas_actor(actor):
	d=shelve.open("movie_db.shelve")
	peliculas=d[actor]
	d.close()
	listp=[]
	listp=peliculas
	# Solo las imprimo. Mas ordenado que en una lista
	for i in listp:
		print i
	#return listp
	
if __name__ == "__main__" :
	if utilidades.existeFichero('movie_db.shelve')==True:
		print ("La BD ya existe.. pasamos a buscar actor\n")
		actor=raw_input("Dime actor o actriz:(Apellido, Nombre) ")
		# Ejemplo de entrada : Pitt, Brad
		# Ejemplo de entrada: Apellido, Nombre
		peliculas_actor(actor)
		#print l
	else:
		print ("Creando BD de actores y actrices")
		actor_db = shelve.open("movie_db.shelve", flag="n")
		populate_database("actors.list")
		populate_database("actresses.list")
		actor_db.close()
