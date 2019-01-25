# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Runner starts n steps ahead of crawler, then both go at the same speed
        crawler = head
        runner = head

        # Handle edge case
        if not head:
            return None

        # Make Runner n steps ahead of crawler in linkedlist
        for i in range(n):
            if runner:
                runner = runner.next
            else:
                return crawler.next

        # Handle edge case where n = lenght of linkedlist
        if not runner:
            return head.next

        # if runner hits None, then crawler skips the node in front of it
        while runner:
            if not runner.next:
                if crawler.next:
                    crawler.next = crawler.next.next
                else:
                    crawler.next = None

                # return head of linkedlist
                return head

            # Update crawler and runner values so they are always n distance apart
            crawler = crawler.next
            runner = runner.next
        return head

    def removeNthFromEnd_old(self, head, n):

        cur = head
        while cur is not None:
            cur_inner = cur.next
            for i in range(n+1):
                # # print("cur ", cur.val, cur_inner,  i)
                # if cur_inner:
                #     # print("cur ", cur.val, cur_inner.val,  i)
                # else:
                #     # print("cur ", cur.val,  i)

                if not cur_inner and i == n:
                    if cur.next and cur.next.next:
                        cur.next = cur.next.next
                    else:
                        cur.next = None
                    return head
                elif not cur_inner:
                    return cur.next
                else:
                    cur_inner = cur_inner.next
            cur = cur.next
        return head

# z = Solution()
# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(3)
# d = ListNode(4)
# e = ListNode(5)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# res = z.removeNthFromEnd(a, 1)
#
# while res is not None:
#     print(res.val)
#     res = res.next
#
