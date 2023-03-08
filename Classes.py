from collections import defaultdict


class Node:
    def __init__(self, label=None, freq=None, FG=None, FD=None):
        self.label = label
        self.freq = int(freq)
        self.FG = FG
        self.FD = FD

    def __str__(self):
        return self.label

    def is_leaf(self):
        return (self.FG is None) and (self.FD is None)

    def children(self):
        return [self.FG, self.FD]


class Arbre:
    def __init__(self, root):
        self.root = root
        self.label = self.root.label
        self.freq = self.root.freq
        self.FG = self.root.FG
        self.FD = self.root.FD

    def __str__(self):
        return str(self.root)

    def is_leaf(self):
        return (self.root.FG is None) and (self.root.FD is None)

    def children(self):
        return [self.root.FG, self.root.FD]


    #fonction qui fait un parcourt d'arbre et retourne la liste des noeuds
    #et un dictionnaire contenant tous les noeuds avec avec leur code binaire
    def parcourt(self, liste=[], dico={}, parent=None):
        if parent is None:
            dico = defaultdict(str)
            parent = self.root
            dico[parent] = ''
        if not self in liste:
            liste.append(self)
        if not self.root.is_leaf():
            parent = self.root
            dico[self.root.FG] = dico[parent] + '0'
            Arbre(self.root.FG).parcourt(liste, dico, parent)
            dico[self.root.FD] = dico[parent] + '1'
            Arbre(self.root.FD).parcourt(liste, dico, parent)
        return liste, dico
