from collections import defaultdict
def brainfuck_interpreter(code, input_):
    cells = defaultdict(int)
    cell = 0
    pos = 0
    output = ""
    
    stack = []
    jump_to = {}
    for i, c in enumerate(code):
        if c == '[':
            stack.append(i)
        if c == ']':
            jump_to[i] = stack[-1]
            jump_to[stack.pop()] = i
    
    while pos < len(code):
        curr = code[pos]
        if curr == '>':
            cell += 1
        elif curr == '<':
            cell -= 1
        elif curr == '+':
            cells[cell] += 1
        elif curr == '-':
            cells[cell] -= 1
        elif curr == '.':
            output += chr(cells[cell])
        elif curr == ',':
            in_char = input_[0]
            input_ = input[1:]
            cells[cell] = ord(in_char)
        elif curr == '[' and cells[cell] == 0:
            pos = jump_to[pos]
        elif curr == ']' and cells[cell] != 0:
            pos = jump_to[pos]
        pos += 1
    
    return output

print(brainfuck_interpreter("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.", ""))