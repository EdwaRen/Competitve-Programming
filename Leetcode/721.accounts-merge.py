import collections

class Solution(object):
    def find(self, parents, email):
        if parents[email] != email:
            parents[email] = self.find(parents, parents[email])
        return parents[email]
    
    def union(self, parents, email_a, email_b):
        parents[self.find(parents, email_a)] = self.find(parents, email_b)
    
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        Union find solution to link two disjoint sets in ~O(1)
        """
        parents = collections.defaultdict(str)
        email_to_name = collections.defaultdict(str)
        for i in range(len(accounts)):
            user_acc = accounts[i]
            for acc in user_acc[1:]:
                email_to_name[acc] = user_acc[0]
                if acc not in parents: parents[acc] = acc
                self.union(parents, acc, user_acc[1])
                
        linked_emails = collections.defaultdict(list)
        for email in parents.keys():
            linked_emails[self.find(parents, email)].append(email)
            
        return [[email_to_name[email]] + sorted(others) for email, others in linked_emails.iteritems()]
        
        