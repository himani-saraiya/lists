a=[[8],[6,87],[54,67]]
i=0
b=[]
while i<len(a):
	j=0
	while j<len(a[i]):
		b.append(a[i][j])
		j=j+1
	i=i+1
print(b)