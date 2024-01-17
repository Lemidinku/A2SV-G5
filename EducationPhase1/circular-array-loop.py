class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n= len(nums)
        visited = set()

        for i,val in enumerate(nums):

            path = set()
            path.add(i)
            nextt = (i+val)%n


            if i in visited: 
                continue

            # for path with legth == 1
            if i==nextt: 
                visited.add(i)

            while nextt not in visited and val*nums[nextt] > 0:
                if nextt == (nextt+nums[nextt])%n:
                    visited.add(nextt)
                    path = set()
                    break
                if nextt in path:
                    return True

                    
                path.add(nextt)
                nextt = (nextt+nums[nextt])%n

            visited.update(path)
            
        return False
                
