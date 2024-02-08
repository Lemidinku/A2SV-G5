class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        count =0
        holder = 0
        for seeker in range(len(s)):
            if s[seeker]=="0":
                s[holder],s[seeker] = s[seeker], s[holder]
                count += seeker-holder
                holder +=1
        return count