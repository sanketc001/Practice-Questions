n=int(input())
s=[]
l=[]
for i in range(n):
    s.append(input())
for i in s:
    if(i=='I'):
        l.append(l[-1]*2)
    elif(i=='+'):
        l.append(l[-1]+l[-2])
    elif(i=='R'):
        l.pop()
    else:
        l.append(int(i))
print(sum(l))