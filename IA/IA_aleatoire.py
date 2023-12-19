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

            str : une action 'N', 'S', '
        Returns:E', 'W', 'L', 'E', 'P'

        """

        coders = game_dict['coders']

        current_player_number = 0  # Replace with the actual player number of your AI

        # Access the AI's current position
        current_position = coders[current_player_number]['position']
        current_energy = coders[current_player_number]['energy']
        current_money = coders[current_player_number]['bitcoins']

        # Access the missions' positions from the game_dict
        missions_positions = {tuple(m['position']): m for m in game_dict['missions']}

        if current_energy == 0:
            position_x_vise = 10
            position_y_vise = 10
            if current_position[0] != position_x_vise:
                if current_position[0] > position_x_vise:
                    return 'E'
                else:
                    return 'W'
            if current_position[1] != position_y_vise:
                if current_position[1] > position_y_vise:
                    return 'N'
                else:
                    return 'S'
            if current_money > 100:
                return 'L'
            return 'R'


        if current_energy > 0:

            position_x_vise = float('inf')  # Initialize with positive infinity to ensure any mission position is closer
            position_y_vise = float('inf')

            for mission_position, mission in missions_positions.items():

                if mission_position != current_position:

                    x, y = mission_position

                    differencex = abs(x - current_position[0])
                    differencey = abs(y - current_position[1])

                    # Check if the current mission is closer than the previously targeted mission
                    if differencex + differencey < abs(position_x_vise - current_position[0]) + abs(position_y_vise - current_position[1]):
                        position_x_vise = x
                        position_y_vise = y


            if current_position[0] != position_x_vise: # Vérifie si la coordonée x du joueur est en accords avec la coordonnée x de la mission

                if current_position[0] > position_x_vise:
                    return 'E'
                else:
                    return 'W'
            if current_position[1] != position_y_vise: # Vérifie si la coordonée y du joueur est en accords avec la coordonnée y de la mission
                if current_position[1] > position_y_vise:
                    return 'N'
                else:
                    return 'S'


    def game_over(self, game_dict: dict) -> None:
        """Appelé à la fin du jeu ; sert à ce que vous voulez

        Args:
            descr (str): descriptif du dernier tour de jeu
        """
        pass
