##############################################################################
# votre IA : à vous de coder
# Rappel : ne pas changer les paramètres des méthodes
# vous pouvez ajouter librement méthodes, fonctions, champs, ...
##############################################################################

import random
from moteur_esn_wars import *

class IA_ESNW:
    def __init__(self, num_joueur : int, game_dic : dict) -> None:
        """génère l'objet de la classe IA_ESNW

        Args:
            desc (str): descriptif de l'état initial de la partie
            num_joueur (int): numéro de joueur attribué à l'IA
        """

        print("IA num", num_joueur,"chargée : OK")
        pass


    def action(self, game_dict: dict) -> str:
        """Appelé à chaque décision du joueur IA

        Args:
            game_dict (dict): descriptif de l'état de la partie

        Returns:
            str : une action 'N', 'S', 'E', 'W', 'L', 'E', 'P'
        """

        # Access the missions' positions from the game_dict
        missions_positions = {tuple(m['position']): m for m in game_dict['missions']}


        # Now you can use missions_positions to get information about missions
        for mission_position, mission in missions_positions.items():
            print(mission_position)
            pass

        # Return a random action for now (replace this with your logic)
        return ['N', 'S', 'E', 'W'][random.randint(0, 3)]





    def game_over(self, game_dict: dict) -> None:
        """Appelé à la fin du jeu ; sert à ce que vous voulez

        Args:
            descr (str): descriptif du dernier tour de jeu
        """
        pass
