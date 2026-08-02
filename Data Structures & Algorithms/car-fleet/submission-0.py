class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        matrix = []
        for i in range(len(position)):
            matrix.append([position[i], (target - position[i]) / speed[i]])
        matrix.sort(key=lambda x: x[0], reverse=True)

        result = 0
        slowest = 0.0
        for pos, t in matrix:
            if t > slowest:          # can't catch the fleet ahead
                result += 1
                slowest = t          # this car now leads, at its own pace
        return result