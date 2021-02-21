class Score:

    def __init__(self, init_sorce = 0):
        self.__score_dict = {0: init_sorce, 1: init_sorce}

    def record_win(self, player_id):
        if player_id in self.__score_dict:
            self.__score_dict[player_id] += 1
        else:
            raise Exception("Input a bwrong player_id.")

    def display(self):
        print(str(self.__score_dict[0]) + '=>' + str(self.__score_dict[0]))


s = Score()
s.record_win(0)
s.record_win(0)

s.display()
