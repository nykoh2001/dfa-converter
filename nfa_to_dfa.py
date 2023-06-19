from copy import copy


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
        self.nfa_final_state = NFA.final_state
        self.final_state = []
        self.delta_funcs = []
        self.naming = {}
        self.naming_index = 0

    def add_name(self, state):
        self.naming["q" + str(self.naming_index).zfill(3)] = state
        self.naming_index += 1

    def print_DFA(self):
        self.start_state = get_key_by_value(self.naming, self.start_state)
        print(
            "StateSet = {",
            self.state_set,
            "}",
        )
        print("DeltaFunctions = {")
        for d in self.delta_funcs:
            print("   ", end="")
            d.print_delta(d.state, d.next)
        print("}")
        print("StartState =", self.start_state)
        print("FinalStateSet = {", ", ".join(self.final_state), "}")


def get_key_by_value(dict, value):

    for key, val in dict.items():
        if (val) == (value):

            return key


def get_closure(DFA, state, visited):
    equi = set()
    visited.append(state)
    for f in DFA.nfa_funcs:
        if f.state == state and f.symbol == "ε":
            equi = set([state])
            for n in f.next:
                if n not in visited:  # 이미 다른 state인 곳 고려 x
                    equi.add(n)
                    equi.update(get_closure(DFA, n, visited))
    if "q000" in equi:  # start state 정의
        DFA.start_state = equi
    return equi


def convertDFA(DFA, closure, visited):
    temp_closure = copy(closure)
    for state in temp_closure:
        closure.update(get_closure(DFA, state, visited))

    temp_sym = set()
    for f in DFA.nfa_funcs:
        if f.state in closure and f.symbol != "ε":
            temp_sym.add(f.symbol)

    temp_next = set()
    for s in temp_sym:
        temp_next = set()
        for f in DFA.nfa_funcs:
            if f.state in closure and f.symbol == s:
                for n in f.next:
                    temp_next.add(n)

        next_closure = copy(temp_next)
        for state in temp_next:
            next_closure.update(get_closure(DFA, state, visited))

        if next_closure == closure:  # recursive move
            closure_num = get_key_by_value(DFA.naming, closure)
            next_closure_num = get_key_by_value(DFA.naming, next_closure)
            if closure_num == None:
                DFA.add_name(closure)
                closure_num = get_key_by_value(DFA.naming, closure)
                print("new state:", closure_num, "=", closure)
                if DFA.nfa_final_state in closure:
                    DFA.final_state.append(closure_num)
            if next_closure_num == None:
                DFA.add_name(next_closure)
                next_closure_num = get_key_by_value(DFA.naming, next_closure)
                print("new state:", next_closure_num, "=", next_closure)
                if DFA.nfa_final_state in next_closure:
                    DFA.final_state.append(next_closure_num)
            DFA.delta_funcs.append(DeltaFunc(closure_num, s, next_closure_num))
            DFA.state_set.add(closure_num)
            DFA.state_set.add(next_closure_num)
            return
        # 가능한 다음 상태 집합을 하나의 집합으로 매칭
        closure_num = get_key_by_value(DFA.naming, closure)
        next_closure_num = get_key_by_value(DFA.naming, next_closure)
        if closure_num == None:
            DFA.add_name(closure)
            closure_num = get_key_by_value(DFA.naming, closure)
            print("new state:", closure_num, "=", closure)
            if DFA.nfa_final_state in closure:
                DFA.final_state.append(closure_num)
        if next_closure_num == None:
            DFA.add_name(next_closure)
            next_closure_num = get_key_by_value(DFA.naming, next_closure)
            print("new state:", next_closure_num, "=", next_closure)
            if DFA.nfa_final_state in next_closure:
                DFA.final_state.append(next_closure_num)
        DFA.delta_funcs.append(DeltaFunc(closure_num, s, next_closure_num))
        DFA.state_set.add(closure_num)

        # 다음 상태에 대한 DFA 변환 호출
        convertDFA(DFA, next_closure, visited)
