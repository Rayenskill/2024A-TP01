# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math

speed = float(input("Quelle est la vitesse initiale de la boule ? ")) 
angle = float(input("Quel est l'angle de lancement de la boule ? "))
g = 9.8
distance = ((speed ** 2)*(math.sin(2*((angle*math.pi)/180))))/g
print(f"La distance maximale qui peut être parcourue par la balle est de {distance:.4}m",)