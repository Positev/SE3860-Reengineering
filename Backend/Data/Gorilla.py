


# The gorilla class will repersent the state of a gorilla sprite that is controller by a player
# Ideally the x_pos and y_pos are float variables that reside on the top center of a Building rectangle
# player_id will link the gorilla class to the actual player.
# This class should provide the state information that allows the front end to render a gorilla that has
# its left arm up, right arm up, or both arms down at some position.
class Gorilla:

  def __init__(self, x_pos: float, y_pos: float, player_id):
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.player_id = player_id