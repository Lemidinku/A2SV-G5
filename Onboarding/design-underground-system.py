class UndergroundSystem:

    def __init__(self):
        self.checked_in = {}
        self.average_time = {}


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checked_in[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station,start_time = self.checked_in[id]
        travel_time = t-start_time

        if (start_station,stationName) in self.average_time:
            # get current average time
            tot_time,travel_num =  self.average_time[(start_station,stationName)]
            self.average_time[(start_station,stationName)] = [tot_time+travel_time,travel_num+1]
        else:
            self.average_time[(start_station,stationName)] = [travel_time,1]
            
        del self.checked_in[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        tot_sum, n = self.average_time[(startStation,endStation)]
        return tot_sum/n

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)