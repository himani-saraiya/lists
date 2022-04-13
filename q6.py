a = [23, 14, 56, 12, 19, 9, 18, 25, 31, 42, 43]
i=0
count=0
while i<len(a):
	if a[i]%2==0:
		count=count+1
	i=i+1
print(count)