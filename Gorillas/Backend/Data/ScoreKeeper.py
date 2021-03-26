class ScoreKeeper:

    def __init__(self, player_1_id: str, player_2_id: str, score_to_win, player_1_init_score=0, player_2_init_score=0):
        self._player_1_id = player_1_id
        self._player_2_id = player_2_id
        self.__score_dict = {player_1_id: player_1_init_score, player_2_id: player_2_init_score}
        self._score_to_win = score_to_win

    def __str__(self):
        out = [f"Player {_id} -> {score}" for _id, score in self.__score_dict.items()]
        return ',  '.join(out)

    def copy(self):
        s = ScoreKeeper(self._player_1_id, self._player_2_id, self._score_to_win)
        s.__dict__.update(self.__score_dict)
        return s

    def check_score_to_win(self) -> str:
        if self.__score_dict[self._player_1_id] < self._score_to_win \
                and self.__score_dict[self._player_2_id] < self._score_to_win:
            return None
        elif self.__score_dict[self._player_1_id] >= self._score_to_win:
            return self._player_1_id
        else:
            return self._player_2_id

    @property
    def score_dict(self):
        return self.__score_dict

    @property
    def score_to_win(self):
        return self._score_to_win

    def record_win(self, player_id):
        if player_id in self.__score_dict.keys():
            self.__score_dict[player_id] += 1
        else:
            raise Exception("Input a wrong player_id.")

    def get_score(self, player_id):
        return self.__score_dict[player_id]
