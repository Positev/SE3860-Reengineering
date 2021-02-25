from WorldDestruction import WorldDestruction
from Wind import Wind
from ScoreKeeper import ScoreKeeper


class GameState:
    def __init__(self, building, gorillas, active_projectiles, destruction, score, wind, turn_active):
        if(isinstance(building, list) and
           isinstance(gorillas, list) and
           isinstance(active_projectiles, list) and
           isinstance(destruction, list) and
           isinstance(score, ScoreKeeper) and
           isinstance(wind, Wind) and
           isinstance(turn_active, bool)):
            self.__building = building
            self.__gorillas = gorillas
            self.__active_projectiles = active_projectiles
            self.__destruction = destruction
            self.__score = score
            self.__wind = wind
            self.__turn_active = turn_active
        else:
             raise Exception("Wrong type parameter.")

    @property
    def building(self):
        return self.__building

    @building.setter
    def building(self, building):
        if (isinstance(building, list)):
            self.__building = building
        else:
            raise Exception("Wrong type parameter.")

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