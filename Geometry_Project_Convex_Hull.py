import matplotlib.pyplot as plt
n=int(input())
def directie(A,B,C):
    det = 0.0
    #print(B[0],C[1],C[0],A[1],A[0])
    det = B[0] * C[1] + C[0] * A[1] + A[0] * B[1] - B[0] * A[1] - B[1] * C[0] - A[0] * C[1]
    return det
v=[]
vect=[]
for i in range(n):
    x,y=map(int,input().split())
    v.append((x,y))
v.sort()
vect.append(v[0])
print(vect[0])
for i in range(1,len(v)-1):
    if directie(vect[len(vect)-1],v[i],v[i+1])<0:
        vect.append(v[i])
    #elif directie(vect[len(vect)-1],v[i],v[i+1])>=0:
       # vect.append(v[i+1])
if directie(vect[len(vect)-1],v[len(v)-1],v[0])<0:
    vect.append(v[len(v)-1])
#elif directie(vect[len(v)-2],v[len(v)-1],v[0])>=0:
    #v#ect.append(v[0])
vect.append(v[0])
#vect.append(v[0])
        

x=[i[0] for i in vect]
y=[i[1] for i in vect]
plt.plot(x, y)
plt.axis([-10,20,-10, 20])
print(vect)
for i_x, i_y in zip(x, y):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y),style='italic')
x=[i[0] for i in v]
y=[i[1] for i in v]
plt.plot(x, y,'ro')
plt.axis([-11,20,-11, 20])

for i_x, i_y in zip(x, y):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))

plt.show()