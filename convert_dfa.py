class DeltaFunc:
    def __init__(self, state, symbol, next_state):
        self.state = state
        self.symbol = symbol
        self.next = next_state

    def print_delta(self, state, _next):
        print(f"({state}, {self.symbol}) = {_next}")


class DFA:
    def __init__(
        self,
        NFA,
    ):
        self.nfa_funcs = NFA.delta_funcs
        self.start_state = set([NFA.start_state])
        self.state_set = set()
        self.delta_funcs = []
        self.naming = {}

    def print_DFA(self):
        print(
            "StateSet = {", ", ".join([self.naming[ss] for ss in self.state_set]), "}"
        )
        print("DeltaFunctions = {")
        for d in self.delta_funcs:
            print("   ", end="")
            d.print_delta(self.naming[str(d.state)], self.naming[str(d.next)])
        print("}")
        print("StartState = q000")

    def convertDFA(self, closure, visited):
        equi = set()
        if closure.issubset(set(visited)):
            temp_sym = set()
            for f in self.nfa_funcs:
                if f.state in closure and f.symbol != "ε":
                    temp_sym.add(f.symbol)

            for s in temp_sym:
                temp_next = set()
                for f in self.nfa_funcs:
                    if f.state in closure and f.symbol == s:
                        for n in f.next:
                            temp_next.add(n)

                str_closure = str(closure)
                equi = set()
                for state in temp_next:
                    visited.append(state)
                    for f in self.nfa_funcs:
                        if f.state == state and f.symbol == "ε":
                            for n in f.next:
                                equi.add(n)
                temp_next = temp_next | equi
                self.delta_funcs.append(DeltaFunc(str_closure, s, temp_next))
                self.state_set.add(str_closure)
                self.state_set.add(str(temp_next))

                self.convertDFA(temp_next, visited)

            return

        for state in closure:
            visited.append(state)
            for f in self.nfa_funcs:
                if f.state == state and f.symbol == "ε":
                    for n in f.next:
                        equi.add(n)
        closure = closure | equi
        closure = self.convertDFA(closure, visited)
        state_list = list(self.state_set)
        for i in range(len(state_list)):
            self.naming[state_list[i]] = "q" + str(i).zfill(3)

        self.print_DFA()
