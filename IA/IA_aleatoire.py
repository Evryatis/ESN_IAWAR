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

        coders = game_dict['coders']
        current_player_number = 0  # Replace with the actual player number of your AI

        # Access the AI's current position
        current_position = coders[current_player_number]['position']

        # Access the missions' positions from the game_dict
        missions_positions = {tuple(m['position']): m for m in game_dict['missions']}

        for mission_position, mission in missions_positions.items():
            if mission_position != current_position:
                position_x = current_position[0]
                position_y = current_position[1]
                position_x_vise = 0
                position_y_vise = 0

                for x, y in [mission_position]:
                    differencex = abs(x - current_position[0])
                    differencey = abs(y - current_position[1])

                    differencex1 = abs(x - position_x_vise)
                    differencey1 = abs(y - position_y_vise)

                    # Check if the current mission is closer
                    if differencex + differencey < differencex1 + differencey1:
                        position_x_vise = x
                        position_y_vise = y

        # Rest of your code
        # Return a random action for now (replace this with your logic)
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
        if current_position == (position_x_vise, position_y_vise):
            return 'P'

    def game_over(self, game_dict: dict) -> None:
        """Appelé à la fin du jeu ; sert à ce que vous voulez

        Args:
            descr (str): descriptif du dernier tour de jeu
        """
        pass

