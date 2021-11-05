from slowprint.slowprint import *
slowprint("Je bent aan het schuilen op een geheime plek in syrie en je ligt op een bed. Je hoort stemmen van mensen die je nog niet eerder gehoordt hebt wat doe je?", 0.45)
answer2 = input('a)je blijft liggen.\nb)je gaat naar buiten.\n:')
if answer2.lower() == "b" or answer2.lower() == "2":   
    slowprint("Je slaat een raampje in en verwijdert zorgvuldig het glas. Je ziet twee mensen in een rood pak wat doe je?", 0.45)
elif answer2.lower() == "a" or answer2.lower() == "1":
    slowprint("Je blijft liggen maar daardoor wordt je geambushed en wordt je meegenemon door de vijand.", 0.45)
    quit()

answer2 = input('a)Confront ze.\nb)probeer weg tekomen doorw on opgemerkt naar buiten tegaan.\n:')
if answer2.lower() == "b" or answer2.lower() == "2":
    slowprint("Je kruipt een kelder in en ontsnapt naar buiten en komt wat mede burgers tegen. wat ga je met ze doen?", 0.45)
elif answer2.lower() == "a" or answer2.lower() == "1":
    slowprint("je confront ze en je vraagt wat ze hier doen je ziet hun emblem en beseft dat ze van de overheid zijn. zij merken dat je ze door hebt en steken je met een mes waardoor je knockout valt.", 0.45)
    quit()

answer2 = input('a)Je rent met je mede burgers over een felt om naar meer burgers te komen.\nb)Je offert jezelf op om avleiding te creën zodat je mede burgers kunnen vluchten.\n:')
if answer2.lower() == "a" or answer2.lower() == "1":   
    slowprint("Tijdens het rennen merk je dat er vliegtuigen aan komen die ineens bommen laat vallen en je hoort dat er 1 erg dicht bij komt je gaat op de grond liggen in de hoop dat je niet geraakt wordt. Je overleeft maar je mede burgers waar je mee was zijn opgeblazen in de explosie. wat doe je?", 0.45)
elif answer2.lower() == "b" or answer2.lower() == "2":
    slowprint("Je creërd afleiding maar merkt dat het niet genoeg was en de burgers en jij zelf worden in een cell gestopt.", 0.45) 
    quit()

answer2 = input('a)je rent terug om te kijken of er nog 1 leeft.\nb)Je rent door.\n:')
if answer2.lower() == "b" or answer2.lower() == "2":
    slowprint("Je komt een nieuwe groep burgers tegen om mee te travellen. wat ga je met ze doen?", 0.45)
elif answer2.lower() == "a" or answer2.lower() == "1":
    slowprint("Je rent terug en een sniper ziet je en je wordt geraakt waardoor je wordt megenomen door wat burgers en het schijnt dat je door dat schot niet veel meer kan doen en je niet meer kan vluchten.", 0.45)
    quit()

answer2 = input('a)Je gaat met ze vlugten om hopelijk een veilig leven te krijgen.\nb)je blijft vechten voor het land.\n:')
if answer2.lower() == "a" or answer2.lower() == "1":
    slowprint("je gaat vluchten richting turkije en onderweg vinden jullie wat wapens van doodgeschoten soldaten. maar terwijl jullie de wapens op pakken komen jullie een groep soldaten tegen, wat doe je?", 0.45)
    answer2 = input('a)je gaat proberen ze te vermoorden met de wapens die je hebt gevonden.\nb)je gaat schuilen.\n:')
    if answer2.lower() == "a" or answer2.lower() == "1":
        slowprint("je vermoordt het groepje soldaten maar verliest 3/5 van de mensen in de groep. jullie maken een nieuw plan en zijn met het plan gekomen om naar.", 0.45)
        answer2 = input('a)je vlucht verder richting turkije.\nb)vecht verder omdat je weet dat vluchten het niet wordt.\n:')
        if answer2.lower() == "a" or answer2.lower() == "1":
            slowprint("uit eindelijk kom je eindelijk bij de grens in turkije hoe ga je langs de grens komen", 0.45)
            answer2 = input('a)je rent door de grens heen in de hoop dat je niet gepakt wordt.\nb)je gaat omlopen om over de grens heen te gaan (onopgemerkt).\n:')
            if answer2.lower() == "a" or answer2.lower() == "1":
                slowprint("je rent door de grens en je struikelt waardoor je wordt opgepakt en de cell in gaat.", 0.45)
                quit()
            elif answer2.lower() == "b" or answer2.lower() == "2":
                slowprint("je gaat on opgemerkt over de grens heen en je bent nu officieel in turkije wat is de volgende stap die je neemt?", 0.45)
                answer2 = input('a)je gaat verder naar de kust.\nb)je gaat proberen een goed veilig leven te krijgen in turkije.\n:')
                if answer2.lower() == "a" or answer2.lower() == "1":
                    slowprint("terwijl je naar de kust gaat kom je wat mensen tegen en je leert die kennen. uiteindelijk schijnen ze heel erg aardig tezijn en biedden ze je aan om je naar nederland te brengen wat zeg je?", 0.45)
                    answer2 = input('a)ja dat zou ik heel erg fijn vinden!\nb)nee ik zal proberen hier verder te gaan met mijn leven.\n:')
                    if answer2.lower() == "a" or answer2.lower() == "1":
                        slowprint("je gaat met de mensen mee naar nederland en vindt daar een gelukkig leven met een vrouw kinderen en een baan.", 0.45)
                        slowprint("THE-END", 0.6)
                    elif answer2.lower() == "b" or answer2.lower() == "2":
                        slowprint("je vindt een mooie plek in turkije en bouwt je beroep daar op en leeft goed en gelukkig.", 0.45)
                        quit()    
                elif answer2.lower() == "b" or answer2.lower() == "2":
                    slowprint("je vindt een mooie plek in turkije en bouwt je beroep daar op en leeft goed en gelukkig.", 0.45)
                    quit()
        elif answer2.lower() == "b" or answer2.lower() == "1":
            slowprint("je vecht verder.", 0.45)
            quit()
    elif answer2.lower() == "b" or answer2.lower() == "2":
        slowprint("je schuilt maar de groep soldaten komen steeds meer jullie kant op. wat wordt het volgende wat jullie doen?", 0.45)
        answer2 = input('a)je gaat een andere kant op.\nb)je vlucht verder.\n:')
        if answer2.lower() == "a" or answer2.lower() == "1":
            slowprint("je gaat een andere kant op en komt uiteindelijk bij de grens van lebanon en gaat verder lopen naar de zee. je komt aan bij de zee en je komt bij een persoon op de boot die je naar europa brengt. je komt uiteindelijk op een hele andere plek dan europa aan je beland in mexico en leeft daar verder.", 0.45)
            quit()
        elif answer2.lower() == "b" or answer2.lower() == "2":
            slowprint("je vlucht verder en raakt uit voedsel je overleeft het niet.", 0.45)
            quit()
elif answer2.lower() == "b" or answer2.lower() == "2":
    slowprint("Je vecht met de mede burgers voor het land. wat doe je?", 0.45)
    answer2 = input('a)je wordt de leider van je eigen groep soldaten en vecht tot het einde.\nb)je komt je vader tegen op het slachtveld en probeert hem te helpen.\n:')
    if answer2.lower() == "a" or answer2.lower() == "1":
        slowprint("je wordt leider van een groep en zorgt ervoor dat er weer rust is in syrië. en nu zijn jullie van plan om in meer landen te helpen met rust krijgen.", 0.45)
        quit()
    elif answer2.lower() == "b" or answer2.lower() == "2":
        slowprint("je helpt je vader maar uit eindelijk gaat hij dood en je wordt meegenomen door de vijand.", 0.45)
        quit()
