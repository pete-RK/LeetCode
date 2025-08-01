class Solution:
    def isPreorder(self, nodes: List[List[int]]) -> bool:
        root,_ = nodes.pop(0)                                   
        stack = deque([root])                                   

        for child, parent in nodes:                             
                                                                
            while stack and parent != stack[-1]: stack.pop()    

            if not stack: return False                         
            
            stack.append(child)

        return True     