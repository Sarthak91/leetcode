class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = 3
    l1.val =3
    l1.next =4
    l1.val =4
    l1.next = None
    while l1.next != None:
        print(l1.val)
        