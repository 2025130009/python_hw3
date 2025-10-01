pw="Aerospace"
count=1
a=input()

while count<5 and a !=pw:
    print("Check again")
    count+=1
    a=input()
if a == pw:
    print("LOGIN")
else:
    print("Fail")
