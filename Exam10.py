import math
def findSecretCode(secretcode,firstkey,secondkey):
    return int(math.pow(math.pow(secretcode,firstkey)%10,secondkey)%1000000007)
s=int(input())
n=int(input())
m=int(input())
result=findSecretCode(s,n,m)
print(result)