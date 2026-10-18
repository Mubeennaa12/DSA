class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            total=0
            while n>0:
                total+=n%10
                n=n//10
            return total
        arr=sorted((digit_sum(x), x, i) for i, x in enumerate(nums))
        pos=[item[2] for item in arr]
        visited=[False]*len(nums)
        swaps=0
        for i in range(len(nums)):
            if visited[i] or pos[i]==i:
                continue
            cycle=0
            j=i
            while not visited[j]:
                visited[j]=True
                j=pos[j]
                cycle+=1
            swaps+=cycle-1
        return swaps
        