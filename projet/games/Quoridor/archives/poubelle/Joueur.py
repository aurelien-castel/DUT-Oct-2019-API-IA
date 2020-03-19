# coding=utf-8

from random import *


class Joueur():
    """Classe Joueur

    Deux joueurs sont créés et positionnés aux extrémités du plateau de jeu.
    """

    # Liste des déplacements possibles
    # -4 : à gauche ou en haut (saute-mouton)
    # -2 : à gauche ou en haut
    # -1 : en haut (pour atteindre la ligne d'arrivée)
    # 1 : en bas (pour atteindre la ligne d'arrivée)
    # 2 : à droite ou en bas
    # 4 : à droite ou en bas (saute-mouton)
    deplacements = [-4, -2, -1, 1, 2, 4]

    def __init__(self, name, pawn, finishline, numerophase, y, x):
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
        self.numerophase = numerophase

    def seDeplacer(self, choix, plateau):
        """Méthode seDeplacer

        Actualise la position du joueur en fonction :
            - de son choix,
            - des murs posés,
            - des limites du plateau.
        """

        # Efface l'ancienne position du joueur sur le plateau de jeu
        plateau.tabDeJeu[self.posY][self.posX] = 0

        # Cas d'un déplacement vers le haut (choix = 1)
        if(choix == "haut"):

            # Pour atteindre la ligne d'arrivée
            if(self.posY == 1):
                self.posY += self.deplacements[2]

            elif self.posY != 0:
                # Cas général
                if(plateau.tabDeJeu[self.posY-1][self.posX] != 1):
                    if(plateau.tabDeJeu[self.posY-2][self.posX] == 0):
                        self.posY += self.deplacements[1]

                    # Cas où le joueur adverse se trouve sur la case choisie
                    else:
                        if(plateau.tabDeJeu[self.posY-3][self.posX] != 1):
                            self.posY += self.deplacements[0]

        # Cas d'un déplacement vers le bas (choix = 2)
        elif(choix == "bas"):

            # Pour atteindre la ligne d'arrivée
            if(self.posY == plateau.ligne-2):
                self.posY += self.deplacements[3]

            elif self.posY != plateau.ligne-1:
                # Cas général
                if(plateau.tabDeJeu[self.posY+1][self.posX] != 1):
                    if(plateau.tabDeJeu[self.posY+2][self.posX] == 0):
                        self.posY += self.deplacements[4]

                    # Cas où le joueur adverse se trouve sur la case choisie
                    else:
                        if(plateau.tabDeJeu[self.posY+3][self.posX] != 1):
                            self.posY += self.deplacements[5]

        # Cas d'un déplacement vers la gauche (choix = 3)
        elif(choix == "gauche"):
            # si on est à colonne 2 on ne peut pas faire de saute mouton
            if self.posX == 2:
                self.posX += self.deplacements[1]
            # Cas général
            elif self.posX != 0:
                if(plateau.tabDeJeu[self.posY][self.posX-1] != 1):
                    if(plateau.tabDeJeu[self.posY][self.posX-2] == 0):
                        self.posX += self.deplacements[1]

                # Cas où le joueur adverse se trouve sur la case choisie
                    elif self.posX != 2:
                        if(plateau.tabDeJeu[self.posY][self.posX-3] != 1):
                            self.posX += self.deplacements[0]

        # Cas d'un déplacement vers la droite (choix = 4)
        elif(choix == "droite"):
            # si on est la colonne 14
            if self.posX == plateau.colonne:
                self.posX += self.deplacements[4]
            # Cas général
            elif self.posX != plateau.colonne-1:
                if(plateau.tabDeJeu[self.posY][self.posX+1] != 1):
                    if(plateau.tabDeJeu[self.posY][self.posX+2] == 0):
                        self.posX += self.deplacements[4]

                    # Cas où le joueur adverse se trouve sur la case choisie
                    else:
                        if(plateau.tabDeJeu[self.posY][self.posX+3] != 1):
                            self.posX += self.deplacements[5]

    def message(self, erreur, plateau):
        """Méthode message

        Affiche un message d'erreur :
            - soit lorsqu'un mur sépare le joueur de la case dans laquelle il veut se déplacer,
            - soit lorsque le joueur est à l'extrémité du plateau et qu'il veut la dépasser.

        Ensuite, demande au joueur de faire un autre choix.
        """

        # Cas où l'erreur est due à une réponse invalide
        if(erreur == "invalide"):
            self.seDeplacer(
                int(input("Veuillez donner une reponse valide : ")), plateau)

        else:
            # Cas où l'erreur est due à un mur
            if(erreur == "mur"):
                print("Un mur se trouve devant vous, vous ne pouvez pas le traverser !")

            # Cas où l'erreur est due aux extrémités du plateau
            else:
                print(
                    "Vous êtes à l'extrémité du plateau, vous ne pouvez pas aller plus loin !")

            self.seDeplacer(
                int(input("Veuillez indiquer un autre déplacement : ")), plateau)

    def poserMur(self, murs, num, plateau):
        """Méthode poserMur

        Pose un mur sur la case dont le numéro est celui choisi.
        """

        murY = murs[num-1]['y']
        murX = murs[num-1]['x']
        # print("y : ", murY, " x : ", murX)

        if(plateau.tabDeJeu[murY][murX] == 'm'):

            # Si le joueur peut poser un mur verticalement et horizontalement
            if(plateau.tabDeJeu[murY+1][murX] == 'm' and plateau.tabDeJeu[murY][murX+1] == 'm'):

                # On choisit pour le joueur au hasard
                direction = randint(1, 2)

                # Verticalement
                if(direction == 1):
                    plateau.tabDeJeu[murY+1][murX] = 1

                # Horizontalement
                else:
                    plateau.tabDeJeu[murY][murX+1] = 1

            # Si le joueur peut poser un mur horizontalement
            elif(plateau.tabDeJeu[murY][murX+1] == 'm'):
                plateau.tabDeJeu[murY][murX+1] = 1

            # Si le joueur peut poser un mur verticalement
            elif(plateau.tabDeJeu[murY+1][murX] == 'm'):
                plateau.tabDeJeu[murY+1][murX] = 1

            # Si le joueur ne peut pas poser de mur ni horizontalement ni verticalement (à cause de la deuxième case)
            else:
                print("Vous ne pouvez pas poser de mur à cet endroit-là...")
                self.poserMur(murs, int(input(
                    "Veuillez indiquer un autre numéro pour la position du mur à poser : ")), plateau)

            # Lorsqu'au moins l'une des conditions ci-dessus est satisfaite
            plateau.tabDeJeu[murY][murX] = 1
            self.retraitMur()

        # Si le joueur ne peut pas poser de mur (à cause de la première case)
        else:
            print("Vous ne pouvez pas poser de mur à cet endroit-là...")
            self.poserMur(murs, int(input(
                "Veuillez indiquer un autre numéro pour la position du mur à poser : ")), plateau)

    def retraitMur(self):
        """Méthode retraitMur

        Décrémente le stock des murs à poser du joueur.
        """

        self.nbMurs -= 1
        print("Joueur ", self.pion, ", il vous reste ", self.nbMurs, " murs.")


############### Méthodes utilisées par la méthode valid_moves de la classe Plateau ###############


    def check_moves(self, choix, plateau):
        # print(plateau.ligne)
        # print(plateau.colonne)
        """Méthode check_moves

        Renvoie True si le déplacement choisi est possible et False sinon.
        """

        # Cas d'un déplacement vers le haut (choix = 1)
        if(choix == "haut"):
            # si on est à la ligne 1 on vérifie qu'il n'y a pas d'adversaire ou obstacle
            if self.posY == 1:
                if plateau.tabDeJeu[self.posY-1][self.posX] != 5:
                    return False
                else:
                    return True
            # si on est à la première ligne impossible d'aller en haut
            elif self.posY == 0:
                return False
            else:
                if((plateau.tabDeJeu[self.posY-1][self.posX] != 1
                    and plateau.tabDeJeu[self.posY-2][self.posX] == 0)
                   or (plateau.tabDeJeu[self.posY-1][self.posX] != 1
                       and plateau.tabDeJeu[self.posY-2][self.posX] != 0
                       and plateau.tabDeJeu[self.posY-3][self.posX] != 1)):

                    return True

                else:
                    return False

        # Cas d'un déplacement vers le bas (choix = 2)
        elif(choix == "bas"):
            # si on est à ligne 17 on vérifie qu'il n'y a aucun obstacle ou adversaire
            if self.posY == plateau.ligne-2:
                if plateau.tabDeJeu[self.posY+1][self.posX] != 7:
                    return False
                else:
                    return True
            # si on est à la dernière ligne impossible d'aller en bas
            elif self.posY == plateau.ligne-1:
                return False
            elif self.posY <= plateau.ligne-4:
                print(len(plateau.tabDeJeu))
                if((plateau.tabDeJeu[self.posY+1][self.posX] != 1
                    and plateau.tabDeJeu[self.posY+2][self.posX] == 0)
                   or (plateau.tabDeJeu[self.posY+1][self.posX] != 1
                       and plateau.tabDeJeu[self.posY+2][self.posX] != 0
                        and plateau.tabDeJeu[self.posY+3][self.posX] != 1)):

                    return True
                else:
                    return False

        # Cas d'un déplacement vers la gauche (choix = 3)
        elif(choix == "gauche"):
            # si on est a la colonne 2 on vérifie s'il n'y l'adversaire à la colonne 0
            # ou un mur
            if self.posX == 2:
                if plateau.tabDeJeu[self.posY][self.posX-1] == 1:
                    return False
                else:
                    if plateau.tabDeJeu[self.posY][self.posX-2] != 0:
                        return False
                    else:
                        return True
            # si on est tout à gauche impossible d'aller à gauche
            elif self.posX == 0:
                return False
            else:
                if((plateau.tabDeJeu[self.posY][self.posX-1] != 1
                    and plateau.tabDeJeu[self.posY][self.posX-2] == 0)

                    or

                    (plateau.tabDeJeu[self.posY][self.posX-1] != 1
                     and plateau.tabDeJeu[self.posY][self.posX-2] != 0
                     and plateau.tabDeJeu[self.posY][self.posX-3] != 1)):

                    return True
                else:
                    return False

        # Cas d'un déplacement vers la droite (choix = 4)
        elif(choix == "droite"):
            # si on est à la colonne 14, on vérifie qu'il n'y apas de mur à droite
            if self.posX == plateau.colonne-3:
                if plateau.tabDeJeu[self.posY][self.posX+1] == 1:
                    return False
                # et pas d'adversaire
                else:
                    if plateau.tabDeJeu[self.posY][self.posX+2] != 0:
                        return False
                    else:
                        return True
            # si on est à la dernière colonne on ne peut pas aller à droite
            elif self.posX == plateau.colonne-1:
                return False

            else:
                if((plateau.tabDeJeu[self.posY][self.posX+1] != 1
                    and plateau.tabDeJeu[self.posY][self.posX+2] == 0)

                    or

                    (plateau.tabDeJeu[self.posY][self.posX+1] != 1
                     and plateau.tabDeJeu[self.posY][self.posX+2] != 0
                     and plateau.tabDeJeu[self.posY][self.posX+3] != 1)):

                    return True

                else:
                    return False

        # Cas où le joueur entre une autre valeur que celles autorisées
        else:
            return False

    def check_laying_walls(self, murs, num, plateau):
        """Méthode check_laying_walls

        Renvoie True si le placement du mur est possible et False sinon.
        """

        murY = murs[num-1]['y']
        murX = murs[num-1]['x']

        # Verticalement et horizontalement
        if((plateau.tabDeJeu[murY][murX] == 'm'
            and plateau.tabDeJeu[murY+1][murX] == 'm'
            and plateau.tabDeJeu[murY][murX+1] == 'm')

            or

            # Verticalement
            (plateau.tabDeJeu[murY][murX] == 'm'
             and plateau.tabDeJeu[murY+1][murX] == 'm')

            or

            # Horizontalement
            (plateau.tabDeJeu[murY][murX] == 'm'
             and plateau.tabDeJeu[murY][murX+1] == 'm')):

            return True

        else:
            return False
