class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        str_dict = {}

        for i in arr:
            str_dict[i] = str_dict.get(i, 0) + 1
        
        distinct_list = []

        for i in arr:
            if str_dict[i] == 1:
                distinct_list.append(i)


        return "" if k > len(distinct_list) else distinct_list[k - 1]
    
