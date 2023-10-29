'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

class Parenthesis:
    
    def __init__(self):
        self.stack=[]
    def check(self,exp):
        for i in range(len(exp)):
            if exp[i]=='(' or exp[i]=='{' or exp[i]=='[':
                self.stack.append(exp[i])
                continue
            if len(self.stack)==0:
                return False
            if exp[i]==')':
                char=self.stack.pop()
                if char!='(':
                    return False
            if exp[i]=='}':
                char=self.stack.pop()
                if char!='{':
                    return False
            if exp[i]==']':
                char=self.stack.pop()
                if char!='[':
                    return False
        if len(self.stack):
            return False
        else:
            return True
p=Parenthesis()
expr=input("Enter Expression: ")

if p.check(expr):
    print("Given expression is valid ")
else:
    print("Given expression is invlaid")
    
        
            
