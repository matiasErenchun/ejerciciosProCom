class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class Solution:

    nodo3 = ListNode(3, None)
    nodo2 = ListNode(2, nodo3)
    nodo1 = ListNode(1, nodo2)
    nodo0 = ListNode(1, nodo1)

    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head