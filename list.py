a=[50,40,23,70,56,12,5,10,75]
i=0
max=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    i=i+1
print(max)
j=0
smax=0
while j<len(a):
    if a[j]<max:
        if a[j]>smax:
            smax=a[j]
    j=j+1
print(smax)
k=0
tmax=0
while k<len(a):
    if a[k]<smax:
        if a[k]>tmax:
            tmax=a[k]
    k=k+1
print(tmax)