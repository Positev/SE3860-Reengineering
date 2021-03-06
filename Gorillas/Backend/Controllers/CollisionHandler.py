import pygame
from Backend.Data.Enumerators import CollisionResult
from Backend.Data.Collision import Collision

from Backend.Adapters.CoordinateAdapter import CoordinateAdapter


class CollisionHandler:

    @staticmethod
    def test_collisions(projectiles: list, buildings: list, players: list, screen_size):



        if projectiles and buildings and players:
            coordinate_adapter = CoordinateAdapter(screen_size)
            adapted_projectiles = coordinate_adapter.adapt_projectiles(projectiles)
            adapted_buildings = coordinate_adapter.adapt_buildings(buildings)
            adapted_gorillas = coordinate_adapter.adapt_gorillas(players)
            collisions = []
            for projectile in adapted_projectiles:
                for player in adapted_gorillas:
                    if pygame.sprite.collide_rect(projectile, player):
                        if player.player_id != projectile.sender_id:
                            collisions.append(Collision(projectile.current_x, projectile.current_y, CollisionResult(1), projectile.key(), player.player_id))
                for building in adapted_buildings:
                    if pygame.sprite.collide_rect(projectile, building):
                        collisions.append(Collision(projectile.current_x, projectile.current_y, CollisionResult(2), projectile.key(), building.key()))
            return collisions
        elif not buildings:
            raise Exception("The list of buildings is empty.")
        elif not players:
            raise Exception("The list of projectiles is empty.")
        return []