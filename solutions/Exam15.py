n=int(input())
l=input().split(",")#[1,2,1,1,1,1,1,1]
b=[]
t=[]
for i in range(len(l)):
    if(l[i] not in t):
        t.append(l[i])
    else:
        t.append(l[i])
        b.append(t)
        t=[]
print(len(b))