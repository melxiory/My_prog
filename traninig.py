def brainfuck_to_c(source_code):
    if source_code.count('[') != source_code.count(']'):
        return "Error!"
    indent_num = 0
    result_end = ''
    comm_plus_minus, comm_left_right = 0, 0
    while source_code:
        while True:
            if source_code and (source_code[comm_plus_minus] == '+' or source_code[comm_plus_minus] == '-') and len(
                    source_code) > comm_plus_minus + 1:
                comm_plus_minus += 1
            else:
                if source_code.count('+') > source_code.count('-'):
                    result_end += f'{" "*indent_num}*p += {source_code.count("+")};\n'
                    source_code = source_code[comm_plus_minus + 1:]
                elif source_code.count('+') == source_code.count('-'):
                    pass
                else:
                    result_end += f'{" "*indent_num}*p -= {source_code.count("-")};\n'
                    source_code = source_code[comm_plus_minus + 1:]
                comm_plus_minus = 0
                break
        while True:
            if source_code and (source_code[comm_left_right] == '>' or source_code[comm_left_right] == '<') and len(
                    source_code) > comm_left_right + 1:
                comm_left_right += 1
            else:
                if source_code.count('>') > source_code.count('<'):
                    result_end += f'{" "*indent_num}p += {source_code.count(">")};\n'
                    source_code = source_code[comm_left_right + 1:]
                elif source_code.count('>') == source_code.count('<'):
                    pass
                else:
                    result_end += f'{" "*indent_num}p -= {source_code.count("<")};\n'
                    source_code = source_code[comm_left_right + 1:]
                comm_left_right = 0
                break
        if source_code and source_code[0] == '.':
            result_end += f'{" "*indent_num}putchar(*p);\n'
            source_code = source_code[1:]
        if source_code and source_code[0] == ',':
            result_end += f'{" "*indent_num}*p = getchar();\n'
            source_code = source_code[1:]
        if source_code and source_code[0] == '[':
            if source_code[1] == ']':
                source_code = source_code[2:]
                continue
            result_end += f'{" "*indent_num}if (*p) do {"{"}\n'
            indent_num += 2
            source_code = source_code[1:]
        if source_code and source_code[0] == ']':
            indent_num -= 2
            result_end += f'{" "*indent_num}{"}"} while (*p);\n'
            source_code = source_code[1:]
    return result_end


print(brainfuck_to_c("++++"))
print(brainfuck_to_c("----"))
print(brainfuck_to_c(">>>>"))
print(brainfuck_to_c("<<<<"))
print(brainfuck_to_c("."))
print(brainfuck_to_c(","))
print(brainfuck_to_c("[[[]]"))
print(brainfuck_to_c("[][]"))
print(brainfuck_to_c("[.]"))
