class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:   
        occ = {}
        for i in nums:
            occ[i] = occ.get(i, 0) + 1
            
        bucket = [[] for _ in range(len(nums) + 1)]
        for val, occ in occ.items():
            bucket[occ].append(val)
        
        
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res
        
#--------- My first solution with buble sort ---------
#         numbers = list(occ.keys())
#         occurencies = list(occ.values())
        
#         for i in range(len(occurencies)):
#             for j in range(0, len(occurencies) - i - 1):
#                 if occurencies[j] > occurencies[j + 1]:
#                     temp = occurencies[j]
#                     occurencies[j] = occurencies[j + 1]
#                     occurencies[j + 1] = temp
                    
#                     temp = numbers[j]
#                     numbers[j] = numbers[j + 1]
#                     numbers[j + 1] = temp