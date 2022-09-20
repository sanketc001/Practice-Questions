n=input().split(" ")
n.sort(key=len)
n[0]=n[0].capitalize()
print(" ".join(n))