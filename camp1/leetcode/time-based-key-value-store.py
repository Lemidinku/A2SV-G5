class TimeMap:

    def __init__(self):
        self.table = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        def maxTime(timeList, target):
            left = 0
            right = len(timeList) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if (mid == len(timeList)-1 or timeList[mid + 1][0] > target) and timeList[mid][0] <= target:
                    return timeList[mid][1]
                if timeList[mid][0] >= target:
                    right = mid - 1
                else:
                    left = mid + 1

            return  ""
        return maxTime(self.table[key], timestamp)
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)