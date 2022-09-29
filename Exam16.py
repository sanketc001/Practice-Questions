
n=5#int(input())
l1=[4,2,5,1,3]#input().split(",")Root between Children
l2=[1,2,4,5,3]#input().split(",")Root before Children



def printPostOrder(input1, input2, input3):
    c=0
    for i in range(input3):
        if (input1[i] == input2[0]):
            root=i
            c=c+1
            break
    if(c==0):
        root=-1
    if (root != 0):
        printPostOrder(input1, input2[1:input3], root)
    if (root != input3 - 1):
        printPostOrder(input1[root + 1: input3],input2[root + 1: input3],input3 - root - 1)
    l.append(input2[0])
    return l
l=[]
print(printPostOrder(l1, l2, n))