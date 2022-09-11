n=list("389899")
for i in range(len(n)-1,0,-1):
    if((int(n[i])+int(n[i-1]))==17):
        n.pop(i)
        n.pop(i-1)
print(len(n))