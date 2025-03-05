# climbing a staircase and it takes n steps to reach the top
# each time you climb 1 or 2 steps. In how many distinct ways can you reach the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        print(one)
        return one
    
# Dynamic programming space optimized approach
# O(n) time complexity
# O(1) space complexity 


""" solution = Solution()
result = solution.climbStairs(5)  # This will print the result for n = 5 """