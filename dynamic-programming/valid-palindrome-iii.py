class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # Handle edge cases
        if not s or k < 0:
            return False
        if k >= len(s):
            return True
        
        n = len(s)
        # Initialize DP array: dp[i][j] = length of LPS in s[i:j+1]
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # Fill DP table
        for length in range(2, n + 1):  # Substring length
            for i in range(n - length + 1):  # Start index
                j = i + length - 1  # End index
                if s[i] == s[j]:
                    # If ends match, include both characters
                    dp[i][j] = 2 + dp[i + 1][j - 1] if i + 1 <= j - 1 else 2
                else:
                    # If ends don't match, take max of excluding either end
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        # LPS length for entire string
        palindrome_len = dp[0][n - 1]
        # Check if removals needed are <= k
        return n - palindrome_len <= k


            