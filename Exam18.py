input1=5
input2=3
input3=[[1, 0], [3, 3], [2, 2]]
qu=[i+1 for i in range(input1)]
for i in sorted(input3):
    print(qu,i)
    if i[0]==1:
        qu.pop(0)
    if i[0]==2:
        qu.pop(qu.index(i[1]))
    if i[0]==3:
        print(qu.index(i[1]))
print(0)