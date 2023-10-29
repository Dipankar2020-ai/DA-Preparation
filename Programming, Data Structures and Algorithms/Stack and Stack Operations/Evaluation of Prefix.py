'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

class Evaluation:
    def __init__(self):
        self.stack=[]
    def isEmpty(self):
        return self.stack==[]
    def push(self,op):
        self.stack.append(op)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return '$'
    def evaluatePrefix(self,exp):
        for c in exp[-1::-1]:
            if c.isdigit():
                self.push(c)
            else:
                a=self.pop()
                b=self.pop()
                self.push(str(eval(b+c+a)))
        return int(self.pop())
e=Evaluation()
print(e.evaluatePrefix('+2**347'))
    
