# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = int(input("Quel est le le pourcentage de votre batterie ? "))

if battery_level in range(51, 101):
    distance = (battery_level - 50) * 2 + ((battery_level - 25) / 2) + (battery_level - 10) + (battery_level - 5) * 2.5 + (battery_level * 6)
    print(f"la distance maximale que vous pouvez parcourir est de {round(distance, 1)}km")
elif battery_level in range(26, 51):
    distance = ((battery_level - 25) / 2) + (battery_level - 10) + (battery_level - 5) * 2.5 + (battery_level * 6)
    print(f"la distance maximale que vous pouvez parcourir est de {round(distance, 1)}km")
elif battery_level in range(11, 26):
    distance = battery_level 
    print(f"la distance maximale que vous pouvez parcourir est de {round(distance, 1)}km")
elif battery_level in range(6, 11):
    distance = battery_level * 2.5
    print(f"la distance maximale que vous pouvez parcourir est de {round(distance, 1)}km")
elif battery_level in range(0, 6):
    distance = battery_level * 6
    print(f"la distance maximale que vous pouvez parcourir est de {round(distance, 1)}km")
