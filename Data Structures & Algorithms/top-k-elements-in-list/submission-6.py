class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
       
        counts = defaultdict(int)
    
        for i in range(len(nums)):
            counts[nums[i]] += 1
        
        arr = []
        for num, count in counts.items():
            arr.append([count, num])
        
        arr.sort()
        
        answ = []
        kcount = k
        for i in range(len(arr)-1,-1,-1):
            if kcount <= 0:
                return answ
            answ.append(arr[i][1])
            kcount -= 1

            
                
                
        return answ



        
        
        
        