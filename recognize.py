def recognize_string(DFA, string):
    print(string)

    final_state = DFA.final_state
    start_state = DFA.start_state
    delta_function = DFA.delta_funcs
    current_state = start_state
    # naming = DFA.naming
    for c in string:
        for d in delta_function:
            print(d.state)
            if current_state in d.state and c == d.symbol:
                current_state = d.next
                break

    if current_state in final_state:
        return string + " 문자열은 인식되었습니다."
    else:
        return "인식할 수 없는 문자열입니다."
