class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total=[]
        running_sum=0
        for i in range(len(nums)):
            running_sum+=nums[i]
            total.append(running_sum)
        return total
        