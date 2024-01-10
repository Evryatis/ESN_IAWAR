import random
from moteur_esn_wars import *
test = 1
COST_UPGRADE = 25

class IA_ESNW:
    global test
    global coût

    def __init__(self, num_joueur: int, game_dict: dict) -> None:
        """Initialize the AI object.

        Args:
            num_joueur (int): Player number assigned to the AI.
            game_dict (dict): Initial state of the game.
        """
        print("IA num", num_joueur, "loaded: OK")
        self.num_joueur = num_joueur


    def action(self, game_dict: dict) -> str:
        """Called for each decision of the AI player.

        Args:
            game_dict (dict): Description of the game state.

        Returns:
            str: An action 'N', 'S', 'E', 'W', 'L', or 'P'.
        """

        global test

        coders = game_dict['coders']
        coût = (coders[self.num_joueur]['level'] + 1) ** 2 * COST_UPGRADE

        liste_enemis = []
        nombre_enemis = 0
        for i in range(len(coders)):
            if coders[i]['position'] != coders[self.num_joueur]['position']:
                liste_enemis.append(coders[i])
                nombre_enemis += 1
        print(liste_enemis)

        # Accès aux valeurs nécessaire au fonctionnement de l'IA.
        current_position = coders[self.num_joueur]['position']
        current_energy = coders[self.num_joueur]['energy']
        current_money = coders[self.num_joueur]['bitcoins']
        current_level = coders[self.num_joueur]['level']
        current_max_energy = coders[self.num_joueur]['max_energy']

        # Accès aux missions du jeu.
        missions_positions = {tuple(m['position']): m for m in game_dict['missions']}



        if current_money > coût and current_position[0] == 10 and current_position[1] == 10 and current_level < 4 and current_max_energy < 4:

            if current_level < MAX_LEVEL and test == 1:

                test = 2
                return 'EM'

            else:

                test = 1
                return 'L'

        if current_energy == 0:  # Si l'energie est à 0

            position_x_vise = 10  # On vise le game center
            position_y_vise = 10

            if current_position[0] != position_x_vise:  # On se deplace vers le game center
                #for i in range(nombre_enemis):
                #    if liste_enemis[i]['position'][1] == current_position[1] -1:
                #        return 'N' if current_position[1] > position_y_vise else 'S'
                return 'W' if current_position[0] > position_x_vise else 'E'
            if current_position[1] != position_y_vise:
                #for i in range(nombre_enemis):
                #    if liste_enemis[i]['position'][1] == current_position[1] +1:
                #        return 'W' if current_position[0] > position_x_vise else 'E'
                return 'N' if current_position[1] > position_y_vise else 'S'


        # If energy is not 0, et qu'on peut donc travailler
        if current_energy > 0:

            position_x_vise = 100  # On initialise une valeur positive pour inclure toute mission possible
            position_y_vise = 100

            for mission_position, mission in missions_positions.items():

                if mission_position != current_position:  # Si on est pas sure une mission :

                    x, y = mission_position

                    differencex = abs(x - current_position[0])
                    differencey = abs(y - current_position[1])

                    # Et que une mission possède un workload inferieur à l'energie, et un cooldown suffisant :
                    if mission['workload'] < current_energy and mission['cooldown'] < 4 and mission['difficulty'] > 1:

                        if mission['difficulty'] <= current_level:
                            position_x_vise = x
                            position_y_vise = y

                            if current_position[0] != position_x_vise:  # On bouge vers cette mission

                                return 'W' if current_position[0] > position_x_vise else 'E'

                            if current_position[1] != position_y_vise:

                                return 'N' if current_position[1] > position_y_vise else 'S'

            for mission_position, mission in missions_positions.items():  # Lance une boucle pour constemment surveiller la liste

                if mission_position != current_position:

                    x, y = mission_position

                    # Calcule la différence entre la position du joueur, et la position de la mission
                    differencex = abs(x - current_position[0])
                    differencey = abs(y - current_position[1])

                    position_x_center = abs(10 - current_position[0])
                    position_y_center = abs(10 - current_position[1])

                    # Compare constemment les missions qui sont dans la liste avec la mission visée, si la distance de celle-ci est inférieur, choisi celle là.
                    if differencex + differencey < abs(position_x_vise - current_position[0]) + abs(position_y_vise - current_position[1]) and mission['cooldown'] < coders[self.num_joueur]['energy']:
                        position_x_vise = x
                        position_y_vise = y

            if current_position[0] != position_x_vise:  # On bouge alors vers cette mission.

                return 'W' if current_position[0] > position_x_vise else 'E'

            if current_position[1] != position_y_vise:
                
                return 'N' if current_position[1] > position_y_vise else 'S'

        return 'P'

    def game_over(self, game_dict: dict) -> None:
        """Called at the end of the game; can be used for any specific actions.

        Args:
            game_dict (dict): Description of the last game turn.
        """
        pass
