class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s,e = 0, len(heights) - 1
        mw = 0

        while s < e:
            min_border = min(heights[s],heights[e])
            water = (e-s) * min_border
            if water > mw:
                mw = water
            
            if min_border == heights[s]:
                s += 1
            else:
                e -= 1
        return mw