# i=0
# while i<=10:
#     if i%2==0:
#         print(i)
#     i=i+1
# j=0
# while j<=10:
#     if j%2==1:
#         print(j)
#     j+=1

a = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
#d=0
b=" "
while i<len(a):
	c=0
	j=0
	while j<len(a):
		if a[i]==a[j]:
			c=c+1
		j+=1
	if a[i] not in b:
		b+=a[i]
		print(a[i],c)
	i=i+1