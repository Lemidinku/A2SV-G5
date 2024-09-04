# Problem: Robot Collisions - https://leetcode.com/problems/robot-collisions/

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = [[positions[i],i] for i in range(n)]
        robots.sort()
        stack = []
        for robot  in robots:
            ind = robot[1]
            dir = directions[ind]
            dead = False
            if stack and dir == "L" and directions[stack[-1][1]] == "R":
                while stack  and directions[stack[-1][1]] == "R":
                    prev_ind = stack[-1][1]
                    if healths[ind] > healths[prev_ind]:
                        stack.pop()
                        healths[ind] -=1
                    elif healths[ind] < healths[prev_ind]:
                        healths[prev_ind] -=1
                        dead  = True
                        break
                    else: 
                        dead  = True
                        stack.pop()
                        break
                if not dead: stack.append(robot)
            else: stack.append(robot)
        stack.sort( key = lambda x:x[-1])
        ans = [healths[a[1]] for a in stack]
        return ans