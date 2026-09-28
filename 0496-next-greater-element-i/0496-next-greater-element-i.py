class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]
        greater={}
        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                greater[smaller]=num
            stack.append(num)
        while stack:
            greater[stack.pop()]=-1
        result=[]
        for num in nums1:
            result.append(greater[num])
        return result