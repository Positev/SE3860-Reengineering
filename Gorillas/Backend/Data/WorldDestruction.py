class WorldDestruction:
    def __init__(self, center_x, center_y, major_axis_dx, major_axis_dy, minor_axis_dx, minor_axis_dy):
        self.__center_x = center_x
        self.__center_y = center_y
        self.__major_axis_dx = major_axis_dx
        self.__major_axis_dy = major_axis_dy
        self.__minor_axis_dx = minor_axis_dx
        self.__minor_axis_dy = minor_axis_dy

    def copy(self):
        return WorldDestruction(self.center_x,
                                self.center_y,
                                self.major_axis_dx,
                                self.major_axis_dy,
                                self.minor_axis_dx,
                                self.minor_axis_dy)

    def __str__(self):
        out = [
            f"Center: ({self.center_x}, {self.center_y})"
            f"Major DX,DY: ({self.major_axis_dx}, {self.major_axis_dy})"
            f"Minor DX,DY: ({self.minor_axis_dx}, {self.minor_axis_dy})"
        ]

        return ','.join(out)

    def get_center(self):
        return self.__center_x, self.__center_y

    @property
    def center_x(self):
        return self.__center_x

    @center_x.setter
    def center_x(self, center_x):
        self.__center_x = center_x

    @property
    def center_y(self):
        return self.__center_y

    @center_y.setter
    def center_y(self, center_y):
        self.__center_y = center_y

    @property
    def major_axis_dx(self):
        return self.__major_axis_dx

    @major_axis_dx.setter
    def major_axis_dx(self, major_axis_dx):
        self.__major_axis_dx = major_axis_dx

    @property
    def major_axis_dy(self):
        return self.__major_axis_dy

    @major_axis_dy.setter
    def major_axis_dy(self, major_axis_dy):
        self.__major_axis_dy = major_axis_dy

    @property
    def minor_axis_dx(self):
        return self.__minor_axis_dx

    @minor_axis_dx.setter
    def minor_axis_dx(self, minor_axis_dx):
        self.__minor_axis_dx = minor_axis_dx

    @property
    def minor_axis_dy(self):
        return self.__minor_axis_dy

    @minor_axis_dy.setter
    def minor_axis_dy(self, minor_axis_dy):
        self.__minor_axis_dy = minor_axis_dy
