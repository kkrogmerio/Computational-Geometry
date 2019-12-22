n,m=map(int,input().split())
c=[0]*m
for i in range(m):
    c[i]=[]
for i in range(m):
    for val in input().split():
        val=int(val)
        c[i].append(val)
suma=0
salv=[]
for i in range(m):
    suma+=len(c[i])
def save(salv,save,ind):
    if (save not in salv and len(save)>1):
        salv.append((save.copy(),ind))
        
    elif (save not in salv and len(save) == 1):
        x=int(save[0])
        salv.append((x,ind))

       
def load(E,salv):   
    while salv:

        if salv[len(salv)-1][1]!=-1 and len(E)>salv[len(salv)-1][1]:

            E[salv[len(salv)-1][1]].append(salv[len(salv)-1][0])
        elif salv[len(salv)-1][1]==-1:
        
            E.append(salv[len(salv)-1][0])
        salv.pop()
oke=0  
nr=0   
def back(k,E,salv):
    vect=E
    global oke
    global nr
    print(E)
    if E==[]:
        oke=1
        return True
    if oke==1:
        return True
    
   
    nr+=1
    if nr>n:
        return
    num,elem=0,0
    ''' if len(E[num]) == 1 and k*-1 in E[num]:
            oke=1
            print(E,' ',E[num])
            return True
        if len(E[num]) == 1 and k in E[num]:
            E.pop(num)
            continue'''
    while num<len(E):
       
        if k in E[num]:
            if k*-1 in E[num]:
        
                save(salv,E[num],-1)
                E.pop(num)
                num-=1
                
                
                
            
            else:
                ind=E[num].index(k)
                save(salv,[E[num][ind]],num)
                E[num].pop(ind)
                if len(E[num])==0:
                    E.pop(num)
                    num-=1
        num+=1
    print(E)
    if E==[]:
        print(E)
        oke=1
        return True
    back(k+1,E,[])
    '''print(E,k)
    load(E,salv)
    print(E,k)'''
    print(E)
    E=vect
    #print(oke)
    if E==[]:
        print(E)
        oke=1
        return True
    if oke==1:
        return True
    #print(E)
    #print(E)
    nr+=1
    if nr==120:
        oke=1
    if oke==1:
        return
    num,elem=0,0
    ''' if len(E[num]) == 1 and k in E[num]:
            oke=1
            return
        if len(E[num]) == 1 and k*-1 in E[num]:
            E.pop(num)
            continue'''
    
    while num<len(E):
       
        if k*-1 in E[num]:
            if k in E[num]:
                save(salv,E[num],-1)
                E.pop(num)
                num-=1
                
                
                
            
            else:
                ind=E[num].index(k*-1)
                save(salv,[E[num][ind]],num)
                E[num].pop(ind)
                if len(E[num])==0:
                    E.pop(num)
                    num-=1
        num+=1
    print(E)
    if E==[]:
        oke=1
        return True

    back(k+1,E,[])
print(back(1,c,salv))

            
    
    
