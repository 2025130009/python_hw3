pw = "Aerospace"
tries = 5
att = 0

while att < tries:
    a=input()
    
    if a == pw:
        print("LOGIN")
        
    else:
        att += 1
        if att < tries:
            print("Check again")
        else:
            print("Fail")
            exit()
