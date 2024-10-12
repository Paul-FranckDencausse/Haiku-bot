import re

# Fonction pour compter les syllabes basées sur les voyelles dans un mot
def compter_syllabes(mot):
    mot = mot.lower()
    syllabes = len(re.findall(r'[aeiouy]+', mot)) # Compte les groupes de voyelles
    if mot.endswith('e'):  # Le 'e' à la fin ne compte souvent pas en français
        syllabes -= 1
    return max(syllabes, 1)  # Minimum 1 syllabe par mot

# Fonction pour compter les syllabes dans une phrase
def compter_syllabes_phrase(phrase):
    mots = phrase.split()
    return sum(compter_syllabes(mot) for mot in mots)

# Fonction principale pour détecter les haïkus
def detecter_haiku(texte):
    phrases = texte.split('\n')  # Divise le texte en lignes (ou phrases)
    haikus_trouves = []

    for i in range(len(phrases) - 2):  # On regarde 3 lignes à la suite
        ligne1_syllabes = compter_syllabes_phrase(phrases[i])
        ligne2_syllabes = compter_syllabes_phrase(phrases[i+1])
        ligne3_syllabes = compter_syllabes_phrase(phrases[i+2])

        if ligne1_syllabes == 5 and ligne2_syllabes == 7 and ligne3_syllabes == 5:
            haikus_trouves.append((phrases[i], phrases[i+1], phrases[i+2]))

    return haikus_trouves

# Demander à l'utilisateur d'entrer plusieurs lignes
print("Entre ton texte ligne par ligne (laisse une ligne vide pour terminer) :")
lignes = []
while True:
    ligne = input()
    if ligne == "":
        break
    lignes.append(ligne)

# Joindre toutes les lignes ensemble, séparées par des retours à la ligne
texte = "\n".join(lignes)

# Analyse le texte pour détecter les haïkus
haikus = detecter_haiku(texte)

# Afficher les haïkus détectés
if haikus:
    for haiku in haikus:
        print("\nHaïku détecté :")
        for ligne in haiku:
            print(ligne)
else:
    print("Aucun haïku détecté.")