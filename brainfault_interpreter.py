from brainfault import Brainfault
from structures.arraystack import ArrayStack as Stack
from structures.linkedqueue import LinkedQueue as Queue
from collections import defaultdict
import re

def brainfault_interpreter(code, input_=[]):
    bf = Brainfault(code)
    input_ = Queue(input_)
    call_stack = Stack()
    cells = defaultdict(int)
    pointer = 0
    i = 0
    output = ""
    
    curr_call = bf
    
    while i < len(curr_call.code):
        cmd = curr_call.code[i]
        if cmd == '+':
            cells[pointer] += 1
        elif cmd == '-':
            cells[pointer] -= 1
        elif cmd == '>':
            pointer += 1
        elif cmd == '<':
            pointer -= 1
        elif cmd == '.':
            output += chr(cells[pointer])
        elif cmd == ':':
            output += f"{cells[pointer]}"
        elif cmd == '?':
            output += f"{10:08b}"
        elif cmd == ',':
            if input_.isEmpty():
                raise RuntimeError("Input taken from empty Queue")
            input_byte = input_.pop()
            if type(input_byte) is str:
                input_byte = ord(input_byte)
            cells[pointer] = input_byte
        elif cmd == '[' and cells[pointer] == 0:
            i = curr_call.jump_to[i]
        elif cmd == ']' and cells[pointer] != 0:
            i = curr_call.jump_to[i]
        elif cmd == '/' and input_.size == 0:
            i = curr_call.jump_to[i]
        elif cmd == '|' and input_.size != 0:
            i = curr_call.jump_to[i]
        elif cmd == '!':
            not_ = False
            num, i = curr_call.substr(i + 1, '(')
            if num[0] == '~':
                not_ = True
                num = num[1:]
            num = int(num)
            if eval("not " * (not_ ^ 1) + "cells[pointer] == num"):
                i = curr_call.jump_to[i]
        elif cmd == '*':
            subroute, i = curr_call.substr(i + 1, '*')
            i += 1
            call_stack.push((curr_call, i))
            curr_call = bf.subroutines[subroute]
            i = -1
        cells[pointer] %= 256
        i += 1
        
        while i == len(curr_call.code) and not call_stack.isEmpty():
            curr_call, i = call_stack.pop()
    return output