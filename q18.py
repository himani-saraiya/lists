a=[1,2,3,4,5,6,7,9,11]
i=0
b=[]
while i<len(a):
	j=1
	c=0
	while j<=a[i]:
		if a[i]%j==0:
			c=c+1
		j=j+1
	if c==2:
		b=b+[a[i]]
	i=i+1
print(b)
	