OPERATORS = {'+': 'add', '-': 'sub', '*': 'mul', '/': 'div'}
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def arithmetic_arranger(arr: list, showAnswer=False):
    if len(arr) > 5:
        return 'Error: Too many problems.'
    first_line = ''
    second_line = ''
    thrid_line = ''
    result_line = ''
    for p in arr:
        (n1, op, n2) = p.split()
        if(op != "+" and op != "-"):
            return "Error: Operator must be '+' or '-'."
        if(len(n1) > 4 or len(n2) > 4):
            return 'Error: Numbers cannot be more than four digits.'
        diff = 0
        firstLen = len(n1)
        secondLen = len(n2)
        lines_lenght = firstLen + 2
        second_line += op + " "
        if secondLen > firstLen:
            diff = secondLen - firstLen
            lines_lenght += diff
            for x in range(diff):
                first_line += " "
        elif firstLen > secondLen:
            diff = firstLen - secondLen
            for x in range(diff):
                second_line += " "

        first_line += "  " + n1 + "    "

        second_line += n2 + "    "
        method = '__%s__' % OPERATORS[op]
        try:
            answer = getattr(int(n1), method)(int(n2))
        except:
            return 'Error: Numbers must only contain digits.'
        # thrid_line += spacing + " " * min_len + line_separator
        thrid_line += "-" * lines_lenght + "    "
        if showAnswer:
            result_length = lines_lenght - len(str(answer))
            result_line += " " * result_length
            result_line += str(answer) + "    "
    solution = first_line.rstrip() + "\n" + second_line.rstrip() + \
        "\n" + thrid_line.rstrip()
    if showAnswer:
        solution += "\n" + result_line.rstrip()
    return solution


# print(arithmetic_arranger(
#     ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))


# print(arithmetic_arranger(
#     ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

actual = arithmetic_arranger(
    ["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)
expected = "   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172"

print(actual == expected)
print("*" * 20)

# print(actual)
# print("*" * 20)
# print(expected)
# print("*" * 20)

index = 3

print(len(actual.split("\n")[index]))
print(len(expected.split("\n")[index]))
print("*" * 20)
print(actual.split("\n")[index])
print(expected.split("\n")[index])

# EXPECTED
#    32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----

# Expected with answer
#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474
