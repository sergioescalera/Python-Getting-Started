class Solution(object):
    def twoSum(self, nums, target):
        return self.twoSumWhile(nums, target)

    def twoSumFor(self, nums, target):

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSumWhile(self, nums, target):

        i = 0

        while i < len(nums) - 1:

            j = i + 1

            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1

            i += 1

    def twoSumDict(self, nums, target):

        dict = {}

        for i in range(len(nums)):
            
            val = nums[i]
            
            diff = target - val
            
            found = dict.get(diff)

            if found is not None:
                return [found, i]
            
            dict[val] = i


sol = Solution()

result = sol.twoSumDict([3,2,4], 6)

print (result)





        