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
                        collisions.append(Collision(projectile.current_x, projectile.current_y, CollisionResult(1)))
                for building in buildings:
                    if pygame.sprite.collide_rect(projectile, building):
                        collisions.append(Collision(projectile.current_x, projectile.current_y, CollisionResult(2)))
            return collisions
        elif not projectiles:
            raise Exception("The list of projectiles is empty.")
        elif not projectiles:
            raise Exception("The list of buildings is empty.")
        else:
            raise Exception("The list of projectiles is empty.")
