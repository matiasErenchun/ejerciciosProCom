n = -1
x=2
es=False
if(n==1):
    es=True
if(n<0):
    x=x/2
    n=n*-1
else:
    acumularod=1
    i=1
    while(acumularod<n and i<=31):
        acumularod=acumularod*x
        if(acumularod==n):
            es=True
        i+=1
print(es)



