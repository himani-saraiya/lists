a=[1,2,3,4,5,6]
b=[9,8,7,10,20,13]
a.extend(b)
print(a)
i=0
c=[]
l=[]
while i<len(a):
	if a[i]%2==0:
		c.append(a[i])
	else:
		l.append(a[i])
	i=i+1
print(c)
print(l)