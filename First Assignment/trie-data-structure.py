class Node:
    __allNodes = []
    __id = -1

    id = 0

    def __init__(self, symbol, parent):
        self.id = Node.__id + 1
        Node.__id = self.id
        self.symbol = symbol
        self.parent = parent
        self.children = set()
        Node.__allNodes.append(self)

    def add_child(self, son):
        self.children.add(son)

    def getChildBySymbol(self, symbol):
        for kid in self.children:
            if kid.symbol == symbol:
                return kid
        return None


root = Node("root", None)

while True:
    seq = input()
    seq = seq.strip()
    if seq == "end":
        break
    current_node = root
    for i in range(len(seq)):
        new_node = current_node.getChildBySymbol(seq[i])
        if new_node is not None:

            current_node = new_node
            continue
        else:
            child = Node(seq[i], current_node)
            print(str(current_node.id) + "->" + str(child.id) + ":" + child.symbol)
            current_node.add_child(child)
            current_node = child
