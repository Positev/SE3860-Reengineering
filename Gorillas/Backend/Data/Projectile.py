class Projectile:
    def __init__(self, 
                 initial_velocity: float, 
                 launch_angle: float, 
                 start_x:float, 
                 start_y: float, 
                 sender_id: str, 
                 sprite: int):

        self._initial_velocity = initial_velocity
        self._launch_angle = launch_angle
        self._start_x = start_x
        self._start_y = start_y
        self._flight_time = 0
        self._current_x = 0
        self._current_y = 0
        self._sender_id = sender_id
        self._sprite = sprite

    @property
    def initial_velocity(self) -> float:
        return self._initial_velocity

    @initial_velocity.setter
    def initial_velocity(self, value: float):
        self._initial_velocity = value

    @property
    def launch_angle(self) -> float:
        return self._launch_angle

    @launch_angle.setter
    def launch_angle(self, value: float):
        self._launch_angle = value

    @property
    def start_x(self) -> float:
        return self._start_x

    @start_x.setter
    def start_x(self, value: float):
        self._start_x = value

    @property
    def start_y(self) -> float:
        return self._start_y

    @start_y.setter
    def start_y(self, value: float):
        self._start_y = value



    @property
    def current_x(self) -> float:
        return self._current_x

    @current_x.setter
    def current_x(self, value: float):
        self._current_x = value

    @property
    def current_y(self) -> float:
        return self._current_y

    @current_y.setter
    def current_y(self, value: float):
        self._current_y = value





    @property
    def sender_id(self) -> str:
        return self._sender_id

    @sender_id.setter
    def sender_id(self, value: str):
        self._sender_id = value

    @property
    def flight_time(self) -> str:
        return self._flight_time

    
    def increment_flight_time(self):
        #TODO Probably can tune this value.
        self._flight_time += 2

    @property
    def sprite(self) -> int:
        return self._sprite

    @sprite.setter
    def sprite(self, value: int):
        #TODO Enforce that sprite is instance of enum
        self._sprite = value
