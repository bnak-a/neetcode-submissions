class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        count = 0
        ans = [0] * (2 * len(nums))
        while count != 2:
            for i in range(len(nums)):
                ans[i + (len(nums) * count)] = nums[i]
            count += 1
        
        return ans