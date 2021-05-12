import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
         
        front = []
        count = 0
        for l in lists:
            if l:
                count += 1
                heapq.heappush(front, (l.val, count, l))
        
        head = prev = ListNode(0)
        while front:
            _, _, cur = heapq.heappop(front)
            prev.next = cur 
            prev = cur
            if cur.next:
                count += 1
                heapq.heappush(front, (cur.next.val, count, cur.next))
        
        return head.next

def printList(list):
    while list:
        print(list.val)
        list = list.next

    # def mergeKLists(self, lists):
    #     amount = len(lists)
    #     interval = 1
    #     while interval < amount:
    #         for i in range(0, amount - interval, interval * 2):
    #             lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
    #         interval *= 2
    #     return lists[0] if amount > 0 else lists

    # def mergeTwoLists(self, list1, list2):
    #     a = list1
    #     b = list2
    #     c = d = ListNode(0)
    #     while not (a== None and b == None):
    #         if a == None:
    #             c.next = b
    #             b = b.next
    #         elif b == None:
    #             c.next = a
    #             a = a.next
    #         else:
    #             if a.val < b.val:
    #                 c.next = a
    #                 a = a.next
    #             else:
    #                 c.next = b
    #                 b = b.next
    #         c=c.next

    #     # self.printList(d.next)
    #     return d.next
    #     pass


a = Solution()
b = ListNode(1)
b.next = ListNode(4)
b.next.next = ListNode(5)
c = ListNode(1)
c.next = ListNode(3)
c.next.next = ListNode(4)
d = ListNode(2)
d.next = ListNode(6)
# a.mergeKLists([b, c, d])

printList(a.mergeKLists([b, c, d]))