n=7
l=list(map(int,"9 -3 8 -6 -7 8 10".split(" ")))
def productsAtNegativeTemp(temperature):
    c = 0
    for i in temperature:
        if(i!=abs(i)):
            c=c+1
    return c
result=productsAtNegativeTemp(l)
print(result)