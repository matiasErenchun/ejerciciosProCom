import re

str = "A man, 9a plan, a canal: Pa9nama"
str=str.lower()
expresion = re.compile(r'[0-9a-zA-Z]*')
p = expresion.findall(str)
cadenafinal=""
for cade in p:
    if len(cade)>0:
        cadenafinal+=cade
print(cadenafinal)
i=0
j=len(cadenafinal)-1
palindromo=True
while(j>i):
    if(cadenafinal[i]!=cadenafinal[j]):
        palindromo=False
        j=0
    j-=1
    i+=1
print(palindromo)