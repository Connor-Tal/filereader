import time

file = open(r"file name","r+")
line = 0
keyword = input("What word are you searching for?")
content = file.readlines()
while True:
    try:
        print(content[line])
        if content[line].__contains__(keyword):
            print("keyword found!", keyword)
            file.close()
            break
        time.sleep(0.25)
        line += 1
    except:
        print("you ran out of lines and no word was found")
        exit()