# coding=utf-8

from Plateau import *

class Main():
    """Classe Main

    Lance le jeu.
    """

    p = Plateau()
    compteur = 0
    action = [False, False]

    while(p.finDeJeu is False):
        p.afficherTabDeJeu()
        p.tour(compteur, action)
        compteur += 1

