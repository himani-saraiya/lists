mainstr="the quick brown fox jumped over the lazy dog .the dog slept over the varndha"
substr="over"
list=mainstr.split( )
i=0
a=" "
while i<len(list):
	if list[i]==substr:
		pass
	else:
		a=a+list[i]+" "
	i=i+1
print(a)