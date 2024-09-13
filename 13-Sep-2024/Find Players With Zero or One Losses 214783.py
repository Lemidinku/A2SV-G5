# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        loses = defaultdict(int)
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            loses[loser]+=1

        all_winners = []
        one_losers = []
        for player in players:
            if loses[player]==0:
                all_winners.append(player)
            if loses[player]==1:
                one_losers.append(player)
        all_winners.sort()
        one_losers.sort()
        return [all_winners,one_losers]