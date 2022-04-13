a=[[10,20],[30,40],[50,60],[30,20,80]]
b=[[61],[12,14,15],[12,13,19,20],[12]]
i=0
sum=0
while i<1:
    j=0
    while j<len(b):
        if a[i]==b[j]:
            sum==sum+a[i]+b[j]
        j=j+1
    i=i+1
print(sum)

	# d=a[0]+b[0]
	# k=a[1]+b[1]
	# j=a[2]+b[2]
	# r=a[3]+b[3]
	
	# i=i+1
	# print(d,k,j,r)