class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)
        path1 = 0
        a,b = min(start,destination), max(start, destination)
        j = a
        while j <  b:
            path1 += distance[j]
            j+=1

        path2 = 0
        i = b
        while (i%n) !=  a:
            path2 += distance[i%n]
            i+=1
        return min(path1, path2)



        