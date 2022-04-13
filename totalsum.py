l=[[2,3],4,[5,6]]
i=0
sum=0
while i<len(l):
	if i==0 or i==2:
		j=0
		while j<len(l[i]):
			sum=sum+l[i][j]
			j=j+1
else:
	sum=sum+l[i]
	i=i+1