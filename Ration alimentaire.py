# Objectif de ce programme.

# J'ai décidé d'écrire ce programme car en 3éme année science, j'ai un chapitre (avec des exercices) ou on doit
# calculer l'apport énergétique d'individu et voir est-ce-qu'elle respecte le régle GPL ou non.
# Ce programme est désigné pour faire ce travail en quelque seconds.

glucides = float(input("Entrer le total de glucides consommés en (g): "))
protides = float(input("Entrer le total de protides consommés (g): "))
lipides = float(input("Entrer le total de lipides consommés (g): "))
breakfast = glucides*4 + protides*4 + lipides*9
print (f"You consumed {breakfast} kcal")
glu1 = glucides*4
pro1 = protides*4
lip1 = lipides*9

glucides = float(input("Entrer le total de glucides consommés en (g): "))
protides = float(input("Entrer le total de protides consommés (g): "))
lipides = float(input("Entrer le total de lipides consommés (g): "))
lunch = glucides*4 + protides*4 + lipides*9
print (f"You consumed {lunch} kcal")
glu2 = glucides*4
pro2 = protides*4
lip2 = lipides*9

glucides = float(input("Entrer le total de glucides consommés en (g): "))
protides = float(input("Entrer le total de protides consommés (g): "))
lipides = float(input("Entrer le total de lipides consommés (g): "))
dinner = glucides*4 + protides*4 + lipides*9
print (f"your consumed {dinner} kcal")
glu3 = glucides*4
pro3 = protides*4
lip3 = lipides*9

total = breakfast + lunch + dinner
print (f"your total is {total} calories")

gluper = ((glu1 + glu2 + glu3)*100/total)
proper = ((pro1 + pro2 + pro3)*100/total)
lipper = ((lip1 + lip2 + lip3)*100/total)
print (f"Votre pourcentage de glucides est {gluper}%")
print (f"Votre pourcentage de protides est {proper}%")
print (f"Votre pourcentage de lipides est {lipper}%")
if gluper == 60 and proper == 25 and lipper == 15:
    print ("Cette ration respecte le régle GPL.")
else:
    print ("Cette ration ne respecte pas le régle GPL.")
    print("Améliorer votre régime!")
