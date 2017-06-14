# Implemented by Marcus Botacin, based on Vitor's implementation.

class SizeOfImage:

    def __init__(self):

        self.found_op1 = None
        self.found_keyword = False
        self.found_op2 = None
        self.found_keyword2 = False
        self.found_op3 = None
        self.found_keyword3 = False

    def check(self, section, address, instruction, op1, op2):

        if instruction in ['mov', 'movsx', 'movzx']:
            if 'fs:0x30' in op2:
                self.found_op1 = op1
                self.found_keyword = True
                return False

        if self.found_keyword:
            if instruction in ['mov', 'movsx', 'movzx']:
                if '[' + self.found_op1 + '+0xc]' in op2:
                    self.found_op2 = op1
                    self.found_keyword2 = True

        if self.found_keyword2:
            if instruction in ['mov', 'movsx', 'movzx']:
                if '[' + self.found_op2 + '+0xc]' in op2:
                    self.found_op3 = op1
                    self.found_keyword3 = True

        if self.found_keyword3:
            if instruction in ['addw','add','sub']:
                if '['+self.found_op3 + '20]':
                    print "\"SizeOfImage\" Detected! Section: <%s> Address: 0x%s" % (section, address)
                    self.clear()


    def clear(self):

        self.found_op1 = None
        self.found_keyword = False
        self.found_op2 = None
        self.found_keyword2 = False
        self.found_op3 = None
        self.found_keyword3 = False
