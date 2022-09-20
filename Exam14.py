n1=list(map(int,input().split(",")))
l=[]
for i in range(len(n1)//2):
    l.append(n1[i]+n1[i+len(n1)//2])
print(max(l))
#61,92,82,93,69,88,99,83,67,77,82,89