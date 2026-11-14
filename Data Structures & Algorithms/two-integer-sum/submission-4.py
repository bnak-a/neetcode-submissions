class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for i in range(len(nums)):
            if(Map.get(target - nums[i]) != None):
                return [Map.get(target - nums[i]), i]
            else:
                Map[nums[i]] = i
        


