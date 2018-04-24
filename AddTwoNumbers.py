#https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        start = mylist = ListNode(0)

        next1 = l1
        next2 = l2
        carry = 0

        while (next1 or next2 or carry):

            val1 = val2 = 0
            if next1:
                val1 = next1.val
                next1 = next1.next
            if next2:
                val2 = next2.val
                next2 = next2.next

            tot = val1 + val2 + carry

            if tot > 9:
                tot = tot % 10
                carry = 1
            else:
                carry = 0

            mylist.next = ListNode(tot)
            mylist = mylist.next

        return start.next


