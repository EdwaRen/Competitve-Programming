import collections

class UndergroundSystem(object):

    def __init__(self):
        self.check_locations = collections.defaultdict(tuple)
        self.averages = collections.defaultdict(list)

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.check_locations[id] = (stationName, t)


    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        prev_station, prev_time = self.check_locations[id]
        self.averages[(prev_station, stationName)].append(t-prev_time)


    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        previous_times = self.averages[(startStation, endStation)]
        return float(sum(previous_times))/len(previous_times)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(10, "Leyton", 3)
undergroundSystem.checkOut(10, "Paradise", 8)
undergroundSystem.getAverageTime("Leyton", "Paradise") # return 5.00000
undergroundSystem.checkIn(5, "Leyton", 10)
undergroundSystem.checkOut(5, "Paradise", 16)
undergroundSystem.getAverageTime("Leyton", "Paradise") # return 5.50000
undergroundSystem.checkIn(2, "Leyton", 21)
undergroundSystem.checkOut(2, "Paradise", 30)
undergroundSystem.getAverageTime("Leyton", "Paradise") # return 6.66667