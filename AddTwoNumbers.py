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
        carry = 0
        while(next1 != None and next2 != None):
            sum = curr1 + curr2 + carry
            if sum >9:
                sumA.insert(0,sum %10)
                carry = 1
            else:
                sumA.insert(0,sum)
                carry = 0
            next1 = curr1.next
            next2 = curr2.next
            #at the end of the while loop one of the lists has hit an end, so we add the remaining digits in the other list
            if next2 == None:
                    while(next1 != None):
                        sumA.insert(0, next1)
                        next1 = curr1.next
            else:#either the next1 or the next 2 is ended
                    while(next2 != None):
                        sumA.insert(0, next2)
                        next2 = curr2.next

