from enum import Enum, unique

@unique
class ArmState(Enum):
    ARM_DOWN = 0
    LEFT_ARM_UP = 1
    RIGHT_ARM_UP = 2


@unique
class ProjectileSprite(Enum):
    BANANA = 0
    BANANA = 1

@unique
class WindDirection(Enum):
    LEFT = 0
    RIGHT = 1