l=[[2,3],4,[5,6]]
i=0
sum=0
num=0
while i<len(l):
	if i==0 or i==2:
		for j in l[i]:
			if l[i]==l[-i]:
				sum=sum+l[i][-i]
				num=num+j
	else:
		sum=sum+l[i]
	i=i+1
	print(sum)
print(num)