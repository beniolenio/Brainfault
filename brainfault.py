from structures.arraystack import ArrayStack as Stack
from structures.linkedqueue import LinkedQueue as Queue
import re

class Brainfault:
    def __init__(self, code):
        self.raw_code = code
        self.subroutines = {}
        
        clean_code = self.raw_code.replace("\n", "")
        clean_code = re.sub("#[^#]*?#", "", clean_code)
        
        subroutines = re.findall("\$([a-zA-Z_]*)\{(.*?)\}", clean_code)
        for name, sub_code in subroutines:
            self.subroutines[name] = Subroutine(sub_code)
        
        clean_code = re.sub("\$[a-zA-Z_]*\{.*?\}", "", clean_code)
        self.code = clean_code
        
        self.jump_to = {}
        if_while_stack = Stack()
        for i, c in enumerate(self.code):
            if c == '[' or c == '(':
                if_while_stack.push((i, c))
            elif c == ']' or c == ')':
                back_to, last_c = if_while_stack.pop()
                if c == ']' and last_c == '(' or c == ')' and last_c == '[':
                    raise RuntimeError("Non-matching brackets")
                self.jump_to[i] = back_to
                self.jump_to[back_to] = i
    
    def substr(self, i, last_char):
        return_val = ""
        while self.code[i] != last_char:
            return_val += self.code[i]
            i += 1
        return return_val, i

class Subroutine:
    def __init__(self, code):
        self.code = code
        self.jump_to = {}
        if_while_stack = Stack()
        for i, c in enumerate(self.code):
            if c == '[' or c == '(':
                if_while_stack.push((i, c))
            elif c == ']' or c == ')':
                back_to, last_c = if_while_stack.pop()
                if c == ']' and last_c == '(' or c == ')' and last_c == '[':
                    raise RuntimeError("Non-matching brackets")
                self.jump_to[i] = back_to
                self.jump_to[back_to] = i
    
    def substr(self, i, last_char):
        return_val = ""
        while self.code[i] != last_char:
            return_val += self.code[i]
            i += 1
        return return_val, i