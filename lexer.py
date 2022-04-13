a=[9,8,[5,[3],[7]]]
i=0
b=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            if type(a[i][j])==list:
                k=0
                c=0
                while k<len(a[i][j]):
                    print(a[i][j][k])
                    k=k+1
            print(print(a[i][j]))
            j=j+1
    print(a[i])
    i=i+1
