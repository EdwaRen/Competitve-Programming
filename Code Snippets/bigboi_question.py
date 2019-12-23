import random

def performTest(): 
    ## complete your work here ##
    # Ask a question
    def askQuestion(operation):

        """DEFINE OP_STRING AND PO_STRING HERE"""
        op_string = ""
        if operation:
            op_string = "multiply"
        else:
            op_string = 'add'

        # Generate the random numbers
        a = random.randint(0, 9)
        b = random.randint(0, 9)

        ans = input("Please " + op_string + " these two numbers and enter your result below: " + str(a) + ', ' + str(b))
        
        if (operation) and (int(ans) == a * b):
            print("Correct! You rightly answered ", a * b)
            return True
        elif (not operation) and (int(ans) == a + b):
            print("Correct! You rightly answered ", a + b)
            return True
        else:
            if operation:
                correctAnswer = a * b 
            else:
                correctAnswer = a + b
            print("Wrong, the correct answer is ", correctAnswer)
            return False

    # Initiate test and track question results
    correctCounts = 0
    for i in range(10):

        """DEFINE OPERATION HERE"""
        operation = random.randint(0, 1)

        question = askQuestion(operation)
        if question:
            correctCounts +=1

    return correctCounts

print("This software tests you with 10 questions  ")

correctCounts = performTest()

if correctCounts <= 6 :
  print("Please ask your teacher for help.")
else:
  print("Congratulations!")