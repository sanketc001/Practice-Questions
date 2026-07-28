n=2
input2=5000
if(input2!=5000):
    input2= input2 - (5000 * (input2 % 5000 - 1)) - input2 % 5000
print(input2 // 5000)