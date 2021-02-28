from typing import Tuple
import pygame



class Building:
    def __init__(self, x_pos: float, y_pos: float, color: Tuple[int,int,int], width:float, height:float ):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        self.width = width
        self.height = height

    def __str__(self):
        return f"X: {self._x_pos}, Y:{self._y_pos}, Color: {self._color}, Width: {self._width}, Height: {self._height}"

    def get_pos(self):
        return self.x_pos, self.y_pos


    def top_center(self) -> Tuple[float,float]:
        x = self.x_pos + self.width / 2
        y = self.height
        return x, y

    def copy(self):
        return Building(self.x_pos,self.y_pos, tuple(c for c in self.color), self.width, self.height)

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
    def y_pos(self, value: float ):
        self._y_pos = value

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float):
        self._width = value
    
    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = value

    @property
    def color(self) -> Tuple[int, int, int]:
        return self._color

    @color.setter
    def color(self, value: Tuple[int,int,int]):
        if type(value) is not tuple:
            raise ValueError(f"{value} is not a valid color.")

        for val in value:
            if type(val) is not int:
                raise ValueError(f"{val} must be an integer, but {val} is {type(val)}. So {value} is not a valid color.")
            if not (0 <= val <= 255):
                raise ValueError(f"{val} must be between 0 and 255. {value} is not a valid color.")
        self._color = value

    @property
    def rect(self):
        return pygame.Rect(self._x_pos, self._y_pos, self._width, self._height)
