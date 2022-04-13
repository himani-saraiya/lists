binary=[1,0,0,1,1,0,1,1]
b=0
i=-1
sum=0
while i>=-len(binary):
	sum=sum+binary[i]*b
	b=b+1
	i=i-1
print(sum)