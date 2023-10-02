#Generer key random de 74 characteres 

#Contenent :

    #ABCDEFGHIJKLMNOPQRSTUVWXYZ
    #abcdefghijklmnopqrstuvwxyz
    #0123456789
    #!§.?$£*µ@-+/

#Exemple :

    #KEY 1
        # ANS7µ0g5Q6$-armeJK49 .3z?tc/£i!1§qEO@*PjMHsGdvyV+D8WLXkn2fBCpZURTxoYIwlbhFu
    #KEY 2
        # NQ3LVZdDwf5sEq1BrvRnaW£kigl.µ2SHJ4zY6oxG0mC AjyMKXO/!9tIc+p?7T*@bU-8FePh§$u

from random import*

caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!§.?$£*µ@-+/ "
liste_de_caracteres = list(caracteres)
for i in range(1,3):
    print("\nKEY",i)
    b = []
    while len(b) != 75:
        a = randint(0, 74)
        if a not in b:
            b.append(a)
            element_choisi = liste_de_caracteres[a]
            print(element_choisi, end='')

