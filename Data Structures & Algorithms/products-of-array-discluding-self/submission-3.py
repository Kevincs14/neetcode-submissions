class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [0]*len(nums)

        summ = 1
        for i in range(len(nums)):
            products[i] = nums[i] * summ
            summ *= nums[i]

        
        # products =  1  2   8  48

        answer = [0]*len(nums)
        total = 1
        for j in range(len(nums)-1,0,-1):
            answer[j] = total*products[j-1]
            total *= nums[j]
        
        answer[0] = total
        
        return answer



            