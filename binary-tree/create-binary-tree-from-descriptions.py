# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = defaultdict()
        childs, parents = set(), set()

        for par, chi, isl in descriptions:
            childs.add(chi)
            parents.add(par)
            if par in nodes:
                if chi not in nodes:
                    new_node = TreeNode(chi)
                    nodes[chi] = new_node
                if isl == 1:
                    nodes[par].left = nodes[chi]
                else:
                    nodes[par].right = nodes[chi]
            else:
                new_parent = TreeNode(par)
                nodes[par] = new_parent
                if chi not in nodes:
                    new_node = TreeNode(chi)
                    nodes[chi] = new_node
                if isl == 1:
                    nodes[par].left = nodes[chi]
                else:
                    nodes[par].right = nodes[chi]

        parent = parents - childs
        return nodes[parent.pop()]