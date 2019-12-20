import collections

class Solution(object):

    def find(self, parents, loc):
        if parents[loc] != loc:
            parents[loc] = parents[parents[loc]]
            return self.find(parents, parents[loc])
        return loc 

    def union(self, parents, loc1, loc2):
        rootA = self.find(parents, loc1)
        rootB = self.find(parents, loc2)

        parents[rootA] = rootB


    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        parents = [i for i in range(10001)]
        email_id = collections.defaultdict(int)
        email_name = collections.defaultdict(str)
        ans = collections.defaultdict(list)

        for index in range(len(accounts)):
            acc = accounts[index]
            
            for email in acc[1::]:
                email_name[email] = acc[0]
                if email not in email_id:
                    email_id[email] = index
                self.union(parents, email_id[acc[1]], email_id[email])
        
        for email, ident in email_id.items():
            ans[self.find(parents, ident)].append(email)

        return [ [ email_name[value[0]]] + sorted(value) for key, value in ans.items()]
   

z = Solution() 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
res = z.accountsMerge(accounts)
print(res)

