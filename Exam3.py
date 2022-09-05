n = int(input())
l = list(map(int, input().split(" ")))
def printSubsequences(arr, index, subarr, s):
    if index == len(arr):
        if len(subarr) != 0:
            return s.append(subarr)
    else:
        printSubsequences(arr, index + 1, subarr, s)
        printSubsequences(arr, index + 1, subarr + [arr[index]], s)
    return s
s = printSubsequences(l, 0, [], [])
sum = 1
for j in s:
    for i in range(1, max(j) + 2):
        if (i not in j):
            sum = sum + i
            break
print(sum)