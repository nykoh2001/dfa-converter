from sys import stdin, exit
from re_to_tree import build_tree, postfix
from re_to_nfa import convert, NFA, access_states
from nfa_to_dfa import DFA, convertDFA
from recognize import recognize_string

import re

p = re.compile("[A-Za-z0-9*+•()]")

print("정규표현:")
re = stdin.readline().rstrip()

if not p.match(re):
    print("문자나 숫자, 정해진 연산자들로만 이루어진 정규 표현을 입력해주세요.")
    exit(0)
print()

processed_re = postfix(re)
tree = build_tree(processed_re)

NFA_nodes = convert(tree)
NFA = NFA()

trainsition_table = {NFA_nodes[0]: 0}
access_states(NFA_nodes[0], [], trainsition_table, NFA)

NFA.final_state = "q" + str(trainsition_table[NFA_nodes[1]]).zfill(3)
print("epsilon NFA")
NFA.print_NFA()

print()


DFA = DFA(NFA)
print("converted DFA")
convertDFA(DFA, DFA.start_state, [])
print()
DFA.print_DFA()


print()
print("정규표현:", re)
print("인식할 문자열:")

input_string = stdin.readline().rstrip()
while True:
    if input_string == "exit":
        exit(0)
    print(recognize_string(DFA, input_string), "\n")
    print("인식할 문자열:")
    input_string = stdin.readline().rstrip()
