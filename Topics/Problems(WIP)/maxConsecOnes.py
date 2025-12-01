# https://leetcode.com/problems/max-consecutive-ones?envType=problem-list-v2&envId=dsa-linear-shoal-array-i

def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0 # Tracking variable to count consecutive 1's
        max_count = 0 # Max Count

        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        
        return max(max_count, count) # Count may be higher when done with loop
