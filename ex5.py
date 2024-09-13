#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Entrez le pays pour lequel vous voulez entrer les médailles ")

while not country.isalpha():
    print("Vous avez entré une chaine de caractères invalide pour le pays \nVeuillez entrer les lettres représentant votre pays ")
    country = input("Entrez le pays pour lequel vous voulez entrer les médailles ")
    

code_medals = input("Entrer la chaine de caratère représentant les médailles gagnées ")
code_medals.upper()
gold = code_medals.count("G")
silver = code_medals.count("S")
bronze = code_medals.count("B")
print(f"MÉDAILLES : \n Nombre de médailles d'or : {gold} \n Nombre de médailles d'argent : {silver} \n Nombre de médailles de bronze : {bronze}")
