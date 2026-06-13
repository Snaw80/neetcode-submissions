import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            s1 = heapq.heappop(heap)
            s2 = heapq.heappop(heap)
            print(s1,s2)
            r = s1 - s2
            if r:
                heapq.heappush(heap,r)

        if len(heap):
            return -heap[0]
        else:
            return 0