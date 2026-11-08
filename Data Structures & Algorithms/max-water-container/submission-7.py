class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_prod = 0
        k = len(heights)
        i=0
        j = k-1
        while i<j:
            curr_prod = (j-i)*min(heights[i],heights[j])
            max_prod = max(max_prod, curr_prod)

            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return max_prod