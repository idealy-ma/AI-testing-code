import random

def generer_mot():
    longueur = random.randint(1, 7)
    
    mot = ''.join(random.choice('01') for _ in range(longueur))
    return mot

def generer_langage():
    nb_mots = random.randint(1, 5)
    langage = []
    for _ in range(nb_mots):
        langage.append(generer_mot())
    return langage


print(generer_langage())