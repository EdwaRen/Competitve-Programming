import collections 

def longest_run(run_input):
    count_map = collections.defaultdict(int)
    parsed_input = run_input.strip().split()
    for num in parsed_input:
        count_map[num]+=1

    most_common_num = 0
    for key, value in count_map.items():
        if value >= most_common_num:
            most_common_num = value 
    return most_common_num

run_input = input("Please enter your run that is space separated \n")
longest = longest_run(run_input)
print("The longest run is of length ", longest)