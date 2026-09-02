class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        areaMax = -1

        while(i < j):
            areaAtual = (j - i) * min(heights[i], heights[j])
            if areaAtual > areaMax:
                areaMax = areaAtual
            
            if heights[i] <= heights[j]:
                i += 1
                continue
            else:
                j -= 1
                continue
        
        return areaMax

        