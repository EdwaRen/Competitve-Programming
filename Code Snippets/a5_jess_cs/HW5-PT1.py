## source code ##

import re
def open_file():   ##method to open a file
    while(True):
        text = input("Enter the file Name\n")
        file = open(text, 'r')
        if not file.closed:   ##checking if the file is opened
            return file
        else:
            print("File name/path is wrong")

def get_alpha(str):    ## method to get only alphabetic char
    validLetters = "abcdefghijklmnopqrstuvwxyz"
    newString = ""
    for char in str:
        if char in validLetters:
            newString += char
    return newString


def read_data(fp):
    lines = fp.readlines()  ## reading the file line by line
    data_dict = {}
    line_cnt = 1
    for line in lines:
        line = line.lower()
        words = line.split()
        ##regex = re.compile('[^a-zA-Z]')

        for word in words:
            ##print word
            word = get_alpha(word)  ##removing all non alphabetic char from the word
            if len(word) <=1:
                continue
            if not word.isalpha():
                continue
            ##print word
            if word in data_dict and line_cnt not in data_dict.get(word):    ## checking if the key is already there in the dictonary
               ## print data_dict.get(word)
                data_dict[word] = data_dict.get(word).union(set([line_cnt]))
            else:                              ## adding word to the dictonary
                data_dict[word] = set([line_cnt])
            ##print data_dict
        line_cnt = line_cnt + 1
   ## print data_dict
    return data_dict

def find_cooccurance(D, inp_str):
    words = inp_str.split()
    if len(words) == 0 or len(get_alpha(words[0].lower())) <= 1:
        print('Word " is not in file')
        return
        
    word_set = D.get(get_alpha(words[0].lower())) or set([])
    for word in words:
        ##print word
        ##print D.get(word)
        parse_word = get_alpha(word.lower())
        print("parsed word", parse_word)
        if parse_word in D:
            # print("parsed word", D.get(parse_word) )
            word_set = word_set & D.get(parse_word)  ##intersection to get common line
        else:
            print('Word ' + word + ' is not in file')
        ##print set
    if len(word_set) != 0:
        print (*list(word_set), sep=' ')


def main():
    file = open_file()
    D = read_data(file)
    while(True):
        text=input("Enter the space separated word\n")
        find_cooccurance(D,text)
        msg = input("Enter Q\q to quit\nAny other key to continue")
        if msg == "q" or msg == "Q":
            break

if __name__ == "__main__":
    main()
## Sample output ##

# C:\Python27\python.exe C:/Users/Samsung/PycharmProjects/untitled/dict_problem.py
# Enter the file Name
# scam_phone_nos.txt
# Enter the space separated word
# true knowledge imagination
# set([3])
# Enter Q\q to quit
# Any other key to continue
# Enter the space separated word
# is the
# set([3, 7])
# Enter Q\q to quit
# Any other key to continue
