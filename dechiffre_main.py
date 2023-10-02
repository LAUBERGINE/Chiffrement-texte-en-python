from math import*
from random import*
from chiffrement_page import*


print("__BIENVENUE SUR EGGPLANTS DECRYPT PASSWORD__")
mdp = str(input("Ecrire le mot de passe : "))
nb = int(input("Ton identifiant : "))
print("Attention ça peut prendre jusqu'a 2 minutes")


for i in range (1, nb+1, 1):
    mdp = Dechiffrement(mdp)

print("Le mot de passe : ",mdp)