class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids: return []
        stack = [asteroids[0]]

        for ast in asteroids[1:]:
            while stack and ast < 0 < stack[-1]:
                if -ast > stack[-1]:
                    stack.pop()
                    continue
                elif -ast == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(ast) 
        
        return stack
                    
            

