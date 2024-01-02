class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        max_processing_time = 0
        j = 0
        i = 0
        while j<len(tasks):
            max_processing_time = max(max_processing_time, tasks[j]+processorTime[i])
            i+=1
            j+=4
        return max_processing_time