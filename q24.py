a=[12,67,98,34]
i=0
b=[]
while i<len(a):
	sum=0
	c=a[i]
	if c>0:
		d=c%10
		sum=sum+d
		c=c//10+sum
		b.append(sum)
	i=i+1
	print(b)