from Backend.Data.ScoreKeeper import ScoreKeeper
from Backend.Data.Wind import Wind


class GameState:
    def __init__(self, building, gorillas, active_projectiles, destruction, score, wind, turn_active):
        if (isinstance(building, list) and
                isinstance(gorillas, list) and
                isinstance(active_projectiles, list) and
                isinstance(destruction, list) and
                isinstance(score, ScoreKeeper) and  # TODO Should not be score keeper
                isinstance(wind, Wind) and
                isinstance(turn_active, bool)):
            self.__building = building
            self.__gorillas = gorillas
            self.__active_projectiles = active_projectiles
            self.__destruction = destruction
            self.__score = score
            self.__wind = wind
            self.__turn_active = turn_active
            self._player_turn = 0
            self.__is_game_over = False
            self.__winner_id = None
        else:
            raise Exception("Wrong type parameter.")

    def copy(self):
        gs = GameState(
            [build.copy() for build in self.__building],
            [g.copy() for g in self.__gorillas],
            [p.copy() for p in self.active_projectiles],
            [d.copy() for d in self.destruction],
            self.score.copy(),
            self.wind.copy(),
            self.turn_active
        )

        gs.__dict__.update(self.__dict__)
        return gs

    @property
    def building(self):
        return self.__building

    @building.setter
    def building(self, building):
        if (isinstance(building, list)):
            self.__building = building
        else:
            raise Exception("Wrong type parameter.")

    def active_player(self):
        return self.gorillas[self._player_turn]

    def next_player(self):
        # print(self._player_turn)
        # print(len(self.gorillas))
        self._player_turn = self._player_turn % len(self.gorillas) - 1

    @property
    def gorillas(self):
        return self.__gorillas

    @gorillas.setter
    def gorillas(self, gorillas):
        if (isinstance(gorillas, list)):
            self.__gorillas = gorillas
        else:
            raise Exception("Wrong type parameter.")

    @property
    def active_projectiles(self):
        return self.__active_projectiles

    @active_projectiles.setter
    def active_projectiles(self, active_projectiles):
        if (isinstance(active_projectiles, list)):
            self.__active_projectiles = active_projectiles
        else:
            raise Exception("Wrong type parameter.")

    @property
    def destruction(self):
        return self.__destruction

    @destruction.setter
    def destruction(self, destruction):
        if (isinstance(destruction, list)):
            self.__destruction = destruction
        else:
            raise Exception("Wrong type parameter.")

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if (isinstance(score, ScoreKeeper)):
            self.__score = score
        else:
            raise Exception("Wrong type parameter.")

    @property
    def wind(self):
        return self.__wind

    @wind.setter
    def wind(self, wind):
        if (isinstance(wind, Wind)):
            self.__wind = wind
        else:
            raise Exception("Wrong type parameter.")

    @property
    def turn_active(self):
        return self.__turn_active

    @turn_active.setter
    def turn_active(self, turn_active):
        if (isinstance(turn_active, bool)):
            self.__turn_active = turn_active
        else:
            raise Exception("Wrong type parameter.")

    def is_game_over(self):
        winner = self.__score.check_score_to_win()
        if winner is None:
            return False
        else:
            self.__winner_id = winner
            return True

    @property
    def winner(self):
        return self.__winner_id

    def __str__(self):

        newline = '\n'
        tabbednewline = '\n\t'
        out = [
            '-' * 90,
            f"Buildings: {tabbednewline}{tabbednewline.join([str(building) for building in self.building])}",
            f"Gorillas: {tabbednewline}{tabbednewline.join([str(gorilla) for gorilla in self.gorillas])}",
            f"Active Projectiles: {tabbednewline}{tabbednewline.join([str(projectile) for projectile in self.active_projectiles])}",
            f"World Destruction: {tabbednewline}{tabbednewline.join([str(destruction) for destruction in self.destruction])}",
            f"Score: {self.score}",
            f"Wind: {self.wind}",
            f"Turn Active: {self.turn_active}",
            '-' * 90,
        ]

        return '\n'.join(out)
