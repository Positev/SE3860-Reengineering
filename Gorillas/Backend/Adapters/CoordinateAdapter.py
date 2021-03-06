from Backend.Data.GameState import GameState


class CoordinateAdapter:

    def __init__(self, screen_size):
        self._screen_size = screen_size

    def _to_top_left_origin_ucs(self, value):
        out = value[0], self._screen_size[1] - value[1]
        return out

    def adapt_projectiles(self, active_projectiles):
        projectiles = []
        for projectile in active_projectiles:

            old_pos = projectile.get_pos()
            cur_pos = self._to_top_left_origin_ucs(old_pos)
            size = projectile.get_size()
            start = self._to_top_left_origin_ucs((projectile.start_x, projectile.start_y))
            cur_pos = cur_pos[0], cur_pos[1]
            adapted_projectile = projectile.copy()

            adapted_projectile.start_x, adapted_projectile.start_y = start
            adapted_projectile.current_x, adapted_projectile.current_y = cur_pos
            adapted_projectile.width, adapted_projectile.height = size
            projectiles.append(adapted_projectile)

        return projectiles

    def adapt_buildings(self, old_buildings):
        buildings = []
        for building in old_buildings:
            new_buidling = building.copy()
            pos = self._to_top_left_origin_ucs(new_buidling.get_pos())

            new_buidling.x_pos, new_buidling.y_pos = pos[0], pos[1]-new_buidling.height
            buildings.append(new_buidling)
        return buildings

    def adapt(self, game_state: GameState) -> GameState:
        adapted_game_state = game_state.copy()

        for gorilla in adapted_game_state.gorillas:
            in_ucs = self._to_top_left_origin_ucs(gorilla.get_pos())
            gorilla.x_pos, gorilla.y_pos = in_ucs

        adapted_game_state.active_projectiles = self.adapt_projectiles(adapted_game_state.active_projectiles)

        for destruction in adapted_game_state.destruction:
            center = self._to_top_left_origin_ucs(destruction.get_center())

            destruction.center_x, destruction.center_y = center

        adapted_game_state.building = self.adapt_buildings(adapted_game_state.building)







        return adapted_game_state
