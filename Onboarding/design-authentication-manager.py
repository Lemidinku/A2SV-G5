class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens = {}
        self.time_to_live = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokens: return
        created_at = self.tokens[tokenId]
        if currentTime-created_at < self.time_to_live:
            self.tokens[tokenId] = currentTime
    def countUnexpiredTokens(self, currentTime: int) -> int:
        count =0 
        for created_at in self.tokens.values():
            if currentTime-created_at < self.time_to_live:
                count +=1
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)

# {"fuzxq": 5,"izmry":7, "ybiqb":21, "gm":14,}