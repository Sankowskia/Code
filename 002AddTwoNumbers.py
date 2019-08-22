# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        f=0
        head=l1
        pre=l1
        while l1 and l2:
            l1.val+=l2.val+f
            if l1.val>=10:
                f=1
                l1.val%=10
            else:
                f=0
            pre=l1
            l1=l1.next
            l2=l2.next
        if l1:
            while f>0 and l1:
                if l1.val+f>=10:
                    f=1
                    l1.val=0
                else:
                    l1.val+=f
                    f=0
                pre=l1
                l1=l1.next
            if f==1:
                pre.next=ListNode(1)
        elif l2:
            pre.next=l2
            while f>0 and l2:
                if l2.val+f>=10:
                    f=1
                    l2.val=0
                else:
                    l2.val+=f
                    f=0
                pre=l2
                l2=l2.next
            if f==1:
                pre.next=ListNode(1)
        else:
            if f==1:
                pre.next=ListNode(1)
        return head 