# -*- coding: utf-8 -*-
"""
@author: Aurélien
"""
import os
import sys
import glob  # globing
import random
import pickle
from copy import deepcopy

# les noeuds:
from agents.node import Node
from utilities.agent_informations import Agent_Informations
from utilities.agent_victories import Agent_Victories

# asserts:
from agents.agent import Agent
from agents.apprentissage_RL.agent import Learner

# plot:
from utilities.plot import plot_winrate

from games.Quoridor.Plateau import Plateau as Quoridor

"""
fonctions utilitaires appelées depuis main.py
"""


def TurnBased(inital_game, agents):
    """
    Permet de jouer avec n'importe quel agent et n'importe quel nombre d'agent selon
    le nombre de joueurs dans la liste players du jeu entré.
    Les objets de type Learner apprennent durant chaque fin de partie.
    """
    for i in agents:
        try:
            isinstance(i, Agent)
        except AttributeError:
            raise Exception("AttributeError")

    game = deepcopy(inital_game)

    # liste de string qui représente les joueurs dans le jeu et définit le nombre de joueurs
    players = game.players

    if len(players) > len(agents):
        raise Exception("List index out of range: not enough agents to play")
    elif len(players) < len(agents):
        print("Too much agents: I will only take the firsts")

    # liste qui définit chaque joueur et sauvegarde leurs informations
    # permet de faire le parallèle entre les players et les agents
    # agents_info sera de la taille de players
    agents_info = []
    for i, j in zip(players, agents):
        agents_info.append(Agent_Informations(i, j))

    # During teaching, chose who goes first randomly with equal probability
    playerIndex = random.randrange(len(agents_info))

    print("#_______#NEW_GAME#_______#\n")

    # Initialize the learner's state and action
    for i in agents_info:
        if isinstance(i.agent, Learner):
            print("___", i.player, i.agent.__class__.__name__, "___")
            i.prev_state = game.print_game()
            currentnode = Node(game, i.player)
            i.prev_action = i.agent.choose_move(currentnode, i.prev_state)
            print("\n")

    # iterate until game is over
    while True:  # execute oldAction, observe reward and state

        # on joue le coup décidé selon choose_move par play_move
        if isinstance(agents_info[playerIndex].agent, Learner):
            game.play_move(
                agents_info[playerIndex].prev_action, agents_info[playerIndex].player)
        else:
            print("___", agents_info[playerIndex].player,
                  agents_info[playerIndex].agent.__class__.__name__, "___")
            currentnode = Node(game, agents_info[playerIndex].player)
            
            if len(currentnode.game.valid_moves(currentnode.player)) == 0:
                break
            
            choix = agents_info[playerIndex].agent.choose_move(
                currentnode)
            game.play_move(choix, agents_info[playerIndex].player)
            print("\n")

        # game is over. +10 reward if win, -10 if loss, 0 if draw
        if not game.winner() == None:
            break  # break car sinon updatera pour 0 à un état final

        # game continues. 0 reward
        reward = 0

        # change player
        playerIndex += 1
        if playerIndex >= len(players):
            playerIndex = 0

        stopAll = False
        for i in agents_info:
            if isinstance(i.agent, Learner):
                print("___", i.player,
                      i.agent.__class__.__name__, "___")
                # partie mise à jour des learners
                new_state = game.print_game()

                # the new node after playing
                currentnode = Node(game, i.player)
                if len(currentnode.game.valid_moves(currentnode.player)) == 0:
                    stopAll = True
                    break

                # determine new action (epsilon-greedy)
                new_action = i.agent.choose_move(currentnode, new_state)
                # update Q-values
                i.agent.update(currentnode, i.prev_state, new_state,
                               i.prev_action, new_action, reward)
                # reset "previous" values
                i.prev_state = new_state
                i.prev_action = new_action
                # append reward
                print("\n")
                
        if stopAll is True:
            break

    # Game over. Perform final update, game is over. +10 reward if win, -10 if loss, 0 if draw
    for i in agents_info:
        if isinstance(i.agent, Learner):
            if game.winner() == i.player:
                i.agent.update(currentnode, i.prev_state, None,
                               i.prev_action, None, 10)
            elif game.winner() == 'Draw':  # it's a draw
                i.agent.update(currentnode, i.prev_state, None,
                               i.prev_action, None, 0)
            else:  # another player wins
                i.agent.update(currentnode, i.prev_state, None,
                               i.prev_action, None, -10)

    print("#________________________#")
    print("Le gagnant est : " + str(game.winner()) + "\n")

    print("Affichage de fin : ")
    print(game.print_game())

    return game.winner()


# Print iterations progress
def progress(count, total, suffix=''):

    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '#' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('|%s| %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()  # As suggested by Rom Ruben

def TurnBased_episodes(game, number_games, print_games=False, *agents):
    """
    Permet de faire plusieurs appels de TurnBased, utilisé pour l'entrainement.
    On peut mettre plusieurs agents les uns à la suite des autres
    en argument de cette fonction. On a aussi besoins du jeu
    et le nombre de fois qu'on veut faire de jeux.
    """
    for i in agents:
        try:
            isinstance(i, Agent)
        except AttributeError:
            raise Exception("AttributeError")

    # liste de string qui représente les joueurs dans le jeu et définit le nombre de joueurs
    players = game.players

    agents_victories = []

    for i, j in zip(players, agents):
        agents_victories.append(Agent_Victories(i, j))
    # agent fictif pour les draw, on créé un objet vide "Draw"
    agents_victories.append(Agent_Victories("Draw", type("Draw", (), {})()))

    progress(1, number_games, "playing games")

    for i in range(number_games):

        if print_games is False:
            sys.stdout = open(os.devnull, 'w')  # disable print out
        winner = TurnBased(game, agents)
        if print_games is False:
            sys.stdout = sys.__stdout__  # restore print out

        # Monitor progress
        progress(i, number_games, "playing games")

        for i in agents_victories:
            if winner is i.player:
                i.victories += 1

    # à la fin on fait un diagramme pour représenter les victoires de chaque joueur

    print("")

    for i in agents_victories:
        if winner is i.player:
            i.victories += 1

    plot_winrate([o.victories for o in agents_victories],
                 [o.agent.__class__.__name__ for o in agents_victories], number_games)

# ──────────────────────────────────────────────────────────────────────────────── save & load


def save_learner(game, learner):
    """
    Save one game learner
    """
    if len(learner.rewards) != 0:
        while True:
            print(str(game.__class__.__name__) + " " +
                  str(learner.__class__.__name__) +
                  " Q matrix's size: " + str(len(learner.rewards)))
            response = input(
                "Enter the file's name you want for it or enter \"no\" if you don't want to save it: ")
            if response == 'n' or response == 'no':
                print("OK. Learner not saved.")
                break
            if not glob.glob("./"+response+"*"):
                learner.save_agent('./'+response+'.pkl')
                break
            else:
                print(
                    "Sorry but a file or a directory has already the same name, please enter another name.")
            print("")
        print("")


def load_learner(file_name):
    """
    Load one game learner
    """
    try:
        f = open(file_name, 'rb')
    except IOError:
        raise Exception("The learner file does not exist.")
    learner = pickle.load(f)
    f.close()
    return learner
