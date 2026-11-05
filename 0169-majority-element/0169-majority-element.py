class Solution:
  def majorityElement(self, nums: list[int]) -> int:
    ans = None
    count = 0
    for i in nums:
        if count == 0:
            ans = i
        if i==ans:
            count=count+1
        else :
            count=count-1
    return ans