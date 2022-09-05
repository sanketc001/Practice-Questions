n=int(input())
lst1=list(map(int,input().split()))
lst2=[]
subs=[]
st=[]
def find(inp,out):
     if(len(inp)==0):
        if(len(out)!=0):
            st.append(out)
        return
     find(inp[1:],out[:])
     if(len(out)==0):
        find(inp[1:],inp[:1])
     elif(inp[0]>out[-1]):
        out.append(int[0])
        find(inp[1:],out[:])
find(lst1,lst2)
print(lst1)
for i in st:
     print(*i)
print(st)