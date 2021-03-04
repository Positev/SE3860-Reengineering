import pygame
from Backend.Data.Enumerators import CollisionResult
from Backend.Data.Collision import Collision


class CollisionHandler:

    @staticmethod
    def test_collisions(projectiles: list, buildings: list, players: list):
        if projectiles and buildings and players:
            collisions = []
            for projectile in projectiles:
                for player in players:
                    if pygame.sprite.collide_rect(projectile, player):
                        if player.player_id != projectile.sender_id:
                            collisions.append(Collision(projectile.current_x, projectile.current_y, CollisionResult(1), projectile.key(), player.player_id))
                for building in buildings:
                    if pygame.sprite.collide_rect(projectile, building):
                        collisions.append(Collision(projectile.current_x, projectile.current_y, CollisionResult(2), projectile.key(), building.key()))
            return collisions
        elif not buildings:
            raise Exception("The list of buildings is empty.")
        elif not players:
            raise Exception("The list of projectiles is empty.")
        return []