a=[1,2,3,4,5]
b=[6,3,5,9]
i=0
c=[]
while i<len(a):
    if a[i] in b:
        c.append(a[i])
    i=i+1
print(c)