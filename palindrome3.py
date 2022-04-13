a=['n','i','t','i','n']
i=-1
while i<len(a):
	b=(a[-1::-1])
	i=i+1
if a==b:
	print(b,'palindrom number')
else:
	print(b,'not palindrom number')