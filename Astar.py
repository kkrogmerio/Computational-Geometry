
class Nod:
	def __init__(self, info, h):
		self.info=info
		self.h=h
		
	def __str__ (self):
		return "("+self.info+", h="+str(self.h)+")"
	def __repr__ (self):
		return "("+self.info+", h="+str(self.h)+")"


class Arc:
	def __init__(self, capat, varf, cost):
		self.capat = capat
		self.varf = varf
		self.cost = cost
		
class Graf:
	def __init__(self):
		self.noduri = [
			Nod('a', float('inf')), Nod('b', 9), 
			Nod('c', 10), Nod('d', 11), 
			Nod('e', 6), Nod('f', 10),
			Nod('g', 6), Nod('h', 0),
			Nod('i', 4), Nod('j', 3)
		]
		self.arce = [
			Arc('a', 'b', 7),
			Arc('a', 'c', 4),
			Arc('a', 'd', 5),
			Arc('b', 'f', 6),
			Arc('b', 'g', 3),
			Arc('c', 'b', 2),
			Arc('c', 'e', 8),
			Arc('c', 'f', 5),
			Arc('d', 'h', 11), # de schimbat cu 21 sa se vada diferenta
			Arc('d', 'e', 5),
			Arc('e', 'f', 4),
			Arc('e', 'h', 6),
			Arc('f', 'h', 10),
			Arc('g', 'i', 2),
			Arc('g', 'j', 3)
		]
		self.nod_start = self.noduri[0]
		self.nod_scop = 'h'
				

	def scop(self, nod):
		return nod.info==self.nod_scop
		
	def cauta_nod_nume(self, info):
		for nod in self.noduri:
			if nod.info==info:
				return nod
		return None
		
	def calculeaza_succesori(self, nod):
		l_succesori=[]
		for arc in self.arce:
			if nod.info==arc.capat :
				l_succesori.append( (self.cauta_nod_nume(arc.varf), arc.cost) )
		return l_succesori
		
class NodCautare:
	def __init__(self, nod_graf ,succesori=[], parinte=None, g=0, f=None):
		self.nod_graf=nod_graf
		self.succesori = succesori
		self.parinte = parinte
		self.g=g
		if f is None :
			self.f=self.g+self.nod_graf.h
		else:
			self.f=f
		
	def drum_arbore(self):
		nod_c=self
		drum=[nod_c]
		while nod_c.parinte is not None :
			drum=[nod_c.parinte]+drum
			nod_c= nod_c.parinte
		return drum
		
	def contine_in_drum(self, nod):
		nod_c=self
		while nod_c.parinte is not None :
			if nod.info==nod_c.nod_graf.info:
				return True
			nod_c = nod_c.parinte
		return False		

	def __str__ (self):
		parinte=self.parinte if self.parinte is None else self.parinte.nod_graf.info
		return "("+str(self.nod_graf)+", parinte="+str(parinte)+", f="+str(self.f)+", g="+str(self.g)+")";



def debug_str_l_noduri(l):
	sir="["
	for x in l:
		sir+=str(x)+"  "
	sir+="]"
	return sir
def afis_succesori_cost(l):
	sir=""
	for (x, cost) in l:
		sir+="\nnod: "+str(x)+", cost arc:"+ str(cost)
	
	return sir
def in_lista(l,nod):
	for x in l:
		if x.nod_graf.info==nod.info:
			return x
	return None
def a_star(graf):
	rad_arbore=NodCautare(nod_graf=graf.nod_start);
	open=[rad_arbore]
	closed=[]
	while len(open) > 0 :
		nod_curent=open.pop(0)
		closed.append(nod_curent)
		if graf.scop(nod_curent.nod_graf):
			print("Nodul extras din open este nod scop")
			break
		l_succesori=graf.calculeaza_succesori(nod_curent.nod_graf)
		for (nod, cost) in l_succesori:
			if(not nod_curent.contine_in_drum(nod)):
				x=in_lista(closed,nod)
				g_succesor=nod_curent.g+cost
				f=g_succesor+nod.h
				if x is not None:
					if(f<nod_curent.f):
						x.parinte=nod_curent
						x.g=g_succesor
						x.f=f
						print(x)						
				else :
					x=in_lista(open,nod)
					if x is not None:						
						if(x.g>g_succesor):
							x.parinte=nod_curent
							x.g=g_succesor
							x.f=f
							print(x)
					else:	
						nod_cautare=NodCautare(nod_graf=nod, parinte=nod_curent,g=g_succesor);#se calculeaza f automat in constructor
						open.append(nod_cautare)
		open.sort(key=lambda x: (x.f, -x.g)) 
	if(len(open)==0):
		print("Lista open e vida, nu avem drum de la nodul start la nodul scop")
	else:
		print("Drum de cost minim: " + debug_str_l_noduri(nod_curent.drum_arbore()))
	

	
	
	
if __name__ == "__main__":
	problema=Graf()
	a_star(problema)
