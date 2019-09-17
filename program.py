# start
vaken = "n"
print ("du har käkat för mycket muskot...")
while vaken == "n":
    vaken = input("har du vaknat [y/n]:")



print (" gå och duscha du luktar skunk. ")

print ("någon har lämnat en brödrost i duschen ")

duscha = input("flyttar du på brödrosten? [y/n]")

if duscha == "n":
    print("du elchockas och ditt äventyr har nått sitt slut")
    exit()

elif duscha == "y":
    print ("friskt vatten sköljer över dig, och du vaknar sakta up")
else: 
    print("does not compute") 

season = False
while season == False: 
    season = input("vilken årstid är der? [vår, vinter, höst, sommar]")
    if season == "vår" or season == "vinter" or season == "höst":
        print("det är kallt och slask fy tusan!")
        print("du klär på dig vinterpälsen...")
    elif season == "sommar":
        print("sommar! slides och shorts")
    else:
        season = False 






