class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sumnaturalnumbers=n*(n+1)//2
        sum_nums=sum(nums)
        return sumnaturalnumbers-sum_nums

        