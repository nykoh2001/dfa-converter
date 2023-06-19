def recognize_string(DFA, string):
    final_state = DFA.final_state
    start_state = DFA.start_state
    delta_function = DFA.delta_funcs
    current_state = start_state

    for c in string:
        moved = False
        for d in delta_function:
            if current_state in d.state and c == d.symbol:

                current_state = d.next
                moved = True
                break
        if not moved:
            return "인식할 수 없는 문자열입니다."
    if string == "":
        string = "epsilon"
    if current_state in final_state:
        return string + "은 인식되었습니다."
    else:
        return "인식할 수 없는 문자열입니다."
