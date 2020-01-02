username = ["joe","joe","joe","james","james"]
timestamp = [1,2,3,4,5]
website = ["cart","maps","home","home","cart"]

# Using Zip will combine the three lists
for user, time, web in zip(username, timestamp, website):
    print(user, time, web)

# Zip can be used to rotate lists
r = [(1, 4), (2, 5), (3, 6)] # => [(1, 2, 3), (4, 5, 6)]
rotate = zip(*r)
print("\nRotate list, original: ", r)
for i in rotate:
    print(i, end=' ')

print("\nPopping from website")
print("---")
website.pop()
website.pop()

# Will only go until the shortest list
for user, time, web in zip(username, timestamp, website):
    print(user, time, web)
