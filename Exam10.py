import math
def findSecretCode(secretcode,firstkey,secondkey):
    return int(((secretcode**firstkey)%10)**secondkey)
s=int(input())
n=int(input())
m=int(input())
result=findSecretCode(s,n,m)
print(result)