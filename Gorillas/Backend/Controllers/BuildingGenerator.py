from typing import Tuple, List
from Backend.Data.Building import Building
import random

BUILDING_RANGE = (5, 8)
#todo return to 40 and 60
BUILDING_HEIGHT_SCREEN_PERCENT_RANGE = (40, 50)
PERCENT_TO_DECIMAL = 1 / 100



# TODO make buildings generate in a pattern such as decend left,
# decent right, valley or crest instead of pure random values

class BuildingGenerator:


    GENERATED_BUILDING_COUNT = 0

    def generate_buildings(self, screen_size: Tuple[int, int]) -> List[Building]:
        generated_buildings = []
        num_buildings = random.randint(BUILDING_RANGE[0], BUILDING_RANGE[1])
        building_width = screen_size[0] / num_buildings  # TODO Make semi-randomized

        for building_index in range(num_buildings):
            building_height = random.randint(
                BUILDING_HEIGHT_SCREEN_PERCENT_RANGE[0],
                BUILDING_HEIGHT_SCREEN_PERCENT_RANGE[1]) * \
                              PERCENT_TO_DECIMAL * screen_size[1]
            new_building = Building(
                building_index * building_width,
                0,
                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                building_width,
                building_height, key=self.GENERATED_BUILDING_COUNT)
            self.GENERATED_BUILDING_COUNT += 1

            generated_buildings.append(new_building)

        return generated_buildings


if __name__ == '__main__':
    BuildingGenerator().generate_buildings((200, 300))
