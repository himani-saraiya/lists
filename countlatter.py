a = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
#d=0
b=" "
while i<len(a):
	c=0
	j=0
	while j<len(a):
		if a[i]==a[j]:
			c=c+1
		j+=1
	if a[i] not in b:
		b+=a[i]
		print(a[i],c)
	i=i+1