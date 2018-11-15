from ch08.rtda.Stack import Stack

class Thread():
    def __init__(self):
        self.pc = 0
        self.stack = Stack(1024)

    def pushFrame(self, frame):
        self.stack.push(frame)

    def popFrame(self):
        return self.stack.pop()

    def currentFrame(self):
        return self.stack.top()

    def newFrame(self, method):
        from ch08.rtda.Frame import Frame
        return Frame(self, method)

    def topFrame(self):
        return self.stack.top()

    def isStackEmpty(self):
        return self.stack.isEmpty()

