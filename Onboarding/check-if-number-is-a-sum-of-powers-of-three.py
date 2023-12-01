class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        num = 0
        x = 16
        while x>=0:
            if num + 3**x < n:
                num += 3**x
            elif num + 3**x == n:
                return True
            x -= 1
        return False


        # 1, 2, 3, 4, 5, 6, ...., 12, 13, 14, 16