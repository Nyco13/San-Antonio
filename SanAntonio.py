
import random
Quote = ["Tu ne l'emporteras pas au paradis", "Tant va la cruche à l'eau quà la fin elle se casse", "Les plus faibles ont toujours tort", "Qui vivra verra", "Un tien vaut mieux que 2 tu l'auras"]
Characters = ["San Antonio", "Felicie", "Antoine", "César", "Mathias"]

def MainFunction()
    MainVar= input("Appuyez sur Entrée pour avoir une citation et un personnage de San Antonio; Appuyez sur E pour terminer le programme")
    if MainVar == E : pass
    else item = random.randrange(0;len(Quote))
        print(Quote[item])
        print(Characters[item])

while MainFunction() !=E :