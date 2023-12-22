class Solution:
    def maxScore(self, s: str) -> int:
        left = -1
        zeros = 0
        ones = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1
            left = max(left, zeros - ones)
        ones += 1 if s[-1] == '1' else 0
        return left + ones

# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/?envType=daily-question&envId=2023-12-22