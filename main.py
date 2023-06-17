from sys import stdin
import re

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
    elif p.match(string[i]) and p.match(string[i + 1]):
        string = string[: i + 1] + "•" + string[i + 1 :]
        length += 1
    i += 1
    if i >= length:
        break


print(string)
