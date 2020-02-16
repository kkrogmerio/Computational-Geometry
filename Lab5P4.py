v=[]
n=str(input())
for i in n:
    #print(i)
    v.append(i)

check=set()
dict=set()
def palin(ind):
    num=0
    ind1=ind
    ind2=ind
    while(ind1>=0 and ind2<=len(v)-1):
        #oki=0
        #if v[ind1]==v[ind2]:    
            #oki=1
        #if oki==0:
            #break
        if ind1>0:
            copie=v[ind+1:ind2+1]
            copie.reverse()
            #print(v[ind1-1:ind+1])
            
            if v[ind1-1:ind+1]==copie and len([x for x in check if x==v[ind1-1:ind2+1]])==0:
                print('ceaules')
                num+=1
                dict.add("".join(v[ind1-1:ind2+1]))
                check.add(str(v[ind1-1:ind2+1]))
                
        if ind2<len(v)-1:
            copie=v[ind+1:ind2+2]
            copie.reverse()
            #print(v[ind1:ind+1])
            if v[ind1:ind+1]==copie and len([x for x in check if x==v[ind1:ind2+2]])==0:
                num+=1
                #print('ceaules')
                dict.add("".join(v[ind1:ind2+2]))
                check.add(str(v[ind1:ind2+2]))
        if 1:
            copie=v[ind+1:ind2+1]
            copie.reverse()
            #print(v[ind1:ind],' ',copie)
            if v[ind1:ind]==copie and len([x for x in check if x==v[ind1:ind2+1]])==0:
                    num+=1
                    dict.add("".join(v[ind1:ind2+1]))
                    check.add(str(v[ind1:ind2+1]))
        
        ind1-=1
        ind2+=1
        
        
    return num

'''mapa=[0]*n
for i in range(n):
    mapa[i]=[0]*n
for i in range(n):
    mapa[i][i]=1
for l in range(3,n):
    for i in range(0,n-l):
        j=i+l-1
        if s[i]==s[j]:
            mapa[i][j]=mapa[i-1][j-1]'''

suma=0
'''for i in range(len(v)):
    suma+=palin(i)
print(suma)
for i in check:
   print(i)'''

s=n
s=' '+s
print(s,' ',dict)
num=len(s)
vect=[0]*num
for i in range(num):
    vect[i]=[0]*num
def palindrom(i,j):
    global vect,s
    if s[i]==s[j]:
        vect[i][j]=1
    i-=1
    j+=1
    while i>=0 and j<len(s):
        if vect[i+1][j-1]==1 and s[i]==s[j]:
            #print('hintru')
            vect[i][j]=1
        else:
            break
        i-=1
        j+=1

for i in range(num):
    palindrom(i,i)
    if i+1<(num):
        palindrom(i+1,i)
    




def spaces(s, dict):
    n = len(s)
    global prev, l,vect
    L = [-1] * (n)
    prev = [-1] * (n)
    L[0] = 0
    for i in range(1,n):
        for j in range(i, 0, -1):
            if vect[j][i]==1: 
                if((L[j-1]+1 < L[i] or L[i]==-1) and L[j-1]!=-1):
                    L[i] = L[j - 1] + 1
                    prev[i] = j - 1
    return L[n - 1]
def print_substr(i):
    if prev[i] > 0:
        print_substr(prev[i])
    print( s[prev[i] + 1 : i + 1] )
print(spaces(s, dict))
print_substr(len(s) - 1)
'''alg divide/greedy corect , povestiri algoritmi'''


