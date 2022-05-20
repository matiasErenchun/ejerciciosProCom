s = "((()))"
pila=[]
continuar=True
i=0
while(continuar and i<len(s)):
    signo=s[i]
    if(signo=='(' or signo=='[' or signo=='{'):
        pila.append(signo)
    else:
        if(len(pila)==0):
            continuar=False
        else:
            otrosigno=pila.pop()
            if((signo==')' and otrosigno=='(')):
                continuar=True
            elif((signo==']' and otrosigno=='[')):
                continuar = True
            elif((signo=='}' and otrosigno=='{')):
                continuar = True
            else:
                continuar=False
    i+=1
if(len(pila)>0):
    continuar=False
print(continuar)
