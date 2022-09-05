def printallSublists(nums, target):
	d = {}
	d.setdefault(0, []).append(-1)
	sum_so_far = 0
	for index in range(len(nums)):
		sum_so_far += nums[index]
		if (sum_so_far - target) in d:
			return [nums[value+1: index+1] for value in d.get(sum_so_far-target)]
		d.setdefault(sum_so_far, []).append(index)


s=input()
n,k=list(map(int, s.split(" ")))
s=input()
a=list(map(int, s.split(" ")))
b=printallSublists(a, k)[0]
st=[x for x in range(len(a)) if a[x:x+len(b)] == b][0]
en=st+len(b)
print(st+1,en)