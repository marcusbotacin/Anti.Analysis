 # Implemented by Marcus Botacin, based on Vitor Falcão da Rocha's implementation.

class HardwareBreakpoint:

    def __init__(self):

        self.seh = True
        self.found_op = None
        self.found_first = False
        self.found_second = False

    def check(self, section, address, instruction, op1, op2):

        if instruction in ['mov','movsx','movzx'] and 'fs:0x0' in op1 and 'rsp' in op2:
            self.seh = True

        elif self.seh==True and instruction in ['mov','movsx','movzx'] and 'rsp+0xc' in op2:
            self.found_first=True
            self.found_op=op1

        elif self.found_first==True and instruction in ['mov','movsx','movzx','cmp','cmpxchg'] and self.found_op in op2 and ('0x4' in op2 or '0x8' in op2 or '0xc' in op2 or '0x10' in op2):
            self.found_second=True

        if self.found_second==True:
            self.clear()
            print "\"HardwareBreakpoint\" Detected! Section: <%s> Address: 0x%s" % (section, address)

    def clear(self):

        self.seh=False
        self.found_op = None
        self.found_first = False
        self.found_second = False
