# TODO: Créer un script permettant le formattage du livre des records des JO.

country = input("De quelle nationalité est l'athlète ? ")
athlete = input("Quel est le nom de l'athlète ? ")
date = input("Entrez la date ? ")
dicipline = input("Quelle dicipline pratique l'athlète ? ")
category = input("Dans quelle catégorie l'athlète compétitionne ? ")
record = input("Quel est le record ? ")
affichage = f"Nouveau Record : \n {date} \n {dicipline} - {category} \n {athlete} {country} - {record}"
print(affichage)