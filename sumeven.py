a= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
while i<len(a):
	if a[i]%2==0:
		sum=sum+a[i]
	i=i+1
print(sum)