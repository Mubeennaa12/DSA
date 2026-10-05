class Solution:
  def majorityElement(self, nums: list[int]) -> int:
    count={}
    for i in nums:
        if i not in count:
            count[i]=1
        else:
            count[i]=count[i]+1
    for i in count:
        if count[i]>len(nums)//2:
            return i
