#toekennen (assignment) =
#optellen (addition) +
#aftrekken (subtraction) -
#keer (multiply) *
#delen (divide) /
#restwaarde (modulo) %
#optellen bij waarde van variabele +=
#delen door waarde van variabele /=

getal1 = 10
getal2 = 21
getal3 = 3
getal4 = 19

#operation 1 
print(getal1 * getal1)
#operation 2 
print(getal1)
#operation 2 
print(getal1 + getal1)
getal1 += getal1
print(getal1)
#operation 2 
print(getal2 - getal1)
#operation 1 
print(getal2 / getal1)
getal2 /= getal2
print(getal2)
#operation 2 
print(getal2 % getal1)


first_name = input("Geef je voornaam\t:")
last_name = input("Geef je achternaam\t:")
print("Geef uw massa in kilogram: ")
massa_kg = int(input())
print("Geef uw lengte in meter: ")
lengte_m = float(input())
bmi = massa_kg / (lengte_m * lengte_m)
print("Uw BMI bedraagt: " + str(bmi) + ".")