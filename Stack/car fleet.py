class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = [[position[i], speed[i]] for i in range(len(speed))]
        fleets = 0
        curent_time = 0
        for dist, speed in sorted(pairs, reverse=True):
            dest_time = (target - dist) / speed
            if curent_time < dest_time:
                fleets += 1
                curent_time = dest_time

        return fleets


