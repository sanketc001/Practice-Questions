url=str(input())
n=int(input())
p=input().split(" ")
v=input().split(" ")
print(url.split("?")[0])
print(len(url.split("?")[1].split(",")))
code=200
for i in sorted(url.split("?")[1].split(",")):
    if(i.split("=")[0] not in p):
        code=404
    print(i.replace("="," "))
print(code)