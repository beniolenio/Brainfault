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
        loop_stack = Stack()
        match = {']': '[', ')': '(', '|': '/'}
        for i, c in enumerate(self.code):
            if c in ("(", "[", "/"):
                loop_stack.push((i, c))
            elif c in (")", "]", "|"):
                back_to, last_c = loop_stack.pop()
                if last_c != match[c]:
                    raise RuntimeError("Non-matching loop characters")
                self.jump_to[i] = back_to
                self.jump_to[back_to] = i
    
    def substr(self, i, last_char):
        return_val = ""
        while self.code[i] != last_char:
            return_val += self.code[i]
            i += 1
        return return_val, i
    
    def __repr__(self):
        return self.code

class Subroutine:
    def __init__(self, code):
        self.code = code
        self.jump_to = {}
        loop_stack = Stack()
        match = {']': '[', ')': '(', '|': '/'}
        for i, c in enumerate(self.code):
            if c in ("(", "[", "/"):
                loop_stack.push((i, c))
            elif c in (")", "]", "|"):
                back_to, last_c = loop_stack.pop()
                if last_c != match[c]:
                    raise RuntimeError("Non-matching loop characters")
                self.jump_to[i] = back_to
                self.jump_to[back_to] = i
    
    def substr(self, i, last_char):
        return_val = ""
        while self.code[i] != last_char:
            return_val += self.code[i]
            i += 1
        return return_val, i
    
    def __repr__(self):
        return self.code