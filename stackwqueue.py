class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        return self.stack

    def pop(self) -> int:
        num = self.stack[-1]
        self.stack.pop(-1)
        return num

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False
