def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data, end = " ")
        printInorder(root.right)

def printPreoder(root):
    if root:
        print(root.data, end = " ")
        printPreoder(root.left)
        printPreoder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data, end=" ")

