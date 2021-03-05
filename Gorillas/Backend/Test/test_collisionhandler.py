import unittest
from Backend.Controllers.CollisionHandler import CollisionHandler
from Backend.Data.Projectile import Projectile
from Backend.Data.Building import Building
from Backend.Data.Gorilla import Gorilla
from Backend.Data.Enumerators import GorillaLocation
from Backend.Data.Enumerators import CollisionResult
from typing import Tuple


class TestCollisionHandler(unittest.TestCase):

    def test_test_collisions_single_projectile(self):
        project1 = Projectile(10, 45, 0, 0, 'project1', 5)
        project1.current_x = 200
        project1.current_y = 200
        projects = [project1]
        building1 = Building(200, 50, (172, 145, 244), 50, 150)
        building2 = Building(230, 200, (172, 145, 244), 50, 150)
        building3 = Building(200, 220, (172, 145, 244), 50, 150)
        building4 = Building(150, 70, (172, 145, 244), 50, 150)
        buildings = [building1, building2, building3, building4]
        player1 = Gorilla(200, 150, 'player1', GorillaLocation.LEFT)
        player2 = Gorilla(230, 200, 'player2', GorillaLocation.LEFT)
        player3 = Gorilla(180, 220, 'player3', GorillaLocation.LEFT)
        player4 = Gorilla(150, 170, 'player4', GorillaLocation.LEFT)
        players = [player1, player2, player3, player4]
        clist = CollisionHandler.test_collisions(projects, buildings, players)
        self.assertEqual(0, len(clist))

        projects[0].current_x = 201
        projects[0].current_y = 200
        clist = CollisionHandler.test_collisions(projects, buildings, players)
        self.assertEqual(2, len(clist))
        self.assertEqual(201, clist[0].x_pos)
        self.assertEqual(200, clist[0].y_pos)
        self.assertEqual(CollisionResult.PLAYER_HIT, clist[0].collision_result)
        self.assertEqual(201, clist[1].x_pos)
        self.assertEqual(200, clist[1].y_pos)
        self.assertEqual(CollisionResult.BUILDING_HIT, clist[1].collision_result)

        projects[0].current_x = 200
        projects[0].current_y = 201
        clist = CollisionHandler.test_collisions(projects, buildings, players)
        self.assertEqual(2, len(clist))
        self.assertEqual(200, clist[0].x_pos)
        self.assertEqual(201, clist[0].y_pos)
        self.assertEqual(CollisionResult.PLAYER_HIT, clist[0].collision_result)
        self.assertEqual(200, clist[1].x_pos)
        self.assertEqual(201, clist[1].y_pos)
        self.assertEqual(CollisionResult.BUILDING_HIT, clist[1].collision_result)

        projects[0].current_x = 199
        projects[0].current_y = 200
        clist = CollisionHandler.test_collisions(projects, buildings, players)
        self.assertEqual(2, len(clist))
        self.assertEqual(199, clist[0].x_pos)
        self.assertEqual(200, clist[0].y_pos)
        self.assertEqual(CollisionResult.PLAYER_HIT, clist[0].collision_result)
        self.assertEqual(199, clist[1].x_pos)
        self.assertEqual(200, clist[1].y_pos)
        self.assertEqual(CollisionResult.BUILDING_HIT, clist[1].collision_result)

        projects[0].current_x = 200
        projects[0].current_y = 199
        clist = CollisionHandler.test_collisions(projects, buildings, players)
        self.assertEqual(2, len(clist))
        self.assertEqual(200, clist[0].x_pos)
        self.assertEqual(199, clist[0].y_pos)
        self.assertEqual(CollisionResult.PLAYER_HIT, clist[0].collision_result)
        self.assertEqual(200, clist[1].x_pos)
        self.assertEqual(199, clist[1].y_pos)
        self.assertEqual(CollisionResult.BUILDING_HIT, clist[1].collision_result)

        player1 = Gorilla(1200, 150, 'player1', GorillaLocation.LEFT)
        player2 = Gorilla(1230, 200, 'player2', GorillaLocation.LEFT)
        player3 = Gorilla(1180, 220, 'player3', GorillaLocation.LEFT)
        player4 = Gorilla(1150, 170, 'player4', GorillaLocation.LEFT)
        players = [player1, player2, player3, player4]
        projects[0].current_x = 201
        projects[0].current_y = 200
        clist = CollisionHandler.test_collisions(projects, buildings, players)
        self.assertEqual(1, len(clist))
        self.assertEqual(CollisionResult.BUILDING_HIT, clist[0].collision_result)

        projects[0].current_x = 200
        projects[0].current_y = 201
        clist = CollisionHandler.test_collisions(projects, buildings, players)
        self.assertEqual(1, len(clist))
        self.assertEqual(CollisionResult.BUILDING_HIT, clist[0].collision_result)

        projects[0].current_x = 199
        projects[0].current_y = 200
        clist = CollisionHandler.test_collisions(projects, buildings, players)
        self.assertEqual(1, len(clist))
        self.assertEqual(CollisionResult.BUILDING_HIT, clist[0].collision_result)

        projects[0].current_x = 200
        projects[0].current_y = 199
        clist = CollisionHandler.test_collisions(projects, buildings, players)
        self.assertEqual(1, len(clist))
        self.assertEqual(CollisionResult.BUILDING_HIT, clist[0].collision_result)


        building1 = Building(1200, 50, (172, 145, 244), 50, 150)
        building2 = Building(1230, 200, (172, 145, 244), 50, 150)
        building3 = Building(1200, 220, (172, 145, 244), 50, 150)
        building4 = Building(1150, 70, (172, 145, 244), 50, 150)
        buildings = [building1, building2, building3, building4]
        player1 = Gorilla(200, 150, 'player1', GorillaLocation.LEFT)
        player2 = Gorilla(230, 200, 'player2', GorillaLocation.LEFT)
        player3 = Gorilla(180, 220, 'player3', GorillaLocation.LEFT)
        player4 = Gorilla(150, 170, 'player4', GorillaLocation.LEFT)
        players = [player1, player2, player3, player4]
        projects[0].current_x = 201
        projects[0].current_y = 200
        clist = CollisionHandler.test_collisions(projects, buildings, players)
        self.assertEqual(1, len(clist))
        self.assertEqual(CollisionResult.PLAYER_HIT, clist[0].collision_result)

        projects[0].current_x = 200
        projects[0].current_y = 201
        clist = CollisionHandler.test_collisions(projects, buildings, players)
        self.assertEqual(1, len(clist))
        self.assertEqual(CollisionResult.PLAYER_HIT, clist[0].collision_result)

        projects[0].current_x = 199
        projects[0].current_y = 200
        clist = CollisionHandler.test_collisions(projects, buildings, players)
        self.assertEqual(1, len(clist))
        self.assertEqual(CollisionResult.PLAYER_HIT, clist[0].collision_result)

        projects[0].current_x = 200
        projects[0].current_y = 199
        clist = CollisionHandler.test_collisions(projects, buildings, players)
        self.assertEqual(1, len(clist))
        self.assertEqual(CollisionResult.PLAYER_HIT, clist[0].collision_result)






    def test_test_collisions_multiple_projectiles(self):
        project1 = Projectile(10, 45, 0, 0, 'project1', 5)
        project1.current_x = 200
        project1.current_y = 200
        project2 = Projectile(10, 45, 0, 0, 'project1', 5)
        project2.current_x = 200
        project2.current_y = 210
        projects = [project1, project2]
        building1 = Building(200, 50, (172, 145, 244), 50, 150)
        building2 = Building(230, 80, (172, 145, 244), 50, 150)
        building3 = Building(180, 230, (172, 145, 244), 50, 150)
        building4 = Building(150, 80, (172, 145, 244), 50, 150)
        buildings = [building1, building2, building3, building4]
        player1 = Gorilla(1200, 1150, 'player1', GorillaLocation.LEFT)
        players = [player1]
        clist = CollisionHandler.test_collisions(projects, buildings, players)
        self.assertEqual(0, len(clist))

        projects[0].current_x = 201
        projects[0].current_y = 200
        clist = CollisionHandler.test_collisions(projects, buildings, players)
        self.assertEqual(1, len(clist))
        self.assertEqual(CollisionResult.BUILDING_HIT, clist[0].collision_result)
        projects[1].current_x = 201
        projects[1].current_y = 210
        clist = CollisionHandler.test_collisions(projects, buildings, players)
        self.assertEqual(2, len(clist))
        self.assertEqual(CollisionResult.BUILDING_HIT, clist[0].collision_result)
        self.assertEqual(CollisionResult.BUILDING_HIT, clist[1].collision_result)

        projects[0].current_x = 201
        projects[0].current_y = 200
        projects[1].current_x = 199
        projects[1].current_y = 210
        clist = CollisionHandler.test_collisions(projects, buildings, players)
        self.assertEqual(2, len(clist))
        self.assertEqual(CollisionResult.BUILDING_HIT, clist[0].collision_result)
        self.assertEqual(CollisionResult.BUILDING_HIT, clist[1].collision_result)

