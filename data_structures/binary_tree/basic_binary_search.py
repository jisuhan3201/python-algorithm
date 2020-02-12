class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return "Data : {}".format(self.data)

def display(tree):

    if tree is None:
        return
    
    if tree.left is not None:
        display(tree.left)

    # print(tree.data)

    if tree.right is not None:
        display(tree.right)

def is_full_binary_tree(tree):
    if tree is None:
        return True
    if tree.left is None and tree.right is None:
        return True
    if tree.left is not None and tree.right is not None:
        return is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right)
    else:
        return False

def breadth_first_search(q):
    if not q:
        return
    cur_tree = q.pop(0)
    if cur_tree.left:
        q.append(cur_tree.left)
    if cur_tree.right:
        q.append(cur_tree.right)
    breadth_first_search(q)

def depth_first_search(tree):
    print(tree)
    if not tree.left and not tree.right:
        return
    if tree.left:
        depth_first_search(tree.left)
    if tree.right:
        depth_first_search(tree.right)

def main():

    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)

    # display(tree)
    print(is_full_binary_tree(tree))
    breadth_first_search([tree])
    depth_first_search(tree)

if __name__ == "__main__":
    main()