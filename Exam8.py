n=8#int(input())
inputList=list(map(int, "11 7 5 10 46 23 16 8".split(" ")))
num=3#int(input())
def funSort(inputList, num):
    p=[]
    for i in sorted(inputList[:num]):
        p.append(str(i))
    for i in sorted(inputList[num:], reverse=True):
        p.append(str(i))
    return p
result=funSort(inputList, num)
print(" ".join(result))
#print(" ".join(sorted(l[:k]))," ".join(sorted(l[k:],reverse=True)))
