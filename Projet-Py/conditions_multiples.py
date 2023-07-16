#Utilisation des conditions multiples avec des opérateurs logiques
avec_soleil = False
en_semaine = False
if avec_soleil and not en_semaine:
    print("on va à la plage")
elif avec_soleil and en_semaine:
    print("on va au travail")
else:
    print("on reste à la maison")
