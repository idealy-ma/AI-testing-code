import csv
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

def generer_donnees_csv(nombre_donnees, nom_fichier):
    donnees_uniques = set()
    with open(nom_fichier, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Langage'])
        while len(donnees_uniques) < nombre_donnees:
            langage = ','.join(generer_langage())
            if langage not in donnees_uniques:
                donnees_uniques.add(langage)
                writer.writerow([langage])

def read_data_in_file(filename):
    langages = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        
        for row in reader:
            langage = row[0].split(",")
            langages.append(langage)

    return langages




generer_donnees_csv(10000, 'data.csv' )
data = read_data_in_file("data.csv")
for _ in data:
    print(_)