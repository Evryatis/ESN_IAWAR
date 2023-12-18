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

        for mission_position, mission in missions_positions.items(): # Vérifie constemment la mission la plus proche du joueur
            if mission_position != current_position:
                position_x = current_position[0]
                position_y = current_position[1]
                position_x_vise = 0 # Variable x de la mission la plus proche
                position_y_vise = 0 # Variable y de la mission la plus proche

                for x, y in [mission_position]: # Calcule la différence de proximité entre la position visée et la meilleure position..
                    differencex = abs(x - current_position[0])
                    differencey = abs(y - current_position[1])

                    differencex1 = abs(x - position_x_vise)
                    differencey1 = abs(y - position_y_vise)

                    # Verifie si la mission vérifiée est plus proche ou pas de la current mission visée
                    if differencex + differencey < differencex1 + differencey1:
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
        if current_position == (position_x_vise, position_y_vise):
            return 'P'

    def game_over(self, game_dict: dict) -> None:
        """Appelé à la fin du jeu ; sert à ce que vous voulez

        Args:
            descr (str): descriptif du dernier tour de jeu
        """
        pass


