from sys import stdin
import re

from node import Node

string = stdin.readline()

ops = "()+*•"

p = re.compile("[a-zA-Z0-9]")

# 축약형 전처리 : • 추가
i = 0
length = len(string)
while True:
    if string[i] in ops:
        if string[i] == "*" and string[i + 1] not in ["+", "•", "\n"]:
            string = string[: i + 1] + "•" + string[i + 1 :]
            length += 1
    elif p.match(string[i]) and string[i + 1] == "(":
        string = string[: i + 1] + "•" + string[i + 1 :]
        length += 1
    elif p.match(string[i]) and p.match(string[i + 1]):
        string = string[: i + 1] + "•" + string[i + 1 :]
        length += 1
    i += 1
    if i >= length:
        break
print(string)
start_node = Node(string)
start_node.build_tree()
print("tree building complete")
queue = [start_node]
print(start_node.exp)
while queue:
    current = queue[0]
    del queue[0]
    print("     ", end="")
    if current.node_0:
        print("node:", current.node_0.exp, end="   ")
        queue.append(current.node_0)
    print("      ", end="")
    if current.operator:
        print("op:", current.operator, end="   ")
    print("      ", end="")
    if current.node_1:
        print("node:", current.node_1.exp, end="   ")
        queue.append(current.node_1)
