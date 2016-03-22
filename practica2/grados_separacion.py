
import shelve
import utilidades


d=shelve.open("movie_db.shelve")
actedWith={}
ActorList=[]
movies={}
actedIn=[]
i=1


def obtenerGrados(original,target,base,dos=0,seen=[]):
	i=i+1
	for actor in actedWith[base]:
		print "\t" + actor
		if target == actor:
			print original, "tiene ", i, "grados de separacion de", target
			return True
	for actor in actedWith[base]:
		if actor in seen: continue
		seen= seen+[actor]
		if obtenerGrados(original,target,actor,i,seen):
			return False
	return True
	
for l in f:
    l = l.strip()
    l = l.split("/")
    movies = {l[0] : l[1:]}
    for e in l[1:]:
        if e in actedWith:
            actedWith[e] = actedWith[e]+movies[l[0]]
        else:
            actedWith[e] = movies[l[0]]

original = raw_input("Nombre actor (Apellido, Nombre): ")
target = raw_input("Nombre actor (Apellido, Nombre): ")
obtenerGrados(original, target, original)


