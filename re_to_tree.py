import re

p = re.compile("[a-zA-Z0-9]")


def isTerm(c):
    return p.match(c)


def higherPrecedence(a, b):
    p = ["+", "•", "*"]
    return p.index(a) > p.index(b)


def postfix(re):
    temp = []
    for i in range(len(re)):
        if (
            i != 0
            and (isTerm(re[i - 1]) or re[i - 1] == ")" or re[i - 1] == "*")
            and (isTerm(re[i]) or re[i] == "(")
        ):
            temp.append("•")
        temp.append(re[i])
    re = temp

    stack = []
    output = ""

    for c in re:
        if isTerm(c):
            output = output + c
            continue

        if c == ")":
            while len(stack) != 0 and stack[-1] != "(":
                output = output + stack.pop()
            stack.pop()
        elif c == "(":
            stack.append(c)
        elif c == "*":
            output = output + c
        elif len(stack) == 0 or stack[-1] == "(" or higherPrecedence(c, stack[-1]):
            stack.append(c)
        else:
            while (
                len(stack) != 0
                and stack[-1] != "("
                and not higherPrecedence(c, stack[-1])
            ):
                output = output + stack.pop()
            stack.append(c)

    while len(stack) != 0:
        output = output + stack.pop()

    return output


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
