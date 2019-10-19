#a1=(1,1,1)
#a2=(2,2,2)
#a3=(3,3,3)
x,y,z=map(int,input().split())
a1=(x,y,z)
x,y,z=map(int,input().split())
a2=(x,y,z)
x,y,z=map(int,input().split())
a3=(x,y,z)
if a1 != a2 and a1 != a3:
    for i in range(0,3):
        try:
            a = (a3[i] - a1[i]) / (a2[i] - a1[i])

        except:
            continue

        x31 = a3[0] - a1[0]
        y31 = a3[1] - a1[1]
        z31 = a3[2] - a1[2]

        ax21 = a * (a2[0] - a1[0])
        ay21 = a * (a2[1] - a1[1])
        az21 = a * (a2[2] - a1[2])

        if x31 == ax21 and y31 == ay21 and z31 == az21:
            print('puncte coliniare')
            print('A3 = (1 - ' + str(a)+ ')*A1 + ' + str(a) + '*A2' )
            ok = 1
            break
else:
    print('puncte coliniare')
    print('A2 = 1 * A1 + 0 * A3')
    ok=1

if ok == 0:
    print('puncte necoliniare')


