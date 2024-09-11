# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.
try:
    x = int(input("Quelle est le volume d'eau à assainir ? "))
except ValueError as e:
    print("vous avex entre un mauvais truc")
water_quantity = float(x)

if water_quantity < 5:
    print("La quantité d'eau est trop petite")

nb_filtre = int(water_quantity // 5)
nb_lampes = int(3 * water_quantity // 5)
chlore = 0.5 * water_quantity // 5
print(f"Il faut {nb_filtre} de filtre, {nb_lampes} de lampes et {chlore}kg de chlore pour assainir {water_quantity}L d'eau")
