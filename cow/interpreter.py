

from operator import le
from xmlrpc.client import Boolean, boolean


class Interpreter:


    def __init__(self, code: list):
        self.memory = [0] * 30000
        self.cell_ptr = 0
        self.cmd_ptr = 0 #prog_pos
        self.code = code
        self.cmds = {0:'moo', 1:'mOo', 2:'moO', 3:'mOO', 4:'Moo', 5:'MOo', 6:'MoO', 7:'MOO', 8:'OOO', 9:'MMM', 10:'OOM', 11:'oom'}
        self.has_register_val = False
        self.register_val: int

    def exec(self, command: str) -> Boolean:
        match(command):
            case 'moo':
                if self.cmd_ptr == 0:
                    return True
                self.cmd_ptr -= 1
                level = 1
                while level > 0:
                    if self.cmd_ptr == 0:
                        break
                    self.cmd_ptr -= 1
                    if self.code[self.cmd_ptr] == self.cmds[0]:
                        level += 1
                    elif self.code[self.cmd_ptr] == self.cmds[7]:
                        level -= 1
                if level != 0:
                    return True
                return self.exec(self.code[self.cmd_ptr])
            
            case 'mOo':
                if self.cell_ptr == 0:
                    return False
                else:
                    self.cell_ptr -= 1
            
            case 'moO':
                self.cell_ptr += 1

            case 'mOO':
                if self.code[self.cmd_ptr] == self.cmds[3]:
                    return False
                else:
                    self.exec(self.code[self.cmd_ptr])

            case 'Moo':
                if self.memory[self.cell_ptr] == 0:
                    self.memory[self.cell_ptr] = ord(input('ASCII:'))
                else:
                    print(chr(self.memory[self.cell_ptr]))
            
            case 'MOo':
                self.memory[self.cell_ptr] -= 1
            
            case 'MoO':
                self.memory[self.cell_ptr] += 1

            case 'MOO':
                if self.memory[self.cell_ptr] == 0:
                    level = 1
                    prev = 0
                    self.cmd_ptr += 1
                    if self.cmd_ptr == len(self.code) - 1:
                        return False
                    while level > 0:
                        prev = self.code[self.cmd_ptr]
                        self.cmd_ptr += 1
                        if self.cmd_ptr == len(self.code) - 1:
                            break
                        if self.code[self.cmd_ptr] == self.cmds[7]:
                            level += 1
                        elif self.code[self.cmd_ptr] == self.cmds[0]:
                            level -= 1
                            if prev == 7:
                                level -= 1
                    if level != 0:
                        return True

            case 'OOO':
                self.memory[self.cell_ptr] = 0

            case 'MMM':
                if self.has_register_val:
                    self.memory[self.cell_ptr] = self.register_val
                else:
                    self.register_val = self.memory[self.cell_ptr]
                self.has_register_val = not self.has_register_val

            case 'OOM':
                print(self.memory[self.cell_ptr])

            case 'oom':
                self.memory[self.cell_ptr] = int(input('Integer'))

    def eval(self):
        for i in self.code:
            self.exec(i)