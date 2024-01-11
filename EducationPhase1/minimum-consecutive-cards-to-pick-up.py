class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        
        left = 0
        freq = defaultdict(int)
        min_len = float("inf")

        
        for right in range(len(cards)):
            freq[cards[right]] += 1

            while freq[cards[right]] > 1:
                freq[cards[left]]-=1
                min_len = min(min_len,right-left+1)
                left+=1

        if min_len>len(cards): return -1
        return min_len


