def main():
    raw_input = input("Please input a list of numbers seperated by a space: ")
    longest_run(raw_input.split())

def longest_run(numSet):
    max_run = 0
    cur_run = 1

    for i in range (1,len(numSet)):

        if(float(numSet[i-1]) == float(numSet[i])):
            cur_run +=1
        else:
            if(cur_run > max_run):
                max_run = cur_run
            cur_run = 1
    
    if(len(numSet) == 0):
        print(0)
        return

    if(cur_run > max_run):
        max_run = cur_run
    
    print(max_run)

main() 