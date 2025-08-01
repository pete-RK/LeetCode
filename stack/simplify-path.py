class Solution:
    def simplifyPath(self, path: str) -> str:
        chars = path.split('/')
        stack = []

        for ch in chars:
            if ch == '' or ch == '.': continue
            if stack and ch == '..':
                stack.pop()
                continue
            elif ch == '..': continue
            
            stack.append(ch)
        
        res = '/' + '/'.join(stack)
        return  res
            


            

            
