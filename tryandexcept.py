run = True
while run == True:
    try:
        mark = int(input('mark'))
    except:
        print("number please")
    else:  
        run = False
        if mark == 1:
            print("yes")
        else:
            print("no")
    