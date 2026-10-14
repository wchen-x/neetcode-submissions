class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        #loop through the list nums
        #we do target - num
        # if the target - num is in seen then we outpuyt the indicies of num and target-num (we need dict to store indicees and value)\
        # if not seen then we add num into seen and move o9n

        for i, num in enumerate(nums):
            sub = target - num 
            if sub in seen:
                return [seen[sub], i]
            seen[num] = i

        return []