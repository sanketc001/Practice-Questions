m=int(input())-1
n=int(input())-1
l=[]
t=1
for i in range((max(m,n)+1)):
    t=t+(i*2)
    l.append(t)
if(m>=n):
    if(m%2==0):
        print(l[m]-(m-n))
    else:
        print(l[m]+(m - n))
else:
    if (n % 2 == 0):
        print(l[n]+(n-m))
    else:
        print(l[n]-(n-m))
'''
p=[]
t=1
for i in range(10000):
    p.append(t)
    t=t+2
for i in range(max(m,n)+1):
    t=0
    for j in range(max(m,n)+1):
        if(i%2==0):
            t+=1
            l[0].append(t+j)
        else:
            t=t+p[i]+p[i-1]-1
            l[0].append(t-j)
'''
'''
1 2 9 10
4 3 8 11
5 6 7 12
16151413
'''