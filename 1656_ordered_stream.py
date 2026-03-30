# [EASY] https://leetcode.com/problems/design-an-ordered-stream
# Completed 2026/03/30
class OrderedStream:

    def __init__(self, n: int):
        self.pnt = 0
        self.stream = [False] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value
        ret = []
        while self.pnt < len(self.stream):
            if not self.stream[self.pnt]:
                break
            ret.append(self.stream[self.pnt])
            self.pnt += 1
        return ret


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)