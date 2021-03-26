import random
from typing import Tuple, List

from Backend.Data.Building import Building
from Backend.Physics.PymunkBuilding import PymunkBuilding

BUILDING_RANGE = (5, 8)
# todo return to 40 and 60
BUILDING_HEIGHT_SCREEN_PERCENT_RANGE = (30, 60)
PERCENT_TO_DECIMAL = 1 / 100


# TODO make buildings generate in a pattern such as decend left,
# decent right, valley or crest instead of pure random values

class BuildingGenerator:
    GENERATED_BUILDING_COUNT = 0

    def generate_buildings(self, screen_size: Tuple[int, int]) -> List[Building]:
        choices = [self._generate_random_buildings, self._generate_hill_terrain]
        return random.choice(choices)(screen_size)

    def _generate_random_buildings(self, screen_size: Tuple[int, int]) -> List[Building]:
        generated_buildings = []
        num_buildings = random.randint(BUILDING_RANGE[0], BUILDING_RANGE[1])
        building_width = screen_size[0] / num_buildings  # TODO Make semi-randomized

        for building_index in range(num_buildings):
            building_height = random.randint(
                BUILDING_HEIGHT_SCREEN_PERCENT_RANGE[0],
                BUILDING_HEIGHT_SCREEN_PERCENT_RANGE[1]) * \
                              PERCENT_TO_DECIMAL * screen_size[1]
            new_building = PymunkBuilding(
                building_index * building_width,
                0,
                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                building_width,
                building_height, key=self.GENERATED_BUILDING_COUNT)
            self.GENERATED_BUILDING_COUNT += 1

            generated_buildings.append(new_building)

        return generated_buildings

    # hands down the worst code ive written in years
    def _generate_hill_terrain(self, screen_size: Tuple[int, int]):
        generated_buildings = []
        num_buildings = random.randint(int(BUILDING_RANGE[0]), int(BUILDING_RANGE[1]))
        building_range = list(range(num_buildings))
        building_width = screen_size[0] / num_buildings
        base_percentile = 30
        delta = 3
        buildings_ranges = (
        [range(base_percentile + (i * delta), base_percentile + ((i + 1) * delta)) for i in range(num_buildings + 1)])

        tallest_building_index = random.randint(0, num_buildings)
        left_buildings, right_buildings = building_range[0: tallest_building_index], building_range[
                                                                                     tallest_building_index + 1:]

        buildings_ranges_l = [b for b in buildings_ranges]
        buildings_ranges_r = [b for b in buildings_ranges]
        buildings_ranges_l.pop()
        buildings_ranges_r.pop()

        arranged_ranges = {}
        for index in reversed(range(len(left_buildings))):
            arranged_ranges[index] = buildings_ranges_l.pop()
        arranged_ranges[tallest_building_index] = buildings_ranges.pop()
        for index in range(len(right_buildings)):
            arranged_ranges[tallest_building_index + index + 1] = buildings_ranges_r.pop()

        for building_index, height_range in arranged_ranges.items():
            height_range = list(height_range)
            height_range = min(height_range), max(height_range)
            building_height = random.randint(*height_range) * \
                              PERCENT_TO_DECIMAL * screen_size[1]
            new_building = PymunkBuilding(
                building_index * building_width,
                0,
                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                building_width,
                building_height, key=self.GENERATED_BUILDING_COUNT)
            self.GENERATED_BUILDING_COUNT += 1

            generated_buildings.append(new_building)

        generated_buildings.sort(key=lambda building: building.x_pos)

        for i in range(len(generated_buildings)):
            generated_buildings[i]._key = i

        return generated_buildings


if __name__ == '__main__':
    buildings = BuildingGenerator()._generate_hill_terrain((200, 300))
    for b in buildings:
        print(b)
