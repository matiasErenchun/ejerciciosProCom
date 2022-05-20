digits = [1,9]
i=len(digits)-1
continuar=True
while(continuar and i>=0):
    if(digits[i]+1<=9):
        digits[i]=digits[i]+1
        continuar=False
    else:
        digits[i]=0
        i-=1
if(continuar):
    digits=[1]+digits
print(digits)