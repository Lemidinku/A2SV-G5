class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):  
        self.times = times     
        leader = 0
        self.leader_at_t = {}
        self.candidates = defaultdict(int)
        for person,time in zip(persons,self.times):
            self.candidates[person]+=1
            if self.candidates[person]>=self.candidates[leader]:
                leader = person
            self.leader_at_t[time] = leader

    def q(self, t: int) -> int:
        def getLeader(nums,target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid]==target:
                    return target
                elif (mid==len(nums)-1 or nums[mid+1]>target) and nums[mid] > target:
                    right = mid - 1
                else: left = mid + 1
            return nums[right]

        time = getLeader(self.times,t)
  
        return self.leader_at_t[time]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)