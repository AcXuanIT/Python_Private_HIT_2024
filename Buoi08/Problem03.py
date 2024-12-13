class Stack:
    def __init__(self, capacity):
        self.__count = 0
        self.__capacity = capacity
        self.__stack = []

    def initialization(self, capacity):
        self.__capacity = capacity

    def isEmpty(self):
        return self.__count == 0
    
    def isFull(self):
        return self.__count == self.__capacity
    
    def pop(self):
        self.__count -= 1
        value = self.__stack[self.__count]
        self.__stack.remove(value)
        return value

    def push(self, value):
        if self.isFull():
            return
        self.__count += 1
        self.__stack.append(value)

    def top(self):
        if self.isEmpty():
            return
        return self.__stack[self.__count-1]

stack1 = Stack(5)
stack1.push(1)
stack1.push(2)
print(stack1.isFull())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.isEmpty())

