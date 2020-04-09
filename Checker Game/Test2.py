def matrice():
    tabla=['#']*64
    for i in range(1,8,2):
        tabla[i]='a'
    for i in range(0,8,2):
        tabla[8+i]='a'
    for i in range(1,8,2):
        tabla[16+i]='a'
    for i in range(0,8,2):
        tabla[5*8+i]='n'
    for i in range(1,8,2):
        tabla[6*8+i]='n'
    for i in range(0,8,2):
        tabla[7*8+i]='n'
    return tabla
tabla=matrice()
def afis(tabla):

    print(" ",end=" ")
    for i in range(8):
        print(i,end=" ")
    print("")
    for i in range(8):
        print(i,end=" ")
        for j in range(8):
            print(tabla[i*8+j],end=" ")
        print("")
tabla[8*0+4]='A'
tabla[8*3+5]='N'
tabla[8*5+5]='n'
okey =0
#afis()
def muta(linie,coloana,matrice):
    #Functie pentru a muta dedicata jucatorului(in care poate alege ce mutare sa mute)
    for i in range(8):
        for j in range(8):
            print(matrice[8*i+j],end=" ")
        print(" ")
    raspuns_valid=False
    global okey
    nr=0
    print(linie,coloana)
    if matrice[linie*8+coloana]=='n':
        while not raspuns_valid:
            if nr==2:
                print("Se pare ca nicio mutare nu mai este valabila , piesa este imutabila")
                if okey==1:
                    return 1
                else:
                    return -1
            nr+=1
            choose=int(input("1 stanga sus 2 dreapta sus: "))
            if(choose)==1:
                if not (linie-1>=0 and coloana-1>=0):
                    print("Mutare imposibila in acea directie,incearca alta")
                else:
                    if matrice[(linie-1)*8+coloana-1]=='#':
                        matrice[linie*8+coloana]='#'
                        if linie-1>0:
                            matrice[(linie-1)*8+coloana-1]='n'
                        else:
                            matrice[(linie-1)*8+coloana-1]='N' 
                        raspuns_valid=True
                        okey=1
                    elif matrice[(linie-1)*8+coloana-1]=='a' or matrice[(linie-1)*8+coloana-1]=='A':
                        if linie-2>=0 and coloana-2>=0:
                            matrice[(linie-2)*8+coloana-2]='n'
                            if linie-2==0:
                                matrice[(linie-2)*8+coloana-2]='N'
                            matrice[linie*8+coloana]='#'
                            matrice[(linie-1)*8+coloana-1]='#'
                            raspuns_valid=True
                            okey=1
                            return muta(linie-2,coloana-2,matrice)
                        else:
                            print("mutare imposibila de efectuat")
                    else:
                        print("mutare imposibila de facut , incearca alta")
            elif choose==2:
                if not (linie-1>=0 and coloana+1<8):
                    print("Mutare imposibila in acea directie,incearca alta")
                else:
                    if matrice[(linie-1)*8+coloana+1]=='#':
                        matrice[linie*8+coloana]='#'
                        if linie-1>0:
                            matrice[(linie-1)*8+coloana+1]='n'
                        else:
                            matrice[(linie-1)*8+coloana+1]='N' 
                        raspuns_valid=True
                        okey=1
                    elif matrice[(linie-1)*8+coloana+1]=='a' or matrice[(linie-1)*8+coloana+1]=='A':
                        if linie-2>=0 and coloana+2<8 and matrice[(linie-2)*8+coloana+2]=='#':
                            matrice[(linie-2)*8+coloana+2]='n'
                            if linie-2==0:
                                matrice[(linie-2)*8+coloana+2]='N'
                            matrice[linie*8+coloana]='#'
                            matrice[(linie-1)*8+coloana+1]='#'
                            raspuns_valid=True
                            okey=1
                            return muta(linie-2,coloana+2,matrice)
                        else:
                            print("mutare imposibila de efectuat")
                    else:
                        print("mutare imposibila de facut , incearca alta")
    
    if matrice[linie*8+coloana]=='a':
        while not raspuns_valid:
            if nr==2:
                print("Se pare ca nicio mutare nu mai este valabila , piesa este imutabila")
                if okey==1:
                    return 1
                else:
                    return -1
            nr+=1
            choose=int(input("1 stanga jos 2 dreapta jos: "))
            if(choose)==1:
                if not (linie+1<8 and coloana-1>=0):
                    print("Mutare imposibila in acea directie,incearca alta")
                else:
                    if matrice[(linie+1)*8+coloana-1]=='#':
                        matrice[linie*8+coloana]='#'
                        if linie+1<7:
                            matrice[(linie+1)*8+coloana-1]='a'
                        else:
                            matrice[(linie+1)*8+coloana-1]='A' 
                        raspuns_valid=True
                        okey=1
                    elif matrice[(linie+1)*8+coloana-1]=='n' or matrice[(linie+1)*8+coloana-1]=='N':
                        if linie+2<8 and coloana-2>=0 and matrice[(linie+2)*8+coloana-2]=='#':
                            matrice[(linie+2)*8+coloana-2]='a'
                            if linie+2==7:
                                matrice[(linie+2)*8+coloana-2]='A'
                            matrice[linie*8+coloana]='#'
                            matrice[(linie+1)*8+coloana-1]='#'
                            raspuns_valid=True
                            okey=1
                            return muta(linie+2,coloana-2,matrice)
                        else:
                            print("mutare imposibila de efectuat")
                    else:
                        print("mutare imposibila de facut , incearca alta")
            elif choose==2:
                if not (linie+1<8 and coloana+1<8):
                    print("Mutare imposibila in acea directie,incearca alta")
                else:
                    if matrice[(linie+1)*8+coloana+1]=='#':
                        matrice[linie*8+coloana]='#'
                        if linie+1<7:
                            matrice[(linie+1)*8+coloana+1]='a'
                        else:
                            matrice[(linie+1)*8+coloana+1]='A' 
                        raspuns_valid=True
                        okey=1
                    elif matrice[(linie+1)*8+coloana+1]=='n' or matrice[(linie+1)*8+coloana+1]=='N':
                        if linie+2<=7 and coloana+2<8 and matrice[(linie+2)*8+coloana+2]=='#':
                            matrice[(linie+2)*8+coloana+2]='a'
                            if linie+2==7:
                                matrice[(linie+2)*8+coloana+2]='A'
                            matrice[linie*8+coloana]='#'
                            matrice[(linie+1)*8+coloana+1]='#'
                            raspuns_valid=True
                            okey=1
                            return muta(linie+2,coloana+2,matrice)
                        else:
                            print("mutare imposibila de efectuat")
                    else:
                        print("mutare imposibila de facut , incearca alta")
            if raspuns_valid==False:
                print("Incearca alta mutare")
    elif matrice[linie*8+coloana]=='A':
        while not raspuns_valid:
            if nr==4:
                print("Se pare ca nicio mutare nu mai este valabila , piesa este imutabila")
                if okey==1:
                    return 1
                else:
                    return -1
            nr+=1
            choose=int(input("1 stanga sus 2 dreapta sus 3 stanga jos 4 dreapta jos"))
            if(choose)==1:
                if not (linie-1>=0 and coloana-1>=0):
                    print("Mutare imposibila in acea directie,incearca alta")
                else:
                    if matrice[(linie-1)*8+coloana-1]=='#':
                        matrice[linie*8+coloana]='#'
                        matrice[(linie-1)*8+coloana-1]='A' 
                        raspuns_valid=True
                        okey=1
                    elif matrice[(linie-1)*8+coloana-1]=='n' or matrice[(linie-1)*8+coloana-1]=='N':
                        if linie-2>=0 and coloana-2>=0:
                            matrice[(linie-2)*8+coloana-2]='A'
                            matrice[linie*8+coloana]='#'
                            matrice[(linie-1)*8+coloana-1]='#'
                            okey=1
                            raspuns_valid=True
                            #In cazul in care o piesa a facut jump , ea va fi capabila sa faca o inca mutare
                            return muta(linie-2,coloana-2,matrice)
                        else:
                            print("mutare imposibila de efectuat")
                    else:
                        print("mutare imposibila de facut , incearca alta")
            elif choose==2:
                if not (linie-1>=0 and coloana+1<8):
                    print("Mutare imposibila in acea directie,incearca alta")
                else:
                    if matrice[(linie-1)*8+coloana+1]=='#':
                        matrice[(linie)*8+coloana]='#'
                        matrice[(linie-1)*8+coloana+1]='A' 
                        raspuns_valid=True
                        okey=1
                    elif matrice[(linie-1)*8+coloana+1]=='n' or matrice[(linie-1)*8+coloana+1]=='N':
                        if linie-2>=0 and coloana+2<8 and matrice[(linie-2)*8+coloana+2]=='#':
                            matrice[(linie-2)*8+coloana+2]='A'
                            matrice[linie*8+coloana]='#'
                            matrice[(linie-1)*8+coloana+1]='#'
                            raspuns_valid=True
                            okey=1
                            return muta(linie-2,coloana+2,matrice)
                        else:
                            print("mutare imposibila de efectuat")
                    else:
                        print("mutare imposibila de facut , incearca alta")
            elif(choose)==3:
                if not (linie+1<8 and coloana-1>=0):
                    print("Mutare imposibila in acea directie,incearca alta")
                else:
                    if matrice[(linie+1)*8+coloana-1]=='#':
                        matrice[linie*8+coloana]='#'
                        matrice[(linie+1)*8+coloana-1]='A' 
                        raspuns_valid=True
                        okey=1
                    elif matrice[(linie+1)*8+coloana-1]=='n' or matrice[(linie+1)*8+coloana-1]=='N':
                        if linie+2<8 and coloana-2>=0 and matrice[(linie+2)*8+coloana-2]=='#':
                            matrice[(linie+2)*8+coloana-2]='A'
                            matrice[linie*8+coloana]='#'
                            matrice[(linie+1)*8+coloana-1]='#'
                            raspuns_valid=True
                            okey=1
                            return muta(linie+2,coloana-2,matrice)
                        else:
                            print("mutare imposibila de efectuat")
                    else:
                        print("mutare imposibila de facut , incearca alta")
            elif choose==4:
                if not (linie+1<8 and coloana+1<8):
                    print("Mutare imposibila in acea directie,incearca alta")
                else:
                    if matrice[(linie+1)*8+coloana+1]=='#':
                        matrice[linie*8+coloana]='#'
                        matrice[(linie+1)*8+coloana+1]='A' 
                        raspuns_valid=True
                        okey=1
                    elif matrice[(linie+1)*8+coloana+1]=='n' or matrice[(linie+1)*8+coloana+1]=='N':
                        if linie+2<=7 and coloana+2<8 and matrice[(linie+2)*8+coloana+2]=='#':
                            matrice[(linie+2)*8+coloana+2]='A'
                            matrice[linie*8+coloana]='#'
                            matrice[(linie+1)*8+coloana+1]='#'
                            raspuns_valid=True
                            okey=1
                            return muta(linie+2,coloana+2,matrice)
                        else:
                            print("mutare imposibila de efectuat")
                    else:
                        print("mutare imposibila de facut , incearca alta")
    elif matrice[linie*8+coloana]=='N':
        while not raspuns_valid:
            if nr==4:
                print("Se pare ca nicio mutare nu mai este valabila , piesa este imutabila")
                if okey==1:
                    return 1
                else:
                    return -1
            nr+=1
            choose=int(input("1 stanga sus 2 dreapta sus 3 stanga jos 4 dreapta jos"))
            if(choose)==1:
                if not (linie-1>=0 and coloana-1>=0):
                    print("Mutare imposibila in acea directie,incearca alta")
                else:
                    if matrice[(linie-1)*8+coloana-1]=='#':
                        matrice[linie*8+coloana]='#'
                        matrice[(linie-1)*8+coloana-1]='N' 
                        raspuns_valid=True
                        okey=1
                    elif matrice[(linie-1)*8+coloana-1]=='a' or matrice[(linie-1)*8+coloana-1]=='A':
                        if linie-2>=0 and coloana-2>=0:
                            matrice[(linie-2)*8+coloana-2]='N'
                            matrice[linie*8+coloana]='#'
                            matrice[(linie-1)*8+coloana-1]='#'
                            okey=1
                            raspuns_valid=True
                            return muta(linie-2,coloana-2,matrice)
                        else:
                            print("mutare imposibila de efectuat")
                    else:
                        print("mutare imposibila de facut , incearca alta")
            elif choose==2:
                if not (linie-1>=0 and coloana+1<8):
                    print("Mutare imposibila in acea directie,incearca alta")
                else:
                    if matrice[(linie-1)*8+coloana+1]=='#':
                        matrice[(linie)*8+coloana]='#'
                        matrice[(linie-1)*8+coloana+1]='N' 
                        raspuns_valid=True
                        okey=1
                    elif matrice[(linie-1)*8+coloana+1]=='a' or matrice[(linie-1)*8+coloana+1]=='A':
                        if linie-2>=0 and coloana+2<8 and matrice[(linie-2)*8+coloana+2]=='#':
                            matrice[(linie-2)*8+coloana+2]='N'
                            matrice[linie*8+coloana]='#'
                            matrice[(linie-1)*8+coloana+1]='#'
                            raspuns_valid=True
                            okey=1
                            return muta(linie-2,coloana+2,matrice)
                        else:
                            print("mutare imposibila de efectuat")
                    else:
                        print("mutare imposibila de facut , incearca alta")
            elif(choose)==3:
                if not (linie+1<8 and coloana-1>=0):
                    print("Mutare imposibila in acea directie,incearca alta")
                else:
                    if matrice[(linie+1)*8+coloana-1]=='#':
                        matrice[linie*8+coloana]='#'
                        matrice[(linie+1)*8+coloana-1]='N' 
                        raspuns_valid=True
                        okey=1
                    elif matrice[(linie+1)*8+coloana-1]=='a' or matrice[(linie+1)*8+coloana-1]=='A':
                        if linie+2<8 and coloana-2>=0 and matrice[(linie+2)*8+coloana-2]=='#':
                            matrice[(linie+2)*8+coloana-2]='N'
                            matrice[linie*8+coloana]='#'
                            matrice[(linie+1)*8+coloana-1]='#'
                            raspuns_valid=True
                            okey=1
                            return muta(linie+2,coloana-2,matrice)
                        else:
                            print("mutare imposibila de efectuat")
                    else:
                        print("mutare imposibila de facut , incearca alta")
            elif choose==4:
                if not (linie+1<8 and coloana+1<8):
                    print("Mutare imposibila in acea directie,incearca alta")
                else:
                    if matrice[(linie+1)*8+coloana+1]=='#':
                        matrice[linie*8+coloana]='#'
                        matrice[(linie+1)*8+coloana+1]='N' 
                        #Mutare normala
                        raspuns_valid=True
                        okey=1
                    elif matrice[(linie+1)*8+coloana+1]=='a' or matrice[(linie+1)*8+coloana+1]=='A':
                        if linie+2<=7 and coloana+2<8 and matrice[(linie+2)*8+coloana+2]=='#':
                            matrice[(linie+2)*8+coloana+2]='N'
                            matrice[linie*8+coloana]='#'
                            matrice[(linie+1)*8+coloana+1]='#'
                            raspuns_valid=True
                            okey=1
                            #Mutare jump , mai pot face miscari
                            return muta(linie+2,coloana+2,matrice)
                        else:
                            print("mutare imposibila de efectuat")
                    else:
                        print("mutare imposibila de facut , incearca alta")
#print(muta(0,4,tabla))




