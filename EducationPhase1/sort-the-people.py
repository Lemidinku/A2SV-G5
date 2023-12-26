class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        k = len(names)
        while k>1:
            for i in range(k-1):
                if heights[i] < heights[i+1]:
                    heights[i], heights[i+1] = heights[i+1], heights[i]
                    names[i], names[i+1] = names[i+1], names[i]

            k-=1
        return names