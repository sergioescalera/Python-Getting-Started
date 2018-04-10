class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums) - (i + 1)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        i = 0
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1

sol = Solution()

print (sol.twoSum([3,2,4], 6))





        