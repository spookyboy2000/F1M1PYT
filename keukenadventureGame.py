# Setup
yes_no = ["ja", "nee"]
directions = ["left", "right", "forward", "backward"]
 
# Introduction
name = input("Wat is je naam?\n:")
print("Goedemorgen, " + name + ". Laten we eens bekijken hoe jij leeft.")
print("Je wordt wakker..")
print("Wat doe je?\n")
 
# Start of game
response = ""
while response not in directions:
    response = input("wakker woorden / blijven slapen\n:")
    if response == "wakker woorden":
        print("Je wordt wakker.\n")
        break
    elif response == "blijven slapen":
        print("Je blijft slapen. vaarwel, " + name + ".")
        quit()
    else:
        print("Vekeerde Input.\n")
 
# Next part of game
response = ""
while response not in directions:
    response = input("Waar will je heen?\nbadkamer/naar beneden\n:")
    if response == "badkamer":
        print("Je loopt naar de bad kamer.\n")
        break
    elif response == "naar beneden":
        print("Je loopt naar beneden.\n")
        break
    else:
        print("Vekeerde Input.\n")

#Next part
response = ""
while response not in directions:
    response = input("Wat doe je?\nde keuken in/schoenen aan doen/naar de wc\n:")
    if response == "de keuken in":
        print("Je loopt naar de keuken.\n")
        response = input("Wat doe je in de keuken?\nbrood pakken/magnetron eten/yoghurt\n:")
        if response == "brood pakken":
            print("Je pakt brood.\n")
            break
#------------------------------------------------------------------------------------------------------------------------
        elif response == "magnetron eten":
            print("Je Doet kantenklaar eten in de magnetron.\n")
            break
#------------------------------------------------------------------------------------------------------------------------
        elif response == "yoghurt":
            print("Je pakt een bak met yoghurt.\n")
            break
#------------------------------------------------------------------------------------------------------------------------
        else:
            print("Vekeerde Input.\n")
#------------------------------------------------------------------------------------------------------------------------    
    elif response == "schoenen aan doen":
        print("Je loopt naar beneden.\n")
        response = input("wat doe je na dat je je schoenen hebt aan gedaan?\nnaar de keuken/naar de wc")
        if response == "naar de keuken":
            print("Je loopt naar de keuken.")
            break
#------------------------------------------------------------------------------------------------------------------------
    elif response == "naar de wc":
        print("Je gaat naar de wc.\n")
        break
#------------------------------------------------------------------------------------------------------------------------
    else:
        print("Vekeerde Input.\n")
#------------------------------------------------------------------------------------------------------------------------
