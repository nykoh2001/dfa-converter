from sys import stdin
from re_to_tree import build_tree
from convert_nfa import convert, NFA, postfix, access_states
from convert_dfa import DFA

re = stdin.readline().rstrip()
processed_re = postfix(re)
tree = build_tree(processed_re)

NFA_nodes = convert(tree)
NFA = NFA()

print("nfa start node", NFA_nodes[0].next_state)
trainsition_table = access_states(NFA_nodes[0], [], {NFA_nodes[0]: 0}, NFA)
NFA.print_NFA()

print()

DFA = DFA(NFA)
DFA.convertDFA(DFA.start_state, [])
