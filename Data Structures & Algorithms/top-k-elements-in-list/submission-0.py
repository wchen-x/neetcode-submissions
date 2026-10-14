class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #counter dictionary
        #list of lists (of n values) to store the number at the index of occurences
        #we loop through from the tail 
        #take and add to answer
        #output answer

        counter = Counter(nums)

        bucket = [[] for _ in range(len(nums)+1)]

        for key, val in counter.items():
            bucket[val].append(key)

        ans = []
        i = len(nums)

        while len(ans) < k:
            if len(bucket[i]) == 0:
                i -= 1
            else:
                ans.append(bucket[i].pop())

        return ans