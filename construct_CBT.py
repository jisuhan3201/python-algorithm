from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return "data : {}, left : {}, right : {}".format(self.data, self.left, self.right)

def main():

    data = [3,5,2,1,4,6,7,8,9,10,11,12,13,14]
    n = iter(data)

    tree = Node(next(n))
    fringe = deque([tree])
    print([Node(1)])
    print(fringe)

if __name__ == "__main__":
    main()