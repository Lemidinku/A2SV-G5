class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        # 4, 3, 3, 1, 2, 2, 1, 1, 1

        n = len(plants)
        steps = 0
        available = capacity
        for i,need in enumerate(plants):
            if available>= need:
                steps+=1
            else:
                steps += (2*i)
                available = capacity 
                steps +=1
            available -=need
        return steps


























