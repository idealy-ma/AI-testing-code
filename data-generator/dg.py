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

def generer_donnees_csv(nombre_donnees, nom_fichier, header = ["Langage"]):
    donnees_uniques = set()
    with open(nom_fichier, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
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

# Les colonnes
def longueur_total(language):
    total_length = sum(len(word) for word in language)
    return total_length

def nombre_de_mot(language):
    num_words = len(language)
    return num_words

def longueur_maximal(language):
    max_length = max(len(word) for word in language)
    return max_length

def calculate_zero_ratio(language):
    total_characters = ''.join(language)
    num_zeros = sum(1 for char in total_characters if char == "0")
    zero_ratio = num_zeros / len(total_characters) if len(total_characters) > 0 else 0
    return zero_ratio

def calculate_one_ratio(language):
    total_characters = ''.join(language)
    num_ones = sum(1 for char in total_characters if char == "1")
    one_ratio = num_ones / len(total_characters) if len(total_characters) > 0 else 0
    return one_ratio

def calculate_bit_changes(language):
    num_changes = sum(1 for i in range(1, len(language)) if language[i] != language[i-1])
    return num_changes

# existance de prefixe
def is_prefix_code(langage):
    langage = sorted(langage, key=len)
    n = len(langage)
    
    for i in range(n):
        for j in range(i+1, n):
            if langage[j].startswith(langage[i]):
                return 0 
    
    return 1

# nombre de prefixe
def calculate_prefix_count(language):
    prefixes = set()
    count = 0
    for word in language:
        for i in range(1, len(word) + 1):
            prefix = word[:i]
            if prefix not in prefixes:
                prefixes.add(prefix)
                count += 1
    return count

# Sardinas and patterson
def multiply(lang1, lang2):
    newLang = set()
    for u in lang1 :
        for v in lang2 :
            if len(u) >= len(v) and u.find(v) == 0:
                newLang.add(u[len(v):])
    return newLang

def removeVoid(language):
    result = set()
    for u in language:
        if u != '' :
            result.add(u)

    return result

def sardinas_patterson(language):
    uN = removeVoid(multiply(language, language))
    uN_1 = []
    while True :
        uN_1.append(set(uN))
        uN = multiply(uN, language).union(multiply(language, uN))
        
        for value in uN :
            if value == "":
                return 0

        for value in uN_1 :
            if value == uN :
                return 1


# generer_donnees_csv(10000, 'data.csv' )
data = read_data_in_file("data.csv")

for _ in data:
    print(_)
    print(sardinas_patterson(set(_)))

# c = set(['011', '1000110', '00000', '0110', '010'])
# print(sardinas_patterson(set(c)))


