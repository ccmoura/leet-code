class Solution:
    def twoSum(self, nums, target):
        diffs = {}

        for index in range(len(nums)):
            complement = target - nums[index]
            if diffs.get(complement) != None:
                return [diffs[complement], index]
            diffs[nums[index]] = index

