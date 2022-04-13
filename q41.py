a=['1','2','3','4','5','6','7','8']
i=0
d=[]
c=a[i+1]
while i<len(a)-1:
	c=a[i+1]
	b=str(a[i]+c)
	d.append(b)
	i+=1
print(d)