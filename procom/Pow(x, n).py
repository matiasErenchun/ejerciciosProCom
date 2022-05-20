'''
intento 1
x = 2.00000
n = 11

newX=x*x
acumulador=1
if(n%2==0):
    unomas=False
else:
    unomas=True
n=(n/2)
i=1
print(n, acumulador)
if(n<0):
    n=n*-1
    x=1/x
while(i<=n):
    acumulador=acumulador*newX
    i+=1
if(unomas):
    acumulador=acumulador*x
print(acumulador)
'''

#no suelo usar recursion pero en estos casos termina siendo la mejor respuesta
#https://www.youtube.com/watch?v=snOaKR2xgZg
def double_pow(x, n):
    if(n==0):
        return 1.0
    if(n==1):
        return x
    if(n<0):
        return double_pow(1/x, -n)
    resultado =double_pow(x*x, int(n/2))#<--
    #en esta parte es cuando se produce la magia ya se duplica el x y se reduce el n
    #usando la propiedad de las potencias X**n <=> (x**2)**n/2 en cada iterasion
    if(n%2):
        resultado*=x
    return resultado

x = 2.00000
n = 10

print(double_pow(x,n))