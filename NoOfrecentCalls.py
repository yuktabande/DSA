class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        count = 0
        i = 0
        self.queue.append(t)
        while i < len(self.queue):
            if self.queue[i] >= t-3000 and self.queue[i] <= t:
                count += 1
                i += 1
            else:
                self.queue.pop(0)
        return count 


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
