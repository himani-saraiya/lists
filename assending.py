a= [-2,0,78,-48,9,6]
i=0
while i<len(a):
	j=i+1
	while j<len(a):
		if (a[i]>a[j]):
			temp=a[i]
			a[i]=a[j]
			a[j]=temp
		j=j+1
	i=i+1
print(a)