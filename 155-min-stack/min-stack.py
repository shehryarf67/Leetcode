class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        if value < self.min:
            self.min = value

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack:
            return 

        self.stack.pop()
        if self.stack:
            self.min = min(self.stack)
        else:
            self.min = float('inf')
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()