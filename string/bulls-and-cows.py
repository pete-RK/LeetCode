class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(s == g for s, g in zip(secret, guess))
        cowSecret, cowGuess = Counter(secret), Counter(guess)
        cows = sum((cowSecret & cowGuess).values()) - bulls
        return f"{bulls}A{cows}B"
    

         