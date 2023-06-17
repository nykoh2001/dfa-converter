import re

p = re.compile("[a-zA-Z0-9]")


class Type:
    SYMBOL = 1
    CONCAT = 2
    UNION = 3
    STAR = 4


def isTerm(c):
    return p.match(c)


class Node:
    def __init__(self, _type, value=None):
        self._type = _type
        self.value = value
        self.node_0 = None
        self.node_1 = None


def build_tree(regexp):
    stack = []
    for c in regexp:
        if isTerm(c):
            stack.append(Node(Type.SYMBOL, c))
            continue
        elif c == "+":
            z = Node(Type.UNION)
            z.node_1 = stack.pop()
            z.node_0 = stack.pop()
        elif c == "•":
            z = Node(Type.CONCAT)
            z.node_1 = stack.pop()
            z.node_0 = stack.pop()
        elif c == "*":
            z = Node(Type.STAR)
            z.node_0 = stack.pop()
        stack.append(z)
    return stack[0]
