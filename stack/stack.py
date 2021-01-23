# Q. Design an queue using linkedlist and have basic capabilities of add , delete and get methods


class AStack:

    def __init__(self):
        """
        initialize stack data structure using list.
        """
        self.stack = []
        self.top = -1
        
    def push(self, val: int) -> None:
        """
        add a val at the top of the stack
        """
        self.stack.append(val)
        self.top += 1

    def pop(self) -> None:
        """
        delete the top most val in the stack
        """
        if self.top == -1:
            return

        self.stack.pop(-1)
        self.top -= 1

    def get_top(self) -> int:
        """
        get the top most element in the stack, if stack is not empty
        """
        if self.top == -1:
            return
        else:
            return self.stack[self.top]
    
    def __str__(self):
        return "<-".join(list(map(str,self.stack[::-1])))

def main():
    stack = AStack()
    stack.push(5)
    stack.push(7)
    stack.push(9)
    stack.pop()
    stack.push(11)
    print("Stack Top: {}".format(stack.get_top()))
    print(stack)

if __name__ == "__main__":
    main()
