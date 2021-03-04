from enum import Enum, unique

@unique
class ArmState(Enum):
    ARM_DOWN = 0
    LEFT_ARM_UP = 1
    RIGHT_ARM_UP = 2
    BOTH_ARM_UP = 3

@unique
class GorillaLocation(Enum):
    LEFT = 0
    RIGHT = 1

@unique
class ProjectileTravelDirection(Enum):
    LEFT = 0
    RIGHT = 1

@unique
class ProjectileSprite(Enum):
    BANANA = 0

@unique
class WindDirection(Enum):
    LEFT = 0
    RIGHT = 1

@unique
class CollisionResult(Enum):
    NO_HIT = 0
    PLAYER_HIT = 1
    BUILDING_HIT= 2