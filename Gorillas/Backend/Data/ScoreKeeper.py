class ScoreKeeper:

    def __init__(self, player_1_init_sorce=0, player_2_init_sorce=0):
        self.__score_dict = {0: player_1_init_sorce, 1: player_2_init_sorce}

    def __str__(self):
        out = [f"Player {_id} -> {score}" for _id, score in self.__score_dict.items()]
        return ',  '.join(out)

    def copy(self):
        s = ScoreKeeper()
        s.__dict__.update(self.__score_dict)
        return s

    @property
    def score_dict(self):
        return self.__score_dict

    def record_win(self, player_id):
        if player_id in self.__score_dict:
            self.__score_dict[player_id] += 1
        else:
            raise Exception("Input a bwrong player_id.")

    def get_score(self, player_id):
        return self.__score_dict[player_id]
