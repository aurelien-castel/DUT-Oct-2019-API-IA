"""
@author: Aurelien Castel
"""

import numpy as np
from random import randrange

from agents.agent import Agent
# les noeuds:
from agents.node import Node


class Random(Agent):
    """
    Agent qui sélectionne aléatoirement
    """

    def choose_move(self, node):
        """
        Methode pour faire des choix aléatoires
        """
        try:
            isinstance(node, Node)
        except AttributeError:
            raise Exception("AttributeError")

        valid = node.game.valid_moves(node.player)  # <-- test
        random_index = randrange(len(node.game.valid_moves(node.player)))
        print("Coup décidé : " +
              str(node.game.valid_moves(node.player)[random_index]))
        return node.game.valid_moves(node.player)[random_index]
