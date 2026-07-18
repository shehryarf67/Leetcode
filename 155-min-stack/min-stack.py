class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mins_stack = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)

        if not self.mins_stack or value <= self.mins_stack[-1]:
            self.mins_stack.append(value)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] == self.mins_stack[-1]:
            self.mins_stack.pop()

        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()