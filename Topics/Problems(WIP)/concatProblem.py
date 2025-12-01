# https://leetcode.com/problems/concatenation-of-array?envType=problem-list-v2&envId=dsa-linear-shoal-array-i

def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n

        for i in range(n):
            ans[i] = nums[i]
        
        ans *= 2

        return ans