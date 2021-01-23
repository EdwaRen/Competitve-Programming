class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.cur_page = 0
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.history = self.history[:self.cur_page+1]
        self.history.append(url)
        self.cur_page+=1
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.cur_page = max(self.cur_page-steps, 0)
        return self.history[self.cur_page]
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.cur_page = min(len(self.history)-1, self.cur_page+steps)
        return self.history[self.cur_page]

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

z = BrowserHistory("leetcode.com")
z.visit("google.com")
z.visit("facebook.com")
z.visit("youtube.com")
print(z.back(1))
print(z.back(1))
print(z.forward(1))
z.visit("linkedin.com")
print(z.forward(2))
print(z.back(2))
print(z.back(7))


