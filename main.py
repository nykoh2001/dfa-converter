from sys import stdin
from re_to_tree import build_tree
from re_to_nfa import convert, NFA, postfix, access_states
from nfa_to_dfa import DFA, convertDFA

re = stdin.readline().rstrip()
print()
processed_re = postfix(re)
tree = build_tree(processed_re)

NFA_nodes = convert(tree)
NFA = NFA()


trainsition_table = access_states(NFA_nodes[0], [], {NFA_nodes[0]: 0}, NFA)
print("transition table", trainsition_table)
print("epsilon NFA")
NFA.print_NFA()

print()


DFA = DFA(NFA)
print("converted DFA")
convertDFA(DFA, DFA.start_state, [])
print()
DFA.print_DFA()
