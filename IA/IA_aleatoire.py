import random
from moteur_esn_wars import *


class IA_ESNW:
    def __init__(self, num_joueur: int, game_dict: dict) -> None:
        """Initialize the AI object.

        Args:
            num_joueur (int): Player number assigned to the AI.
            game_dict (dict): Initial state of the game.
        """
        print("IA num", num_joueur, "loaded: OK")

    def action(self, game_dict: dict) -> str:
        """Called for each decision of the AI player.

        Args:
            game_dict (dict): Description of the game state.

        Returns:
            str: An action 'N', 'S', 'E', 'W', 'L', or 'P'.
        """

        coders = game_dict['coders']
        current_player_number = 0  # Replace with the actual player number of your AI

        # Access the AI's current position
        current_position = coders[current_player_number]['position']
        current_energy = coders[current_player_number]['energy']
        current_money = coders[current_player_number]['bitcoins']

        # Access the missions' positions from the game_dict
        missions_positions = {tuple(m['position']): m for m in game_dict['missions']}

        if current_energy == 0:  # Si l'energie est à 0
            position_x_vise = 10  # On vise le game center
            position_y_vise = 10

            if current_position[0] != position_x_vise:  # On se deplace vers le game center

                return 'E' if current_position[0] > position_x_vise else 'W'

            if current_position[1] != position_y_vise:
                return 'N' if current_position[1] > position_y_vise else 'S'

            if current_money > 100 and current_position[0] == 10 and current_position[1] == 10:
                return 'L'

            return 'P'

        # If energy is not 0, et qu'on peut donc travailler
        if current_energy > 0:

            position_x_vise = float(
                'inf')  # On initialise une valeur visée infinie positive pour inclure toute mission possible
            position_y_vise = float('inf')

            for mission_position, mission in missions_positions.items():

                if mission_position != current_position:  # Si on est pas sure une mission :

                    x, y = mission_position

                    differencex = abs(x - current_position[0])
                    differencey = abs(y - current_position[1])

                    # Et que une mission possède un workload inferieur à l'energie, et un cooldown suffisant :
                    if mission['workload'] < current_energy and mission['cooldown'] < 4:

                        position_x_vise = x
                        position_y_vise = y

                        if current_position[0] != position_x_vise:  # On bouge vers cette mission
                            return 'E' if current_position[0] > position_x_vise else 'W'
                        if current_position[1] != position_y_vise:
                            return 'N' if current_position[1] > position_y_vise else 'S'

            for mission_position, mission in missions_positions.items():  # Lance une boucle pour constemment surveiller la liste

                if mission_position != current_position:

                    x, y = mission_position

                    # Calcule la différence entre la position du joueur, et la position de la mission
                    differencex = abs(x - current_position[0])
                    differencey = abs(y - current_position[1])

                    # Compare constemment les missions qui sont dans la liste avec la mission visée, si la distance de celle-ci est inférieur, choisi celle là.
                    if differencex + differencey < abs(position_x_vise - current_position[0]) + abs(position_y_vise - current_position[1]) and mission['cooldown'] < 2:

                        position_x_vise = x
                        position_y_vise = y

            if current_position[0] != position_x_vise:  # On bouge alors vers cette mission.

                return 'E' if current_position[0] > position_x_vise else 'W'

            if current_position[1] != position_y_vise:
                return 'N' if current_position[1] > position_y_vise else 'S'

        return 'P'

    def game_over(self, game_dict: dict) -> None:
        """Called at the end of the game; can be used for any specific actions.

        Args:
            game_dict (dict): Description of the last game turn.
        """
        pass
