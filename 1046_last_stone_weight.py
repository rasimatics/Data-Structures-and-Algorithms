class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-1 * i for i in stones]
        heapq.heapify(arr)
                
        while len(arr) > 1:
            x = -1 * heapq.heappop(arr)
            y = -1 * heapq.heappop(arr)
            
                    
            if x != y:
                heapq.heappush(arr, y-x)
            
        return -1 * arr[0] if arr else 0