class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack, min_check = [], -math.inf

        for num in preorder:
            while stack and stack[-1] < num:
                min_check = stack.pop()
            if num < min_check:
                return False
            
            stack.append(num)
        
        return True
            




        




        