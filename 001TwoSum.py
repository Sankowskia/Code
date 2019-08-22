class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, num in enumerate(nums):
            another_one = target - num
            if another_one in hash_map:
                return [hash_map[another_one], index]
            hash_map[num] = index
        return None