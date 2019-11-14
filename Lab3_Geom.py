a1=[]
a2=[]
a3=[]
a4=[]
x,y=map(int,input().split())
a1=((x,y))
x,y=map(int,input().split())
a2=((x,y))
x,y=map(int,input().split())
a3=((x,y))
x,y=map(int,input().split())
a4=((x,y))
def sarrus(p1,p2,p3):
    return p1[0]*p2[1]+p2[0]*p3[1]+p1[1]*p3[0]-p3[0]*p2[1]-p3[1]*p1[0]-p1[1]*p2[0]
vala1=-a2[1]+a1[1]
valb1=a2[0]-a1[0]
vala2=-a4[1]+a3[1]
valb2=a4[0]-a3[0]
valc1=-a1[1]*vala1-a1[0]*valb1
valc2=-a3[1]*vala2-a3[0]*valb2
sigma=vala1*valb2-vala2*valb1

if sigma is not 0:
    x=(valc2*valb1-valc1*valb2)/sigma
    y=(vala2*valc1-valc2*vala1)/sigma
    
    if x>min(a1[0],a2[0]) and x>min(a3[0],a4[0]) and x<max(a1[0],a2[0]) and x<max(a3[0],a4[0]) and y>min(a1[1],a2[1]) and y>min(a3[1],a4[1]) and y<max(a1[1],a2[1]) and x<max(a3[1],a4[1]):
        print('punctele apartin')
    else:
        print('punctele nu apartin')
if sigma is 0 :
    if (vala1*valb2-vala2*valb1)+(vala1*valc2-valc1*vala2)+(valb1*valc2-valc1*valb2) is 0:
        if sarrus(a3,a1,a2)*sarrus(a3,a1,a4)<=0 and sarrus(a4,a2,a1)*sarrus(a4,a2,a3)<=0:
            #AB interior CD viceversa
            #XA XB < XC XD
            print('A1A2 se intersect cu A3A4')
            #http://campion.edu.ro/arhiva/www/arhiva_2009/papers/paper41.pdf
    else:
        print('A1A2 intersectat cu A3A4 da multimea vida')

