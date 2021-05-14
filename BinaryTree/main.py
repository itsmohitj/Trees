import traversal 
class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

    def insertLevelOrder(arr, root, i, n):
        if i < n:
            temp = Node(arr[i])
            root = temp
            root.left = Node.insertLevelOrder(arr, root.left, 2 * i + 1, n)
            root.right = Node.insertLevelOrder(arr, root.right, 2 * i + 2, n)
        return root

if __name__ == '__main__':
    lst = list(map(int,input().split()))
    root = Node.insertLevelOrder(lst, None, 0, len(lst))
    traversal.printInorder(root)
