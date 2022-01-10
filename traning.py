import sys

n = str(sys.stdin.readline().strip())
stack = []
ind_val = []

def balanced(s):
    for ch in enumerate(s):
        if ch[1] not in ['(', '{', '[',']','}',')']:
            continue
        if ch[1] in ['(', '{', '[']:
            stack.append(ch)
        else:
            if not stack:
                return ch[0]+1
            top = stack.pop()[1]
            if top == '(' and ch[1] != ')' or \
                    top == '[' and ch[1] != ']' or \
                    top == '{' and ch[1] != '}':
                return ch[0]+1
    else:
        if stack:
            return stack[0][0]+1
    return 'Success'

print(balanced(n))
