# The gorilla controller shall modify the state of a gorilla class 
# after a gorilla is created, the only modifications to that class
# should be in the state of the arms.

# A controller is used to interact with this class with an eye towards
# future maintainence. I can see gorilla movement during the game to be a 
# feature request, or different kinds of gorillas and such

class TEMPGORILLAENUM:
  down = 0
  left_up = 1
  right_up = 2
  both_up = 3

class GorillaController:
  def __init__(self, gorilla):
    self.gorilla = gorilla

  def arms_down(self):
    self.gorilla.arm_state = TEMPGORILLAENUM.down
  
  def arms_up(self):
    self.gorilla.arm_state = TEMPGORILLAENUM.both_up
  
  def left_arm_up(self):
    self.gorilla.arm_state = TEMPGORILLAENUM.left_up
  
  def right_arm_up(self):
    self.gorilla.arm_state = TEMPGORILLAENUM.right_up