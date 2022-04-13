a=["red","yellow","pink"]
i=0
b=[]
while i<len(a):
	j=0
	c=[]
	while j<len(a[i]):
		c.append(a[i][j])
		j=j+1
	b.append(c)
	i=i+1
print(b)