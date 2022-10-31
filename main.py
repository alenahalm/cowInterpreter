from cow.interpreter import Interpreter

file = open('hello.cow')
cmds = '\n'.join(file.readlines())

interp = Interpreter(cmds)
interp.eval()