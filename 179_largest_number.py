import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:    
        nums = [str(num) for num in nums]
        sorted_nums = sorted(nums, key=functools.cmp_to_key(self.comparator), reverse=True)
        if sorted_nums[0] == '0': return '0'
        return "".join(sorted_nums)
    
    
    def comparator(self, a: str, b: str)->int:
        if int(a + b) > int(b + a):
            return 1
        elif int(a + b) < int(b + a):
            return -1
        else:
            return 0
        
