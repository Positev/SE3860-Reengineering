from Backend.Data.GameState import GameState


class CoordinateAdapter:

    def __init__(self, screen_size):
        self._screen_size = screen_size

    def _to_top_left_origin_ucs(self, value):
        return value[0], self._screen_size[1] - value[1]

    def adapt(self, game_state: GameState) -> GameState:
        adapted_game_state = game_state.copy()

        for gorilla in adapted_game_state.gorillas:
            in_ucs = self._to_top_left_origin_ucs(gorilla.get_pos())
            gorilla.x_pos, gorilla.y_pos = in_ucs

        for projectile in adapted_game_state.active_projectiles:
            cur_pos = self._to_top_left_origin_ucs(projectile.get_pos())
            size = self._to_top_left_origin_ucs(projectile.get_size())
            start = self._to_top_left_origin_ucs((projectile.start_x,projectile.start_y))

            projectile.start_x, projectile.start_y = start
            projectile.current_x, projectile.current_x = cur_pos
            projectile.width, projectile.height = size

        for destruction in adapted_game_state.destruction:
            center = self._to_top_left_origin_ucs(destruction.get_center())

            destruction.center_x, destruction.center_y = center

        for building in adapted_game_state.building:
            pos = self._to_top_left_origin_ucs(building.get_pos())

            building.x_pos, building.y_pos = pos





        return adapted_game_state
