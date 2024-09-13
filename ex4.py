# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = float(input("Veuillez entrer le pourcentage de batterie (entre 0 et 100) : "))

if battery_level in range(51,101):
    distance = ((battery_level - 50) * 2) + (25 * 0.5) + (15 * 1) + (5 * 2.5) + (5 * 6)
elif battery_level in range(26, 51):
    distance = ((battery_level - 25) * 0.5) + (15 * 1) + (5 * 2.5) + (5 * 6)
elif battery_level in range(11, 26):
    distance = ((battery_level - 10) * 1) + (5 * 2.5) + (5 * 6)
elif battery_level in range(6, 11):
    distance = ((battery_level - 5) * 2.5) + (5 * 6)
elif battery_level in range(0, 6):
    distance = (battery_level * 6)
else:
    print("la valeur entrée est invalide")

print(f"La distance maximale que vou pouvez parcourir est de {round(distance, 1)}km.")
