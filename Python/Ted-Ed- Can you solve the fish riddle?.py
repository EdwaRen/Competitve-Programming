for i in range(8):
    for j in range(1, 8):
        n = (50-6-j)%(6+i)
        if n == 0:
            print("n is now 0", i, j)
        
