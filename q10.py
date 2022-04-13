a = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
c=0
count=0
counter=0
while i<len(a):
	if a[i]>=10000000:
		c=c+1
	elif a[i]>=100000:
		count=count+1
	else :
		counter=counter+1
	i=i+1
print(count,"lakhpati")
print(c,"crorepati")
print(counter,"=","dilbale")