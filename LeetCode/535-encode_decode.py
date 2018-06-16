import random

class Codec:
    mappings = {}
    count = 0;

    def randomURL(self):
        url=""
        for x in range(6):
            url+= str(random.randint(0, 9))
        return str(url)
    def encode(self, longUrl):
        my_url = self.randomURL()
        while my_url in self.mappings:
            my_url = self.randomURL
        self.mappings[my_url] = longUrl
        return my_url

    def decode(self, shortUrl):
        return self.mappings[shortUrl]


codec = Codec()
print(codec.decode(codec.encode("HELLO")))
