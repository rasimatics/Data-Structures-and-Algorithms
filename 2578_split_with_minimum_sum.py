import heapq

class Solution:
    def splitNum(self, num: int) -> int:
        list_of_int = [int(i) for i in str(num)]

        heapq.heapify(list_of_int)

        iterations = len(list_of_int)

        a = ""
        b = ""
        first = True

        for i in range(iterations):
            val = heapq.heappop(list_of_int)
            if first:
                a += str(val)
                first = False
            else:
                b += str(val)
                first = True

        return int(a) +  int(b)
