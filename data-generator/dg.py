import csv
import random
from column import Column
from sardinas_patterson import Sardinas_Patterson

# ecriture et lecture de fichier
def write_data_to_csv(file_path, data, header="head"):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for value in data:
            writer.writerow(value)

def write_list_to_csv(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def read_data_in_file(filename):
    langages = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        
        for row in reader:
            langage = row[0].split(",")
            langages.append(langage)

    return langages

# Generation des data
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

def getColumnValue(language) :
    value = [
        column.calculate_bit_changes(language),
        column.calculate_one_ratio(language),
        column.calculate_prefix_count(language),
        column.calculate_zero_ratio(language),
        column.is_prefix_code(language),
        column.longueur_maximal(language),
        column.longueur_total(language),
        column.nombre_de_mot(language),
        sardinas_patterson.sardinas_patterson(set(language))
    ]

    return value

sardinas_patterson = Sardinas_Patterson()
column = Column()

data = read_data_in_file("data.csv")
data_info = []

header = ['bit_change','one_ratio','prefix_number','zero_ratio','is_prefix','max_len','total_len','word_number','classe']

for _ in data:
    data_info.append(getColumnValue(_))

write_data_to_csv("training_data.csv", data_info, header)

# c = set(['011', '1000110', '00000', '0110', '010'])
# print(sardinas_patterson(set(c)))


