def oddNumbers(l, r):
    for i in range(l, r+1, 2):
        if i % 2 == 1:
            print(i)

oddNumbers(1, 4)