class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7

        dp = [0] * (n + 1)
        dp[1] = 1  

        share = 0  

        for day in range(2, n + 1):
            share += dp[day - delay] if day - delay >= 1 else 0
            share %= MOD

            share -= dp[day - forget] if day - forget >= 1 else 0
            share %= MOD

            dp[day] = share

        ans = 0
        for day in range(n - forget + 1, n + 1):
            ans += dp[day]
            ans %= MOD

        return ans
