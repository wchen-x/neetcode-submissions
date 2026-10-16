class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for key, value in counter.items():
            bucket[value].append(key)
        
        ans = []

        for i in range(len(nums), -1, -1):
            for j in range(len(bucket[i])):
                ans.append(bucket[i][j])

                if len(ans) == k:
                    return ans