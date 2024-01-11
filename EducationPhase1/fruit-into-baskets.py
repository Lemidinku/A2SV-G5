class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        window = defaultdict(int)
        types = 0
        left = 0
        max_fruits = 0
        for right in range(n):
            if not window[fruits[right]]:
                types+=1
            window[fruits[right]] +=1

            while types>2:
                window[fruits[left]] -= 1
                if not window[fruits[left]]:
                    types-=1
                left+=1

            max_fruits = max(max_fruits, right-left+1)
        return max_fruits

            
                
