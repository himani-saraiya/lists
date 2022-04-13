a=[4,6,8,10]
i=1
b=[]
while i<len(a):
	c=a[-i]-a[-i-1]
	b.append(c)
	i=i+1
print(b)
