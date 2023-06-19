import re

p = re.compile("[a-zA-Z0-9]")


def isTerm(c):
    return p.match(c)


class Node:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
        self.node_0 = None
        self.node_1 = None


def build_tree(exp):
    stack = []
    for c in exp:
        if isTerm(c):
            stack.append(Node(1, c))
            continue
        elif c == "+":
            z = Node(3)
            z.node_1 = stack.pop()
            z.node_0 = stack.pop()
        elif c == "•":
            z = Node(2)
            z.node_1 = stack.pop()
            z.node_0 = stack.pop()
        elif c == "*":
            z = Node(4)
            z.node_0 = stack.pop()
        stack.append(z)
    return stack[0]
