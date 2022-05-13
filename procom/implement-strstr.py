haystack = "hello"
needle = "ll"
i=0
while i<len(haystack):
    j=0
    k=i
    while k<len(haystack) and j<len(needle) and haystack[k]==needle[j]:
        j+=1
        k+=1
    if(j==len(needle)):
        break
    else:
        i+=1
print(i)