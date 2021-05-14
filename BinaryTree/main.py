import traversal 
import createTree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None


if __name__ == '__main__':
    lst = list(map(lambda x : x if type(x) is int else x, input().split()))
    root = createTree.createLevelOrder(lst, None, 0, len(lst))
    traversal.printInorder(root)
