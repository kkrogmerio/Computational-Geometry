
a,b=map(int,input().split())
A=(a,b)
a,b=map(int,input().split())
B=(a,b)
a,b=map(int,input().split())
C=(a,b)
a,b=map(int,input().split())
D=(a,b)
vect=[]
vect.append(A)
vect.append(B)
vect.append(C)
vect.append(D)
vect.sort()

def determinant(A,B,C):
    return A[0] * B[1] + A[1] * C[0] + B[0] * C[1] - B[1] * C[0] - C[1] * A[0] - B[0] * A[1]
def aria(A,B,C):
    return abs(determinant(A,B,C)/2)
def coliniar(A,B,C):
    return (determinant(A,B,C)==0)
def directie(A,B,C):
    det = 0.0

    det = B[0] * C[1] + C[0] * A[1] + A[0] * B[1] - B[0] * A[1] - B[1] * C[0] - A[0] * C[1]

    return det > 0


I=[]
J=[]
'''if coliniar(A,B,C) and coliniar(B,C,D):
    I.append(A)
    I.append(B)
    J.append(C)
    J.append(D)'''
if coliniar(vect[0],vect[1],vect[2]) and coliniar(vect[1],vect[2],vect[3]):
    I.append(vect[0])
    I.append(vect[3])
    J.append(vect[1])
    J.append(vect[2])
else:
    area1=[A,B,C]
    area2=[A,B,D]
    area3=[A,C,D]
    area4=[B,C,D]
    area=[]
    area.append(area1)
    area.append(area2)
    area.append(area3)
    area.append(area4)
    area.sort(key=lambda x:aria(x[0],x[1],x[2]),reverse=True)
    if area[0]==area[1]+area[2]+area[3]:
        print("3 puncte form un triunghi iar al 4-lea este in interiorul lui")
        if area1==area[0]:
            I.append(D)
            J.append(A)
            J.append(B)
            J.append(C)
        elif area2==area[0]:
            I.append(C)
            J.append(A)
            J.append(B)
            J.append(D)
        elif area3==area[0]:
            I.append(B)
            J.append(A)
            J.append(D)
            J.append(C)
        elif area4==area[0]:
            I.append(A)
            J.append(B)
            J.append(D)
            J.append(C)
    else:
        print('cele 4 pct form un patrulater:')
        if (directie(A,B,C) and not directie(A,B,D)) or (not directie(A,B,C) and directie(A,B,D)):
            I.append(A)
            I.append(B)
            J.append(C)
            J.append(D)
        elif (directie(A,C,B) and not directie(A,C,D)) or (not directie(A,C,B) and directie(A,C,D)):
            I.append(A)
            I.append(C)
            J.append(B)
            J.append(D)
        else:
            I.append(A)
            I.append(D)
            J.append(B)
            J.append(C)
print("I:  ",I)
print("J:  ",J)