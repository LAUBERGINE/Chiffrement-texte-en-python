from math import*
from random import*
from chiffrement_page import*


print("__BIENVENUE SUR EGGPLANTS CREATOR PASSWORD__")
mdp = str(input("Ecrire le mot de passe : "))
print("Attention ça peut prendre jusqu'a 2 minutes")
nb = randint(1, 14000000) #Nombres de possibilités (ici c'est 14 millions de possibilité au max)
print("Votre Identifiant : ",nb) 

for i in range (1, nb+1, 1):
    mdp = Chiffrement(mdp)

print("Le mot de passe : >",mdp,"<")