arr="4 4 1 4 13 8 8 8 0 8 14 9 15 11 -1 10 15 22 22 22 22 22 21".split(" ")
ans=-9999999999999999
res=-1
weight=[0]*(len(arr)+1)
print(weight)
for i in range(len(arr)):
    source=i
    dest=int(arr[i])
    if(dest!=-1):
        weight[dest]+=source
        if(ans<=weight[dest]):
            ans=max(ans,weight[dest])
            res=dest
if(ans!=-9999999999999999):
    print(res)
else:
    print(-1)