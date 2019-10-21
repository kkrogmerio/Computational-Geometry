"""
1. Se dau n cuburi cu laturile diferite două câte două. Fiecare cub are o culoare, codificată cu un
 număr de la 1 la p (p dat). Să se construiască un turn de înălţime maximă de cuburi în care un cub 
 nu poate fi aşezat pe un cub de aceeaşi culoare sau cu latură mai mică decât a sa – O(n logn). 
 Justificaţi corectitudinea algoritmului propus. În cazul în care lungimile laturilor cuburilor nu
  erau diferite mai este valabilă metoda propusă? Justificaţi. Exemplu: pentru n=4, p=2 şi cuburi 
  cu caracteristicile latură/culoare: 5/1, 10/1, 9/1, 8/2, o soluţie este turnul cu cuburile 10/1, 8/2,
    5/1. Se aleg 3 cuburi, cuburile 2 4 și 1 (în ordinea datelor de intrare) și se obține înălțimea 23."""
from queue import PriorityQueue
q = PriorityQueue()
v=[]
elem=list()
ind=0
n,m=map(int,input().split())
for i in range(0,n):
    ind+=1
    x,y=map(int,input().split())
    q.put((-x,-y,ind))

num=0
sumi=0
while not q.empty():
    
    a=q.get()
    a=(a[0]*-1,a[1]*-1,a[2])
   # print(a[0],' ',a[1])
    if len(elem)==0:
        elem.append((a[0],a[1],a[2]))
        num+=1
        sumi+=a[0]
    if elem[-1][1]==a[1] or elem[-1][0]<a[0]:
        continue
    
    num+=1
    sumi+=a[0]
    elem.append((a[0],a[1],a[2]))
    
print(num,' ',sumi)
for i in elem:
    print(i[2])