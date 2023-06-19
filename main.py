from sys import stdin
from re_to_tree import build_tree
from convert_nfa import convert, NFA, postfix, access_states
from convert_dfa import DFA

re = stdin.readline().rstrip()
processed_re = postfix(re)
tree = build_tree(processed_re)

NFA_nodes = convert(tree)
NFA = NFA()


trainsition_table = access_states(NFA_nodes[0], [], {NFA_nodes[0]: 0}, NFA)
print("epsilon NFA")
NFA.print_NFA()

print()


DFA = DFA(NFA)
print("converted DFA")
DFA.convertDFA(DFA.start_state, [])
DFA.print_DFA()
