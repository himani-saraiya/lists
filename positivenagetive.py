a = [2, -7, 5, -64, -14]
i=0
c=0
d=0
while i<len(a):
	if a[i]>0:
		c=c+1
	else:
		d=d+1
	i=i+1
print(c,"posutive",d,"negative")