class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # { 1: 1, 2: 2, 3: 3}
        # [[], [1], [2], [3], [], [], []]
        # [3, 2, 1] = ans 

        counter = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for key, value in counter.items():
            bucket[value].append(key)

        ans = []

        for i in range(len(nums), -1, -1):
            for j in range(len(bucket[i])):
                print(f"{i} {j}")
                
                ans.append(bucket[i][j])
        
        return ans[:k]

        

