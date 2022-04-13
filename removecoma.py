s=["sai,priya","deepa,patel"]
i=0
l=[]
while i <len(s):
    if "," in s[i]:
        h=s[i].replace(",","")
        l.append(h)
    i=i+1
print(l)