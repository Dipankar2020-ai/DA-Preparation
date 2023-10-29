'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

class Stack:
    def __init__(self):
        self.stack=[]
    def isEmpty(self):
        return self.stack==[]
    def push(self,ele):
        self.stack.append(ele)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return -1
            
    def peek(self):
        if not self.stack1.isEmpty():
            return self.stack[-1]
        else:
            return -1
s=Stack()

while True:
    print("Push ")
    print("Pop ")
    print("Peak")
    print("Exit")
    do=input("What exactly you want to do : ")
    if do=="Push":
        ele=int(input("Enter the element to insert into stack: "))
        s.push(ele)
    elif do=='Pop':
        ele=s.pop()
        if ele==-1:
            print("Stack is empty")
        else:
            print("Deleted element from stack is ={0}".format(ele))
    elif do=='Peak':
        if ele==-1:
            print("Stack is empty")
        else:
            print("Top of the Stack element is ={} ".format(ele))
    elif do=="Exit":
        break
