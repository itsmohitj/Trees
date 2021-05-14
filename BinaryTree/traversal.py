def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data, end = " ")
        printInorder(root.right)

def printPreorder(root):
    if root:
        print(root.data, end = " ")
        printPreorder(root.left)
        printPreorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data, end=" ")

def printLevelorder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while(len(queue) > 0):
        print(queue[0].data, end=" ")
        temp = queue.pop(0)
        if temp.left is not None:
            queue.append(temp.left)
        if temp.right is not None:
            queue.append(temp.right)
