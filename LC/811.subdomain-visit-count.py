import collections

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        
        # Handle edge case
        if not cpdomains or len(cpdomains) == 0:
            return None

        # Create hashtable with each domain
        domain_map = collections.defaultdict(int)

        # Iterate through all domains
        for i in cpdomains:
            num, domain = i.split()
            domain_list = domain
            domain_map[domain_list] += int(num)

            while (len(domain_list.split('.')) > 1):
                domain_list = domain_list.split('.', 1)
                domain_map[domain_list[1]] += int(num)
                domain_list = domain_list[1] 
        res = [ str(val) + " " + str(key) for key, val in domain_map.items() ]
        return res

z = Solution()
cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
sol = z.subdomainVisits(cpdomains)
print(sol)


        
