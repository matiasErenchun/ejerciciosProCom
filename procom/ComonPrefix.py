from typing import List

strs = ["flower","flow","flight"]

def longestCommonPrefix(strs: List[str]) -> str:
    s = strs
    respuesta = ""
    i = 0
    continuar = True
    while (continuar):
        if (len(s[0]) > 0 and i < len(s[0])):
            valor = s[0][i]
            for palabra in s:
                if i < len(palabra):
                    if valor != palabra[i]:
                        continuar = False
                else:
                    continuar = False
            if (continuar == True):
                respuesta += valor
            i += 1
        else:
            continuar = False
    return respuesta

print(longestCommonPrefix(strs))