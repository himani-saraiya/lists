elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
sum=0
odd_sum=0
c=1
c1=1
c2=1
avg=0
avg1=1
while i<len(elements):
	print('number',elements[i],'count',c)
	if elements[i]%2==0:
		print(c1,'count1','even',elements[i])
		sum=sum+elements[i]
		avg=sum//11
	else:
		print(c2,'count2','odd',elements[i],)
		odd_sum=odd_sum+elements[i]
		avg1=odd_sum//11
		a=sum+odd_sum
		b=avg+avg1
	c=c+1
	c1=c1+1
	c2=c2+1
	i=i+1
print("even sum",sum)
print("odd sum",odd_sum)
print('average',avg)
print('average',avg1)
print("even and odd sum",a)
print("average total",b)
