from ch06.instructions.base.Instruction import Index16Instruction

class CHECK_CAST(Index16Instruction):
    def execute(self, frame):
        stack = frame.operandStack
        ref = stack.popRef()
        stack.pushRef(ref)
        if not ref:
            return

        cp = frame.method.getClass().constantPool
        classRef = cp.getConstant(self.index)
        clazz = classRef.resolveClass()
        if not ref.isInstanceOf(clazz):
            raise RuntimeError("java.lang.ClassCastException")


