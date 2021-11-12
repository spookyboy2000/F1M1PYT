running = True
while running == True:
    antwoord = input("Type hier een zin:  ")
    user = antwoord.split()
    for x in user:
        if len(x) >3:
            print(x[0:2]+"...", x[0:2]+"..." ,x)
        else:
            print(x)