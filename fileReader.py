import time

line = 0
wordcount = 0
file = open('text.txt', 'r')
data = file.read()
original = file.read()
keep = input('Do you want to keep to keep the original format (y)? Or have the program make a new line after each space (n)? (y/n)')
if keep == 'y':
    print('original data kept')
if keep == 'n':
    data = data.replace('.', '.\n')
    file.close()
    file = open('text.txt', 'w')
    file.write(' ')
    file.write(data)
    file.close()

keyword = input("What word are you searching for?")

while True:
    try:
        with open('text.txt',"r") as file:
            content = file.readlines()
            if content[line].__contains__(keyword):
                wordcount += 1
                print(f"The word you are looking for is on line: {line + 1}")
                print (f"This is the line: {content[line]}")
                time.sleep(1)
                line += 1
            else:    
                line += 1
    except:
        if wordcount == 0:
            print("The word you were looking for is not in the file")
            file.close()
            exit()
        else:
            print(f"There were a total of the {wordcount} of the words you were looking for in the document")
            file.close()
            exit()