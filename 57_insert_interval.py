class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insertIndex = -1
        
        for i in range(len(intervals)):
            if newInterval[0] < intervals[i][0]:
                insertIndex = i
                break
        
        if insertIndex == -1:
            intervals.append(newInterval)
        else:
            intervals.insert(i, newInterval)
            
            
        return self.mergeIntervals(intervals)
            
        
    
    def mergeIntervals(self, intervals):
        res = [intervals[0]]
        
        
        for i in range(len(intervals)):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(intervals[i][1], res[-1][1])
        
        return res
                
                