class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def display(tree):

    if tree is None:
        return
    
    print(tree.data)

    if tree.left is not None:
        display(tree.left)

    if tree.right is not None:
        display(tree.right)


def main():

    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)

    display(tree)

def dfs(tree, start):
    visited = []
    stack = []

    stack.append(start)

    while stack:
        node = stack.pop()
        print(node.data)
        
        visited.append(stack.data)

        if tree.left is not None:
            stack.append(tree.left)

        


if __name__ == "__main__":
    main()