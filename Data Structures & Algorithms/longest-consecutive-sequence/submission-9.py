class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        lookup = set(nums)
         
        best = 1  
        for num in nums: 
            if num - 1 not in lookup:
                count = 1
                curr = num
                while True:
                    curr = curr + 1
                    if curr in lookup:
                        count += 1
                    else:
                        break
                best = max(count, best)
       
        return best
                        



             