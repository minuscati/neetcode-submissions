class Solution:
    def trap(self, height: List[int]) -> int:
#逐列计算
        Answer = 0
        k = len(height)
        prefix_max = [height[0]]*k
        suffix_max = [height[k-1]]*k
        for i in range(1,k):
            prefix_max[i]=max(prefix_max[i-1],height[i])
        for j in range(k-2,-1,-1):
            suffix_max[j]=max(suffix_max[j+1],height[j])
        for i in range(k):
            Answer+= min(prefix_max[i],suffix_max[i])-height[i]
        return Answer

            
        