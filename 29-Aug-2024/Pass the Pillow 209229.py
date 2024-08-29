# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i = 0
        dir = 1
        while time:
            i+=dir
            if i==n-1:
                dir=-1
            elif i==0:
                dir = 1
            time -=1
        return i+1
