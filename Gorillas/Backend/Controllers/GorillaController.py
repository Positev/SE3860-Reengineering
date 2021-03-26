# The gorilla controller shall modify the state of a gorilla class 
# after a gorilla is created, the only modifications to that class
# should be in the state of the arms.

# A controller is used to interact with this class with an eye towards
# future maintainence. I can see gorilla movement during the game to be a 
# feature request, or different kinds of gorillas and such
from Backend.Data.Enumerators import GorillaLocation, ArmState

ARM_UP_TIME = 10


class GorillaController:
    def __init__(self, gorilla):
        self.gorilla = gorilla

    def arms_down(self):
        self.gorilla.arm_state = ArmState.ARM_DOWN
        self.gorilla.arm_state_clock = 0

    def arms_up(self, time):
        self.gorilla.arm_state = ArmState.BOTH_ARM_UP
        self.gorilla.arm_state_clock = time

    def left_arm_up(self, time=ARM_UP_TIME):
        self.gorilla.arm_state = ArmState.LEFT_ARM_UP
        self.gorilla.arm_state_clock = time

    def right_arm_up(self, time=ARM_UP_TIME):
        self.gorilla.arm_state = ArmState.RIGHT_ARM_UP
        self.gorilla.arm_state_clock = time

    def throw(self):
        if self.gorilla.location == GorillaLocation.LEFT:
            self.right_arm_up()
        else:
            self.left_arm_up()

    def handle_new_frame(self):
        self.gorilla.decrement_clock()
        if self.gorilla.arm_state_clock == 0:
            self.arms_down()
