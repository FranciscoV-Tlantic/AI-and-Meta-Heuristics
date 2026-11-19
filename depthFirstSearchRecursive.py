class Node:
    def __init__(self, name):
        self.name = name
        self.adjancency_list = []
        self.visited = False

def depth_first_search(node):
    node.visited = True
    print(node.name)

    for n in node.adjancency_list:
        if not n.visited:
            depth_first_search(n)


if __name__ == "__main__":
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    node1.adjancency_list.append(node2)
    node2.adjancency_list.append(node3)
    node2.adjancency_list.append(node4)
    node3.adjancency_list.append(node4)
    node4.adjancency_list.append(node5)

    depth_first_search(node1)