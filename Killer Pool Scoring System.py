# Killer Pool Scoring System

numOfPlayers = int(input("How many players are playing..."))
allPlayers = []
for i in range(numOfPlayers):
    onePlayer = input("Enter player names and press enter between each one...").title()
    allPlayers.append([onePlayer, 3])

print ("\nThis round of killer pool will be played by...")
print ("Player,Lives")
for name in allPlayers:
    print (name)

while len(allPlayers) > 1:
    for name in allPlayers:
        print ("It is",name[0]+"'s turn.")
        shot = input("Did the player (p)ot or (m)iss... ")
        if shot == "m":
            name[1] -= 1
            if name[1] == 0:
                print (name[0], "has 0 lives left and is out of the game!")
                del allPlayers[name]#problem here
        else:
            print ("Well done!")

    print ("After this round. Here are the lives remaining...")
    for name in allPlayers:
        print (name)        
