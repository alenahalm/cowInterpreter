from cow.interpreter import Interpreter

file = open('hello.cow')
cmds = []
for i in file.readlines():
    cmds.extend(i.strip().split(' '))


interp = Interpreter(cmds)
interp.eval()
