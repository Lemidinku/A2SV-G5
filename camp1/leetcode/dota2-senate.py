class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        radias = senate.count("R")
        dires = senate.count("D")
        if not radias: return "Dire"
        if not dires: return "Radiant"
        queue = deque(senate)
        disabledRadias = disabledDires= 0
        while queue:
            # print(queue, radias, dires)
            voter = queue.popleft()
            if voter=="R":
                if disabledRadias:
                    disabledRadias -=1
                    radias -=1
                else:
                    queue.append("R")
                    disabledDires +=1
                    if dires==disabledDires: return "Radiant"

            else:
                if disabledDires:
                    disabledDires -=1
                    dires -=1
                else:
                    queue.append("D")
                    disabledRadias +=1
                    if radias==disabledRadias: return "Dire"
        






        return "Radiant"
