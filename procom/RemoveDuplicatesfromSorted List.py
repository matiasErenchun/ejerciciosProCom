class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


nodo3 = ListNode(3, None)
nodo2 = ListNode(2, nodo3)
nodo1 = ListNode(1, nodo2)
nodo0 = ListNode(1, nodo1)

diccionario ={}
head = nodo0
continuar=0
while(continuar<3):
    print(head.next)
    if(head.next==None):
        #continuar=False
        print("hola")
    diccionario[str(head.val)]=head.val
    head=head.next
    print(head.val)
    continuar+=1
salida =[]
for j in diccionario.keys():
    salida.append(diccionario.get(j))
print(salida)