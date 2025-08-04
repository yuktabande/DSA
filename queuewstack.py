class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
       self.queue.append(x)
       return self.queue 

    def pop(self) -> int:
        num = self.queue[0]
        self.queue.pop(0)
        return num

    def peek(self) -> int:
        return self.queue[0] 

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False
