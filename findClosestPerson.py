class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        diff1 = abs(z - x)
        diff2 = abs(z - y) 

        if diff1 < diff2:
            return 1
        elif diff2 < diff1:
            return 2
        else:
            return 0
