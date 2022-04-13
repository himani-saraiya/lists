a= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
c=0
while i<len(a):
	if a[i]%2==1:
		sum=sum+a[i]
		c+=1
	i=i+1
print(sum//c)