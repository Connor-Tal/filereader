import time

file = open(r"file name","r+")
content = file.readlines()
line = 0
wordcount = 0

keyword = input("What word are you searching for?")
while True:
    try:
        if content[line].__contains__(keyword):
            wordcount += 1
            print("The word you are looking for is on line:", line + 1)
            print ("This is the line:", content[line])
            time.sleep(1)
            line += 1
        else:    
            line += 1
    except:
        if wordcount == 0:
            print("The word you were looking for is not in the file")
            exit()
        else:
            print("There were a total of", wordcount,"words in the document")
            file.close()
            exit()