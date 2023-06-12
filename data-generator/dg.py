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


def generate_data_in_file(filename, nb_langages):
    with open(filename, 'w') as file:
        for _ in range(nb_langages):
            langage = generer_langage()
            line = ' '.join(langage)
            file.write(line + '\n')

def read_data_in_file(filename):
    langages = []
    with open(filename, 'r') as file:
        for line in file:
            langage = line.strip().split()
            langages.append(langage)
    return langages

# generate_data_in_file("data", 1000)
print(_ for _ in read_data_in_file("data"))