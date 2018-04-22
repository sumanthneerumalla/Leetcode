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
        curr1 = l1
        curr2 = l2
        next1 = l1.next
        next2 = l2.next
        sumA = []
        while(next1 != None and next2 != None):
            sum = curr1 + curr2
            if sum >9:
                sumA.insert(0,sum %10)


