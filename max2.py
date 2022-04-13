numbers=[[5,6,8,10],[20,25,65,95],[35,75,28,20]]
i=0
while i<len(numbers):
	j=0
	max=0
	while j<len(numbers[i]):
		if numbers[i][j]>max:
			max=numbers[i][j]
		j+=1
	print(max)
	i+=1