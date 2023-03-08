import os

from collections import defaultdict
from Classes import Node, Arbre


def codage(fichierBase, fichierFreq, fichierBin):
    with open(fichierBase, "r") as f:
        contenu = f.read()  # lire le contenu du fichier

    frequence = defaultdict(int)  # Initialiser un dictionnaire pour stocker les occurrences

    # compter les occurrences de chaque lettre
    for lettre in contenu:
        frequence[lettre] += 1
    sorted_frequence = sorted(frequence.items(), key=lambda x: (x[1], ord(x[0])))  # liste triée des fréquences

    # ecris dans le fichier des frequences les frequences de chaque caractère
    with open(fichierFreq, "w") as f:
        # Ecrire dans le fichier
        f.write(str(len(sorted_frequence)))
        for i in sorted_frequence:
            f.write('\n')
            f.write(str(i[0]))
            f.write(' ')
            f.write(str(i[1]))

    # crée la liste des arbres où chaque arbre correspond à chaque caractère
    liste_Arbre = []
    for i in sorted_frequence:
        liste_Arbre.append(Arbre(Node(i[0], i[1])))

    # crée l'abre de Huffman
    while len(liste_Arbre) != 1:
        arbre1 = None
        arbre2 = None
        freq1 = int(liste_Arbre[0].root.freq)
        for arbre in liste_Arbre:
            if (arbre.root.freq <= freq1):
                arbre1 = arbre
                freq1 = arbre.root.freq
        liste_Arbre.remove(arbre1)
        freq2 = int(liste_Arbre[0].root.freq)
        for arbre in liste_Arbre:
            if (arbre.root.freq <= freq2):
                arbre2 = arbre
                freq2 = arbre.root.freq
        liste_Arbre.remove(arbre2)
        liste_Arbre.append(Arbre(Node(freq=freq1 + freq2, FG=arbre1, FD=arbre2)))

    # création du dictionnaire avec pour clés les carcatère et pour valeur leur coodage en binaire
    arbre = liste_Arbre[0].parcourt()[1]
    newDico = {}
    for i, j in arbre.items():
        if i.label is not None:
            newDico[i.label] = j

    # création du texte binaire
    binTexte = ''
    for lettre in contenu:
        binTexte += newDico[lettre]
    binaryTexte = int(binTexte, 2)
    l_BinTexte = (len(binTexte) + 7) // 8

    # écriture de ce texte dans le fichier bin en le convertissant en bytes
    with open(fichierBin, "wb") as f:
        f.write(binaryTexte.to_bytes(l_BinTexte))

    return newDico


# donne le nombre moyen de bits par caractère pour un dictionnaire
def nombreMoyenBits(dico):
    moyenne = 0
    for caractere in dico:
        moyenne += len(dico[caractere])
    moyenne = moyenne / len(dico)
    return moyenne


if __name__ == "__main__":
    '''Fichier textesimple.txt'''
    fichierBase = "Ressources/textesimple.txt"
    fichierFreq = "Ressources/textesimple_freq.txt"
    fichierBin = "Ressources/textesimple_comp.bin"

    codage(fichierBase, fichierFreq, fichierBin)
    dico = codage(fichierBase, fichierFreq, fichierBin)
    nbBits = nombreMoyenBits(dico)

    file_path1 = "Ressources/textesimple.txt"
    file_size1 = os.path.getsize(file_path1)

    file_path2 = "Ressources/textesimple_comp.bin"
    file_size2 = os.path.getsize(file_path2)

    print("The size of the file '{}' is {} octets.".format(file_path1, file_size1))
    print("The size of the file '{}' is {} octets.".format(file_path2, file_size2))
    print("Taux de compression = ", 1 - file_size2 / file_size1)
    print("Nombre moyen de bits par caractère = ", nbBits)
    print('\n')

    '''Fichier extraitalice.txt'''
    fichierBase = "Ressources/extraitalice.txt"
    fichierFreq = "Ressources/extraitalice_freq.txt"
    fichierBin = "Ressources/extraitalice_comp.bin"

    codage(fichierBase, fichierFreq, fichierBin)
    dico = codage(fichierBase, fichierFreq, fichierBin)
    nbBits = nombreMoyenBits(dico)

    file_path1 = "Ressources/extraitalice.txt"
    file_size1 = os.path.getsize(file_path1)

    file_path2 = "Ressources/extraitalice_comp.bin"
    file_size2 = os.path.getsize(file_path2)

    print("The size of the file '{}' is {} octets.".format(file_path1, file_size1))
    print("The size of the file '{}' is {} octets.".format(file_path2, file_size2))
    print("Taux de compression = ", 1 - file_size2 / file_size1)
    print("Nombre moyen de bits par caractère = ", nbBits)
    print('\n')

    '''Fichier alice.txt'''
    fichierBase = "Ressources/alice.txt"
    fichierFreq = "Ressources/alice_freq.txt"
    fichierBin = "Ressources/alice_comp.bin"

    codage(fichierBase, fichierFreq, fichierBin)
    dico = codage(fichierBase, fichierFreq, fichierBin)
    nbBits = nombreMoyenBits(dico)

    file_path1 = "Ressources/alice.txt"
    file_size1 = os.path.getsize(file_path1)

    file_path2 = "Ressources/alice_comp.bin"
    file_size2 = os.path.getsize(file_path2)

    print("The size of the file '{}' is {} octets.".format(file_path1, file_size1))
    print("The size of the file '{}' is {} octets.".format(file_path2, file_size2))
    print("Taux de compression = ", 1 - file_size2 / file_size1)
    print("Nombre moyen de bits par caractère = ", nbBits)
