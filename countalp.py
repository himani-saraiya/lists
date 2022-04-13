chart = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
a=[]
while i<len(chart):
	b=[]
	j=0
	count=0
	while j<len(chart):
		if chart[i]==chart[j]:
			count=count+1
		j=j+1
		b.append(chart[i])
		b.append(count)
		if b not in a:
			a.append(b)	
		i=i+1
print(a)