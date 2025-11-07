class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] * (1 + len(s)) # dp[i] = num ways to decode s[i:]

        for i in reversed(range(len(s))):
            single_digit_ways = 0 if s[i] == '0' else dp[i + 1]
            double_digit_ways = dp[i + 2] if i + 1 < len(s) and s[i] in '12' and int(s[i:i + 2]) <= 26 else 0
            dp[i] = single_digit_ways + double_digit_ways

        return dp[0]