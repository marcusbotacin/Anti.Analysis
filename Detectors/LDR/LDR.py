 # Implemented by Marcus Botacin, based on Vitor Falcão da Rocha's implementation.

class LDR:

    def __init__(self):

        self.found_op1 = None
        self.found_keyword = False

    def check(self, section, address, instruction, op1, op2):

        if instruction in ['mov', 'movsx', 'movzx']:
            if 'fs:0x30' in op2:
                self.found_op1 = op1
                self.found_keyword = True
                return False

        if self.found_keyword:
            if instruction in ['cmp', 'cmpxchg', 'mov', 'movsx', 'movzx']:
                if '[' + self.found_op1 + '+0xc]' in op1 or '[' + self.found_op1 + '+0xc]' in op2:
                    self.clear()
                    print "\"LDR\" Detected! Section: <%s> Address: 0x%s" % (section, address)

    def clear(self):

        self.found_op1 = None
        self.found_keyword = False
