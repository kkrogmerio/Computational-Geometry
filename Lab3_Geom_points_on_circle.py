import math
a,b=map(int,input().split())
A=(a,b)
a,b=map(int,input().split())
B=(a,b)
a,b=map(int,input().split())
C=(a,b)
a,b=map(int,input().split())
D=(a,b)
def calcul(A,B):
    return A[0]*B[0]+A[1]*B[1]
def cos(A,A1,A2):
    return calcul(A1,A2)/(math.sqrt(calcul(A1,A1)*calcul(A2,A2)))
def vectorul(A,B):
    return (B[0]-A[0],B[1]-A[1])
def directie(A,B,C):
    det = 0.0

    det = B[0] * C[1] + C[0] * A[1] + A[0] * B[1] - B[0] * A[1] - B[1] * C[0] - A[0] * C[1]

    return det > 0
def functie():
    if ((directie(A,B,C) and not directie(A,B,D)) or (not directie(A,B,C) and directie(A,B,D))) and ((directie(A,C,B) and not directie(A,C,D)) or (not directie(A,C,B) and directie(A,C,D))):
        print('punctele form patrulater convex')
    else:
        if A==B or A==C or A==D or B==C or B==D or C==D:
            print("Puncte coliniare")
            return 0
    cosA,cosB,cosC,cosD=cos(A,vectorul(A,B),vectorul(A,D)),cos(B,vectorul(B,A),vectorul(B,C)),cos(C,vectorul(C,B),vectorul(C,D)),cos(D,vectorul(D,A),vectorul(D,C))
    cosB=math.acos(cosB) * 180 /math.pi
    cosD=math.acos(cosD) * 180 /math.pi
    print(cosB, ' ',cosD)
    if cosB+cosD==180.00:
        print("Punctul e pe cerc")
    else:
        if cosB+cosD<180:
            print("Punctul e in exteriorul cercului")
        else:
            print("Punctul e in interiorul cercului")
functie()
