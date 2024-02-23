class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        ends = {}
        for i in reversed(range(len(s))):
            if s[i] not in ends:
                ends[s[i]] = i
        
        curr_start = 0
        curr_end = -1
        partitions = []
        for i in range(len(s)):
            if curr_end < ends[s[i]]:
                curr_end = ends[s[i]]

            if curr_end==i:
                partitions.append(curr_end-curr_start+1)
                curr_start =curr_end+1

        return partitions
            
























        