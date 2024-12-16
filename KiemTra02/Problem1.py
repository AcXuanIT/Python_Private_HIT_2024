
class Stack:
    def __init__(self, capacity : int):
        """
            Ham khoi tao 1 doi tuong thuoc class Stack \n
            Arge:
                int : capacity
            Returns:
                Stack : Object
        """
        self.__count = 0
        self.__capacity = capacity
        self.__stack = []

    def initialization(self, capacity : int):
        """
            Ham gan lai gia tri cua capacity \n
            Args:
                int : capacity
        """
        self.__capacity = capacity

    def isEmpty(self) -> bool:
        """
            Ham kiem tra xem stack co rong khong \n
            Returns:
                True : stack rong
                False : stack khong rong
        """
        return self.__count == 0
    
    def isFull(self) -> bool:
        """
            Ham kiem tra xem stack da full phan tu chua \n
            Returns:
                True : stack full
                False : stack not full
        """
        return self.__count == self.__capacity
    
    def pop(self) -> int:
        """
            Ham loai bo phan tu tren cung va tra ve gia tri do \n
            Return:
                int : top element
        """
        self.__count -= 1
        value = self.__stack[self.__count]
        self.__stack.remove(value)
        return value

    def push(self, value : int) -> int:
        """
            Ham them gia tri vao vi tri tren cung cua Stack \n
            Args:
                int : element
        """
        if self.isFull():
            return
        self.__count += 1
        self.__stack.append(value)

    def top(self) -> int:
        """
            Ham tra ve gia tri tren cung cua Stack, nhung khong loai bo \n
            Returns:
                int : top element
        """
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

