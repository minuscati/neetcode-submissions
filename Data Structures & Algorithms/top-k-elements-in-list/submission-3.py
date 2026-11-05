class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Answer= []
        count= {}
        for i in nums:
            if i in count:
                count[i] +=1
            else:
                count[i]=1
        # 构造新字典，按值排序
        sorted_count_by_value = dict(sorted(count.items(), key=lambda item:item[1],reverse = True))
        sorted_keys = [i for i in sorted_count_by_value.keys()]
        return sorted_keys[:k]