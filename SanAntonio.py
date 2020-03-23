
import random
import json

Quotes = ["Tu ne l'emporteras pas au paradis", "Tant va la cruche à l'eau qu'à la fin elle se casse", "Les plus faibles ont toujours tort", "Qui vivra verra", "Un tien vaut mieux que 2 tu l'auras"]
Characters = ["San Antonio", "felicie", "Antoine", "césar", "Mathias"]

def message(character, quote):
    n_character =character.capitalize()
    n_quote = quote.capitalize()
    return "{} a dit : {}".format(n_character, n_quote)

def RandomQuotes():
    RandomQ = random.randint(0,len(Quotes))
    return RandomQ
    
def RandomChar():
    RandomC = random.randint(0,len(Characters))
    return RandomC

MainVar= input("Appuyez sur Entrée pour avoir une citation et un personnage de San Antonio; Appuyez sur E pour terminer le programme")
while MainVar != "E" :
    RandomQuotes()
    RandomChar()
    print(message(Characters[RandomC],Quotes[RandomQ]))
