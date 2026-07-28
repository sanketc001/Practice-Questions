n=int(input())
l=list(str(n))
c=0
for i in range(len(l)):
    if(int(l[i])<3):
        l[i]="3"
        c=c+1
        break
if(c==0):
    l[-1]="3"
print("".join(l))
