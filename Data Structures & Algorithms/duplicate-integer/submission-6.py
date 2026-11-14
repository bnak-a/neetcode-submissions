class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = [None] * len(nums)
        for i in range(len(nums)):
            hash_index = nums[i] % len(nums)
            if (hash_map[hash_index] == nums[i]):
                return True
            while (hash_map[hash_index] != nums[i] and hash_map[hash_index] != None and hash_index != (len(hash_map) - 1)):
                if (hash_map[hash_index] == nums[i]): 
                    return True
                
                hash_index += 1
            if (hash_index == len(hash_map)):
                hash_index = 0
                while (hash_map[hash_index] != nums[i] and       hash_map[hash_index] != None):
                    if (hash_map[hash_index] == nums[i]): 
                        return True
                
                    hash_index += 1
                
            hash_map[hash_index] = nums[i]
        
        return False    