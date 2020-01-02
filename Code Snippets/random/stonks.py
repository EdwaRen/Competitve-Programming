def interest(rate):
    roi = 1
    years = 0
    while roi < 2:
        roi *= (1+rate)
        years += 1
    return years

interest_rate = float(input("Please enter your interest rate greater than 0\n"))
years = interest(interest_rate) 
print("it would take " + str(years) + " years to double your investment")