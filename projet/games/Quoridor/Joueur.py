# coding=utf-8


class Joueur():
    """Classe Joueur

    Deux joueurs sont créés et positionnés aux extrémités du plateau de jeu.
    """

    def __init__(self, name, pawn, finishline, phasenumber, y, x):
        """Constructeur de la classe Joueur

        Un joueur possède:
            - un nom permettant de le distinguer,
            - un pion permettant de suivre ses déplacements,
            - une ligne d'arrivee à franchir pour gagner,
            - une position x (colonne),
            - une position y (ligne),
            - un nombre de mur à poser.
        """

        self.nom = name
        self.pion = pawn
        self.arrivee = finishline
        self.posY = y
        self.posX = x
        self.nbMurs = 10

        # Compteur de phases
        self.numerophase = phasenumber

    def retraitMur(self):
        """Méthode retraitMur

        Décrémente le stock des murs à poser du joueur.
        """

        self.nbMurs -= 1
        print("Joueur ", self.pion, ", il vous reste ", self.nbMurs, " murs.")
