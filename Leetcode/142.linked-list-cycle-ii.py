class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        crawl = head
        run = head
        head_count = True
        while crawl and run and run.next:
            #            print("crawl, run", crawl.val, run.val)
            if crawl == run and not head_count:
                entry = head
                # entry.next=head
                pos = -1
                #               print(entry.val, crawl.val)
                while entry != crawl:
                    crawl = crawl.next
                    entry = entry.next
                    pos += 1
                return entry

            crawl = crawl.next
            run = run.next.next
            head_count = False
        return None


z = Solution()
a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(4)
# e = ListNode(5)
a.next = b
# b.next = c
# c.next = d
# d.next = b
# e.next = c
#
#
print(z.detectCycle(a))
