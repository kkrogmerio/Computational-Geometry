import time
import copy
import Test2
#!!!!!!!!!!!De preferat maxim adancime 2/3 , de la 4 produce un timp de gandire destul de ridicat



class Joc:
    """
    Clasa care defineste jocul. Se va schimba de la un joc la altul.
    """
    NR_COLOANE = 8
    NR_LINII = 8
    NR_CONNECT = 4  # cu cate simboluri adiacente se castiga
    SIMBOLURI_JUC = ['A', 'N']  # ['G', 'R'] sau ['X', '0']
    JMIN = None  # 'R'
    JMAX = None  # 'G'
    GOL = '#'

    def __init__(self, tabla=None):
        self.matr = tabla or Test2.matrice()
        #print(Test.matrice())

    def linie(self, lista, jucator):
        simbol = 'A' if jucator == 'N' else 'N'
        if simbol in lista:
            return 0
        else:
            return 1

    def afis_daca_final(self):
        #A castigat jucatorul cu cele mai multe piese pe tabla
        nra=self.matr.count('A')
        nrn=self.matr.count('N')
        if(nra>nrn):
            print("Alb a castigat")
        if(nrn>nra):
            print("Negru a castigat")
        else:
            print("Remiza")
    def verific_final(self,linie,coloana):
        #In aceasta functie verific daca piesa de la coordonata linie,coloana este mutabila sau nu
        raspuns_valid=False
        okey=0
        if self.matr[linie*8+coloana]=='n':
                    if not (linie-1>=0 and coloana-1>=0):
                        no_action=1
                    else:
                        if self.matr[(linie-1)*8+coloana-1]=='#':
                                raspuns_valid=True
                                okey=1
                        elif self.matr[(linie-1)*8+coloana-1]=='a' or self.matr[(linie-1)*8+coloana-1]=='A':
                            if linie-2>=0 and coloana-2>=0:
                                raspuns_valid=True
                                okey=1
                                #return muta(linie-2,coloana-2,jucator)
                            else:
                                no_action=1
                    if not (linie-1>=0 and coloana+1<8):
                        no_action=1
                    else:
                        if self.matr[(linie-1)*8+coloana+1]=='#':
                            raspuns_valid=True
                            okey=1
                        elif self.matr[(linie-1)*8+coloana+1]=='a' or self.matr[(linie-1)*8+coloana+1]=='A':
                            if linie-2>=0 and coloana+2<8 and self.matr[(linie-2)*8+coloana+2]=='#':
                                raspuns_valid=True
                                okey=1
                                #return muta(linie-2,coloana+2,jucator)
                            else:
                                no_action=1
    
        if self.matr[linie*8+coloana]=='a':
                    if not (linie+1<8 and coloana-1>=0):
                        no_action=1
                    else:
                        if self.matr[(linie+1)*8+coloana-1]=='#':
                            raspuns_valid=True
                            okey=1
                        elif self.matr[(linie+1)*8+coloana-1]=='n' or self.matr[(linie+1)*8+coloana-1]=='N':
                            if linie+2<8 and coloana-2>=0 and self.matr[(linie+2)*8+coloana-2]=='#':
                                
                                raspuns_valid=True
                                okey=1
                                #return muta(linie+2,coloana-2,jucator)
                    if not (linie+1<8 and coloana+1<8):
                        no_action=1
                    else:
                        if self.matr[(linie+1)*8+coloana+1]=='#':
                            
                            raspuns_valid=True
                            okey=1
                        elif self.matr[(linie+1)*8+coloana+1]=='n' or self.matr[(linie+1)*8+coloana+1]=='N':
                            if linie+2<=7 and coloana+2<8 and self.matr[(linie+2)*8+coloana+2]=='#':
                                
                                raspuns_valid=True
                                okey=1
                            else:
                                no_action=1
        elif self.matr[linie*8+coloana]=='A':
                    if not (linie-1>=0 and coloana-1>=0):
                        no_action=1
                    else:
                        if self.matr[(linie-1)*8+coloana-1]=='#':
                             
                            raspuns_valid=True
                            okey=1
                        elif self.matr[(linie-1)*8+coloana-1]=='n' or self.matr[(linie-1)*8+coloana-1]=='N':
                            if linie-2>=0 and coloana-2>=0:
                                
                                okey=1
                                raspuns_valid=True
                                #return muta(linie-2,coloana-2,jucator)
                            else:
                                no_action=1
                    if not (linie-1>=0 and coloana+1<8):
                        no_action=1
                    else:
                        if self.matr[(linie-1)*8+coloana+1]=='#':
                            
                            raspuns_valid=True
                            okey=1
                        elif self.matr[(linie-1)*8+coloana+1]=='n' or self.matr[(linie-1)*8+coloana+1]=='N':
                            if linie-2>=0 and coloana+2<8 and self.matr[(linie-2)*8+coloana+2]=='#':
                                
                                raspuns_valid=True
                                okey=1
                                #return muta(linie-2,coloana+2,jucator)
                            else:
                                no_action=1
                    if not (linie+1<8 and coloana-1>=0):
                        no_action=1
                    else:
                        if self.matr[(linie+1)*8+coloana-1]=='#':
                            
                            raspuns_valid=True
                            okey=1
                        elif self.matr[(linie+1)*8+coloana-1]=='n' or self.matr[(linie+1)*8+coloana-1]=='N':
                            if linie+2<8 and coloana-2>=0 and self.matr[(linie+2)*8+coloana-2]=='#':
                               
                                raspuns_valid=True
                                okey=1
                                #return muta(linie+2,coloana-2,jucator)
                            else:
                                no_action=1
                    if not (linie+1<8 and coloana+1<8):
                        no_action=1
                    else:
                        if self.matr[(linie+1)*8+coloana+1]=='#':
                            
                            raspuns_valid=True
                            okey=1
                        elif self.matr[(linie+1)*8+coloana+1]=='n' or self.matr[(linie+1)*8+coloana+1]=='N':
                            if linie+2<=7 and coloana+2<8 and self.matr[(linie+2)*8+coloana+2]=='#':
                               
                                raspuns_valid=True
                                okey=1
                                #return muta(linie+2,coloana+2,jucator)
                            else:
                                no_action=1
        elif self.matr[linie*8+coloana]=='N':
                    if not (linie-1>=0 and coloana-1>=0):
                        no_action=1
                    else:
                        if self.matr[(linie-1)*8+coloana-1]=='#':
                            
                            raspuns_valid=True
                            okey=1
                        elif self.matr[(linie-1)*8+coloana-1]=='a' or self.matr[(linie-1)*8+coloana-1]=='A':
                            if linie-2>=0 and coloana-2>=0:
                                
                                okey=1
                                raspuns_valid=True
                            else:
                                no_action=1
                    if not (linie-1>=0 and coloana+1<8):
                        no_action=1
                    else:
                        if self.matr[(linie-1)*8+coloana+1]=='#':
                           
                            raspuns_valid=True
                            okey=1
                        elif self.matr[(linie-1)*8+coloana+1]=='a' or self.matr[(linie-1)*8+coloana+1]=='A':
                            if linie-2>=0 and coloana+2<8 and self.matr[(linie-2)*8+coloana+2]=='#':
                                
                                raspuns_valid=True
                                okey=1
                            else:
                                no_action=1
                    if not (linie+1<8 and coloana-1>=0):
                        no_action=1
                    else:
                        if self.matr[(linie+1)*8+coloana-1]=='#':
                            
                            raspuns_valid=True
                            okey=1
                        elif self.matr[(linie+1)*8+coloana-1]=='a' or self.matr[(linie+1)*8+coloana-1]=='A':
                            if linie+2<8 and coloana-2>=0 and self.matr[(linie+2)*8+coloana-2]=='#':
                                
                                raspuns_valid=True
                                okey=1
                            else:
                                no_action=1
                    if not (linie+1<8 and coloana+1<8):
                        no_action=1
                    else:
                        if self.matr[(linie+1)*8+coloana+1]=='#':
                            
                            raspuns_valid=True
                            okey=1
                        elif self.matr[(linie+1)*8+coloana+1]=='a' or self.matr[(linie+1)*8+coloana+1]=='A':
                            if linie+2<=7 and coloana+2<8 and self.matr[(linie+2)*8+coloana+2]=='#':
                                
                                raspuns_valid=True
                                okey=1
                            else:
                                no_action=1
        return raspuns_valid
    def final(self,jucator):
        #Verific daca mai e posibila cel putin o mutare , pentru jucatorul curent
        for i in range(self.NR_LINII):
            for j in range(self.NR_COLOANE):
                if self.matr[i*self.NR_COLOANE+j]==jucator.lower() or self.matr[i*self.NR_COLOANE+j]==jucator.upper():
                    #Aici verific toate posibilitatile unei piese ce apartine de jucator pentru a o muta
                    #Daca cel putin una e mutabila , jucatorul mai poate muta , deci n-a pierdut
                    if self.verific_final(i,j)==True:
                        return 0
        return 1
    l_mutari=[]
    def mutari(self,linie,coloana,jucator,matrice):
        #Aici calculatorul calculeaza toate posibilitatile de mutare(l_mutari l-am scos inafara functiei)
        #Pentru a updata si atunci cand piesul are multiple posibilitati de mutare
        #in jucator se pasteeaza jucatorul curent iar matrice ->matricea curenta pentru o anumita mutare
        raspuns_valid=False
        aux=copy.deepcopy(matrice)
        if matrice[linie*8+coloana]=='n':
                    if not (linie-1>=0 and coloana-1>=0):
                        no_action=1
                    else:
                        if matrice[(linie-1)*8+coloana-1]=='#':
                            aux[linie*8+coloana]='#'
                            if linie-1>0:
                                aux[(linie-1)*8+coloana-1]='n'
                            else:
                                aux[(linie-1)*8+coloana-1]='N' 
                            #Se preiau toate mutarile posibile
                            self.l_mutari.append(Joc(aux))
                        elif matrice[(linie-1)*8+coloana-1]=='a' or self.matr[(linie-1)*8+coloana-1]=='A':
                            if linie-2>=0 and coloana-2>=0:
                                aux[(linie-2)*8+coloana-2]='n'
                                if linie-2==0:
                                    aux[(linie-2)*8+coloana-2]='N'
                                aux[linie*8+coloana]='#'
                                aux[(linie-1)*8+coloana-1]='#'
                                self.l_mutari.append(Joc(aux))
                                #Pentru mutarile multiple , se iau toate cazurile
                                #Parcurg recursiv la mutarile jumps pana nu mai pot efectua jump-uri
                                #Si salvez fiecare configuratie in parte
                                self.mutari(linie-2,coloana-2,jucator,aux)
                            else:
                                no_action=1
                    aux=copy.deepcopy(matrice)
                    if not (linie-1>=0 and coloana+1<8):
                        no_action=1
                    else:
                        if matrice[(linie-1)*8+coloana+1]=='#':
                            aux[linie*8+coloana]='#'
                            if linie-1>0:
                                aux[(linie-1)*8+coloana+1]='n'
                            else:
                                aux[(linie-1)*8+coloana+1]='N' 
                            self.l_mutari.append(Joc(aux))
                        elif matrice[(linie-1)*8+coloana+1]=='a' or self.matr[(linie-1)*8+coloana+1]=='A':
                            if linie-2>=0 and coloana+2<8 and self.matr[(linie-2)*8+coloana+2]=='#':
                                aux[(linie-2)*8+coloana+2]='n'
                                if linie-2==0:
                                    aux[(linie-2)*8+coloana+2]='N'
                                aux[linie*8+coloana]='#'
                                aux[(linie-1)*8+coloana+1]='#'
                                self.l_mutari.append(Joc(aux))
                                self.mutari(linie-2,coloana+2,jucator,aux)
                            else:
                                no_action=1
    
        if matrice[linie*8+coloana]=='a':
                    if not (linie+1<8 and coloana-1>=0):
                        no_action=1
                    else:
                        if matrice[(linie+1)*8+coloana-1]=='#':
                            aux[linie*8+coloana]='#'
                            if linie+1<7:
                                aux[(linie+1)*8+coloana-1]='a'
                            else:
                                aux[(linie+1)*8+coloana-1]='A' 
                            self.l_mutari.append(Joc(aux))
                        elif matrice[(linie+1)*8+coloana-1]=='n' or self.matr[(linie+1)*8+coloana-1]=='N':
                            if linie+2<8 and coloana-2>=0 and self.matr[(linie+2)*8+coloana-2]=='#':
                                aux[(linie+2)*8+coloana-2]='a'
                                if linie+2==7:
                                    aux[(linie+2)*8+coloana-2]='A'
                                aux[linie*8+coloana]='#'
                                aux[(linie+1)*8+coloana-1]='#'
                                self.l_mutari.append(Joc(aux))
                                self.mutari(linie+2,coloana-2,jucator,aux)
                    aux=copy.deepcopy(matrice)
                    if not (linie+1<8 and coloana+1<8):
                        no_action=1
                    else:
                        if matrice[(linie+1)*8+coloana+1]=='#':
                            aux[linie*8+coloana]='#'
                            if linie+1<7:
                                aux[(linie+1)*8+coloana+1]='a'
                            else:
                                aux[(linie+1)*8+coloana+1]='A' 
                            self.l_mutari.append(Joc(aux))
                        elif matrice[(linie+1)*8+coloana+1]=='n' or self.matr[(linie+1)*8+coloana+1]=='N':
                            if linie+2<=7 and coloana+2<8 and self.matr[(linie+2)*8+coloana+2]=='#':
                                aux[(linie+2)*8+coloana+2]='a'
                                if linie+2==7:
                                    aux[(linie+2)*8+coloana+2]='A'
                                aux[linie*8+coloana]='#'
                                aux[(linie+1)*8+coloana+1]='#'
                                self.l_mutari.append(Joc(aux))
                                self.mutari(linie+2,coloana+2,jucator,aux)
                            else:
                                no_action=1
        elif matrice[linie*8+coloana]=='A':
                    if not (linie-1>=0 and coloana-1>=0):
                        no_action=1
                    else:
                        if matrice[(linie-1)*8+coloana-1]=='#':
                            aux[linie*8+coloana]='#'
                            aux[(linie-1)*8+coloana-1]='A' 
                            self.l_mutari.append(Joc(aux))
                        elif matrice[(linie-1)*8+coloana-1]=='n' or self.matr[(linie-1)*8+coloana-1]=='N':
                            if linie-2>=0 and coloana-2>=0:
                                aux[(linie-2)*8+coloana-2]='A'
                                aux[linie*8+coloana]='#'
                                aux[(linie-1)*8+coloana-1]='#'
                                okey=1
                                raspuns_valid=True
                                self.mutari(linie-2,coloana-2,jucator,aux)
                            else:
                                no_action=1
                    aux=copy.deepcopy(matrice)
                    if not (linie-1>=0 and coloana+1<8):
                        no_action=1
                    else:
                        if matrice[(linie-1)*8+coloana+1]=='#':
                            aux[(linie)*8+coloana]='#'
                            aux[(linie-1)*8+coloana+1]='A' 
                            self.l_mutari.append(Joc(aux))
                        elif matrice[(linie-1)*8+coloana+1]=='n' or self.matr[(linie-1)*8+coloana+1]=='N':
                            if linie-2>=0 and coloana+2<8 and self.matr[(linie-2)*8+coloana+2]=='#':
                                aux[(linie-2)*8+coloana+2]='A'
                                aux[linie*8+coloana]='#'
                                aux[(linie-1)*8+coloana+1]='#'
                                self.l_mutari.append(Joc(aux))
                                self.mutari(linie-2,coloana+2,jucator,matrice)
                            else:
                                no_action=1
                    aux=copy.deepcopy(matrice)
                    if not (linie+1<8 and coloana-1>=0):
                        no_action=1
                    else:
                        if matrice[(linie+1)*8+coloana-1]=='#':
                            aux[linie*8+coloana]='#'
                            aux[(linie+1)*8+coloana-1]='A' 
                            self.l_mutari.append(Joc(aux))
                        elif matrice[(linie+1)*8+coloana-1]=='n' or self.matr[(linie+1)*8+coloana-1]=='N':
                            if linie+2<8 and coloana-2>=0 and self.matr[(linie+2)*8+coloana-2]=='#':
                                aux[(linie+2)*8+coloana-2]='A'
                                aux[linie*8+coloana]='#'
                                aux[(linie+1)*8+coloana-1]='#'
                                self.l_mutari.append(Joc(aux))
                                self.mutari(linie+2,coloana-2,jucator,aux)
                            else:
                                no_action=1
                    aux=copy.deepcopy(matrice)
                    if not (linie+1<8 and coloana+1<8):
                        no_action=1
                    else:
                        if matrice[(linie+1)*8+coloana+1]=='#':
                            aux[linie*8+coloana]='#'
                            aux[(linie+1)*8+coloana+1]='A' 
                            self.l_mutari.append(Joc(aux))
                        elif matrice[(linie+1)*8+coloana+1]=='n' or self.matr[(linie+1)*8+coloana+1]=='N':
                            if linie+2<=7 and coloana+2<8 and self.matr[(linie+2)*8+coloana+2]=='#':
                                aux[(linie+2)*8+coloana+2]='A'
                                aux[linie*8+coloana]='#'
                                aux[(linie+1)*8+coloana+1]='#'
                                self.l_mutari.append(Joc(aux))
                                self.mutari(linie+2,coloana+2,jucator,aux)
                            else:
                                no_action=1
        elif matrice[linie*8+coloana]=='N':
                    if not (linie-1>=0 and coloana-1>=0):
                        no_action=1
                    else:
                        if matrice[(linie-1)*8+coloana-1]=='#':
                            aux[linie*8+coloana]='#'
                            aux[(linie-1)*8+coloana-1]='N' 
                            self.l_mutari.append(Joc(aux))
                        elif matrice[(linie-1)*8+coloana-1]=='a' or self.matr[(linie-1)*8+coloana-1]=='A':
                            if linie-2>=0 and coloana-2>=0:
                                aux[(linie-2)*8+coloana-2]='N'
                                aux[linie*8+coloana]='#'
                                aux[(linie-1)*8+coloana-1]='#'
                                okey=1
                                raspuns_valid=True
                                self.mutari(linie-2,coloana-2,jucator,aux)
                            else:
                                no_action=1
                    aux=copy.deepcopy(matrice)
                    if not (linie-1>=0 and coloana+1<8):
                        no_action=1
                    else:
                        if matrice[(linie-1)*8+coloana+1]=='#':
                            aux[(linie-1)*8+coloana+1]='N' 
                            aux[(linie)*8+coloana]='#'
                            self.l_mutari.append(Joc(aux))
                        elif matrice[(linie-1)*8+coloana+1]=='a' or self.matr[(linie-1)*8+coloana+1]=='A':
                            if linie-2>=0 and coloana+2<8 and self.matr[(linie-2)*8+coloana+2]=='#':
                                aux[(linie-2)*8+coloana+2]='N'
                                aux[linie*8+coloana]='#'
                                aux[(linie-1)*8+coloana+1]='#'
                                self.l_mutari.append(Joc(aux))
                                self.mutari(linie-2,coloana+2,jucator,aux)
                            else:
                                no_action=1
                    
                    if not (linie+1<8 and coloana-1>=0):
                        no_action=1
                    else:
                        if matrice[(linie+1)*8+coloana-1]=='#':
                            aux[linie*8+coloana]='#'
                            aux[(linie+1)*8+coloana-1]='N' 
                            self.l_mutari.append(Joc(aux))
                        elif matrice[(linie+1)*8+coloana-1]=='a' or self.matr[(linie+1)*8+coloana-1]=='A':
                            if linie+2<8 and coloana-2>=0 and self.matr[(linie+2)*8+coloana-2]=='#':
                                aux[(linie+2)*8+coloana-2]='N'
                                aux[linie*8+coloana]='#'
                                aux[(linie+1)*8+coloana-1]='#'
                                self.l_mutari.append(Joc(aux))
                                self.mutari(linie+2,coloana-2,jucator,aux)
                            else:
                                no_action=1
                    if not (linie+1<8 and coloana+1<8):
                        no_action=1
                    else:
                        if matrice[(linie+1)*8+coloana+1]=='#':
                            aux[linie*8+coloana]='#'
                            aux[(linie+1)*8+coloana+1]='N' 
                            self.l_mutari.append(Joc(aux))
                        elif matrice[(linie+1)*8+coloana+1]=='a' or self.matr[(linie+1)*8+coloana+1]=='A':
                            if linie+2<=7 and coloana+2<8 and self.matr[(linie+2)*8+coloana+2]=='#':
                                aux[(linie+2)*8+coloana+2]='N'
                                aux[linie*8+coloana]='#'
                                aux[(linie+1)*8+coloana+1]='#'
                                self.l_mutari.append(Joc(aux))
                                self.mutari(linie+2,coloana+2,jucator,aux)
                            else:
                                no_action=1





    def fct_euristica(self):

        
        return self.matr.count(self.JMAX) - self.matr.count(self.JMIN)

    def estimeaza_scor(self, jucator,adancime):
        #Daca s-a terminat jocul pentru minim , ins ca e cel mai bun scor(max a castigat) , altfel viceversa
        t_final = self.final(jucator)
        if t_final == 1 and Joc.JMIN==jucator:
            return (999+adancime)
        elif t_final == 1 and Joc.JMAX==jucator:
            return (-999-adancime)
        elif t_final == 'remiza':
            return 0
        else:
            return self.fct_euristica()

    def __str__(self):
        sir = '  '
        for nr_col in range(self.NR_COLOANE):
            sir += str(nr_col) + ' '
        sir += '\n'
        #print(self.matr)
        for lin in range(self.NR_LINII):
            k = lin * self.NR_COLOANE
            sir += (str(lin)+" "+" ".join([str(x)for x in self.matr[k: k+self.NR_COLOANE]])+"\n")
        return sir


class Stare:
    """
    Clasa folosita de algoritmii minimax si alpha-beta
    Are ca proprietate tabla de joc
    Functioneaza cu conditia ca in cadrul clasei Joc sa fie definiti JMIN si JMAX (cei doi jucatori posibili)
    De asemenea cere ca in clasa Joc sa fie definita si o metoda numita mutari() care ofera lista cu
    configuratiile posibile in urma mutarii unui jucator
    """

    ADANCIME_MAX = None

    def __init__(self, tabla_joc, j_curent, adancime, parinte=None, scor=None):
        self.tabla_joc = tabla_joc
        self.j_curent = j_curent

        # adancimea in arborele de stari
        self.adancime = adancime

        # scorul starii (daca e finala) sau al celei mai bune stari-fiice (pentru jucatorul curent)
        self.scor = scor

        # lista de mutari posibile din starea curenta
        self.mutari_posibile = []

        # cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        self.stare_aleasa = None

    def jucator_opus(self):
        if self.j_curent == Joc.JMIN:
            return Joc.JMAX
        else:
            return Joc.JMIN
    def getmutari(self):
        return self.tabla_joc.l_mutari
    def mutari(self):
        #Aici calculez toate posiblitatile de mutare pentru toate piesele mutabile pentru calculator
        for i in range(self.tabla_joc.NR_LINII):
            for j in range(self.tabla_joc.NR_COLOANE):
                if self.tabla_joc.matr[i*self.tabla_joc.NR_COLOANE+j]==self.j_curent.lower() or self.tabla_joc.matr[i*self.tabla_joc.NR_COLOANE+j]==self.j_curent.upper():
                    self.tabla_joc.mutari(i,j,self.j_curent,self.tabla_joc.matr)
        #Intrucat , pentru a lua toate posibilitatile de mutare si a pastra elementele din recursivitate,
        #vectorul cu mutari este in clasa , dar in afara functiei , astfel ca pentru a obtine mutarile
        #m-am folosit de functie care returneaza mutarile din clasa joc
        l_mutari=self.getmutari()
        juc_opus = self.jucator_opus()
        l_stari_mutari = [
            Stare(mutare, juc_opus, self.adancime-1, parinte=self) for mutare in l_mutari]
        return l_stari_mutari

    def __str__(self):
        sir = str(self.tabla_joc) + "(Juc curent: "+self.j_curent+")\n"
        return sir


""" Algoritmul MinMax """


def min_max(stare):
	#De corectat min_max
    if stare.adancime == 0 or stare.tabla_joc.final():
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.jucator_opus,stare.adancime)
        return stare

    # calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile = stare.mutari(stare.j_curent)

    # aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutari_scor = [min_max(mutare) for mutare in stare.mutari_posibile]

    if stare.j_curent == Joc.JMAX:
        # daca jucatorul e JMAX aleg starea-fiica cu scorul maxim
        stare.stare_aleasa = max(mutari_scor, key=lambda x: x.scor)
    else:
        # daca jucatorul e JMIN aleg starea-fiica cu scorul minim
        stare.stare_aleasa = min(mutari_scor, key=lambda x: x.scor)

    stare.scor = stare.stare_aleasa.scor
    return stare


def alpha_beta(alpha, beta, stare):
    if stare.adancime == 0 or stare.tabla_joc.final(stare.j_curent):
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.j_curent,stare.adancime)
        return stare
    if alpha >= beta:
        return stare  # este intr-un interval invalid deci nu o mai procesez
    
    #print("")
    stare.mutari_posibile = stare.mutari()
    
    if stare.j_curent == Joc.JMAX:
        scor_curent = float('-inf')
        for mutare in stare.mutari_posibile:
            # calculeaza scorul
            #print("ajungf")
            stare_noua = alpha_beta(alpha, beta, mutare)
            if (scor_curent < stare_noua.scor):
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor
            if(alpha < stare_noua.scor):
                alpha = stare_noua.scor
                if alpha >= beta:
                    break

    elif stare.j_curent == Joc.JMIN:
        scor_curent = float('inf')
        for mutare in stare.mutari_posibile:
            stare_noua = alpha_beta(alpha, beta, mutare)

            if (scor_curent > stare_noua.scor):
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if(beta > stare_noua.scor):
                beta = stare_noua.scor
                if alpha >= beta:
                    break
    if stare.stare_aleasa==None:
        print("overflow")
        return
    stare.scor = stare.stare_aleasa.scor
    return stare


def main():
    # initializare algoritm
    raspuns_valid = False
    while not raspuns_valid:
        tip_algoritm = input(
            "Algorimul folosit? (raspundeti cu 1 sau 2)\n 1.Minimax\n 2.Alpha-beta\n ")
        if tip_algoritm in ['1', '2']:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")

    # initializare ADANCIME_MAX
    raspuns_valid = False
    while not raspuns_valid:
        n = input("Adancime maxima a arborelui: ")
        if n.isdigit():
            Stare.ADANCIME_MAX = int(n)
            raspuns_valid = True
        else:
            print("Trebuie sa introduceti un numar natural nenul.")

    # initializare jucatori
    [s1, s2] = Joc.SIMBOLURI_JUC.copy()  # lista de simboluri posibile
    print(s1,s2)
    raspuns_valid = False
    while not raspuns_valid:
        Joc.JMIN = str(
            input("Doriti sa jucati cu {} sau cu {}? ".format(s1, s2))).upper()
        #print(Joc.JMIN)
        if (Joc.JMIN in ['A','N']):
            raspuns_valid = True
        else:
            print("Raspunsul trebuie sa fie {} sau {}.".format(s1, s2))
    Joc.JMAX = s1 if Joc.JMIN == s2 else s2

    # initializare tabla
    tabla_curenta = Joc()
    print("Tabla initiala")
    print(str(tabla_curenta))

    # creare stare initiala
    stare_curenta = Stare(
        tabla_curenta, 'N', Stare.ADANCIME_MAX)

    linie = -1
    coloana = -1
    finish = 0
    while True:
        if (stare_curenta.j_curent == Joc.JMIN):
            # muta jucatorul
            raspuns_valid = False
            while not raspuns_valid:
                
                linie = int(input("linie= "))
                coloana = int(input("coloana = "))
                aux=copy.deepcopy(stare_curenta.tabla_joc.matr)
                print(stare_curenta.tabla_joc.matr[linie*8+coloana])
                #Verific daca elementul selectat apartine de jucator , daca nu , trb sa aleaga o alta piesa sa mute
                if stare_curenta.tabla_joc.matr[linie*8+coloana]!=Joc.JMIN.lower() and stare_curenta.tabla_joc.matr[linie*8+coloana]!=Joc.JMIN.upper():
                    print("Elementul selectat nu apartine de jucatorul ",Joc.JMIN)
                    continue
                if not stare_curenta.tabla_joc.final(Joc.JMIN):
                    #Verific daca mai sunt mutari valabile pentru jucator
                    print("Aici    ")
                    Test2.muta(linie,coloana,stare_curenta.tabla_joc.matr)
                    #Daca da , fac mutarea pentru input-ul ales
                    if aux!=stare_curenta.tabla_joc.matr:
                        raspuns_valid=True
                else:
                    print("A castigat ",stare_curenta.jucator_opus())
                    break

            # dupa iesirea din while sigur am valida coloana
            # deci pot plasa simbolul pe "tabla de joc"
            #pozitie = linie * Joc.NR_COLOANE + coloana
            #stare_curenta.tabla_joc.matr[pozitie] = Joc.JMIN

            # afisarea starii jocului in urma mutarii utilizatorului
            print("\nTabla dupa mutarea jucatorului")
            print(str(stare_curenta))
            # testez daca jocul a ajuns intr-o stare finala
            # si afisez un mesaj corespunzator in caz ca da
            stare_curenta.j_curent = stare_curenta.jucator_opus()
        # --------------------------------
        else:  # jucatorul e JMAX (calculatorul)
            # Mutare calculator
            #print("inainte calculator")
            # print(str(stare_curenta))
            # preiau timpul in milisecunde de dinainte de mutare
            #print(stare_curenta.tabla_joc.l_mutari)
            stare_curenta.tabla_joc.l_mutari=[]
            t_inainte = int(round(time.time() * 1000))
            if tip_algoritm == '1':
                stare_actualizata = min_max(stare_curenta)
            else:  # tip_algoritm==2
                stare_actualizata = alpha_beta(-5000, 5000, stare_curenta)
            if stare_actualizata.stare_aleasa is None:
                print("A castigat: ",stare_curenta.jucator_opus())
                break
            else:

                stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
                print("Tabla dupa mutarea calculatorului")
                print(str(stare_curenta))
            # preiau timpul in milisecunde de dupa mutare
            t_dupa = int(round(time.time() * 1000))
            print("Calculatorul a \"gandit\" timp de " +
                  str(t_dupa-t_inainte)+" milisecunde.")
            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()


if __name__ == "__main__":
    main()
