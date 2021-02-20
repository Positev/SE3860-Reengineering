


# The gorilla class will repersent the state of a gorilla sprite that is controller by a player
# Ideally the x_pos and y_pos are float variables that reside on the top center of a Building rectangle
# player_id will link the gorilla class to the actual player.
# This class should provide the state information that allows the front end to render a gorilla that has
# its left arm up, right arm up, or both arms down at some position.
class Gorilla:

  def __init__(self, x_pos: float, y_pos: float, player_id: str):
    self._x_pos = x_pos
    self._y_pos = y_pos
    self._player_id = player_id
    self._arm_state = 0

  @property
  def x_pos(self) -> float:
      return self._x_pos

  @x_pos.setter
  def x_pos(self, value: float):
      self._x_pos = value

  @property
  def y_pos(self) -> float:
      return self._y_pos

  @y_pos.setter
  def y_pos(self, value: float):
      self._y_pos = value

  @property
  def player_id(self) -> str:
      return self._player_id

  @player_id.setter
  def player_id(self, value: str):
      self._player_id = value

  @property
  def arm_state(self) -> int:
      return self._arm_state

  @arm_state.setter
  def arm_state(self, value: int):
    #TODO enforce that value is an enum and change type hints to use enum
      self._arm_state = value