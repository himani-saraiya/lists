l=["a","bc","abc","de","xy"]
i=0
max=0
k=0
while i<len(l):
    len(l[i])>max
    max=len(l[i])
    i+=1
print(max)
j=0
smax=0
c=0
while j<len(l):
    if len(l[j])==max:
        smax=len(l[j])
        c=c+1
        p=l[j]
    j+=1
print(c)
print(max**c)
