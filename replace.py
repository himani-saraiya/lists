mainstr="the quick brown fox jumped over the lazy dog .the dog slept over the varndha"
substr="over"
list=mainstr.split( )
a=" "
r=" on"
i=0
while i<len(list):
	if list[i]==substr:
		a=a+r+" "
	else:
		a=a+list[i]+" "
	i=i+1
print(a)
